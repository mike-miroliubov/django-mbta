import { Layout, theme } from "antd"
import Path from '../path';
import LineService from "../../services/lines-service";
import React, { useReducer } from "react";
import Stations from "./stations";
import { BranchSelectedEvent, LinesContext, LinesDispatchContext, LinesEvent, LinesLoadedEvent, LinesState } from "./lines-context";
import { LinesMenu } from "./lines-menu";

const lineService = new LineService()
const { Content } = Layout;

const Lines = () => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  const [state, dispatch] = useReducer(linesReducer, { lines: [] })

  React.useEffect(() => {
    lineService.getLines().then(lines => {
      dispatch(new LinesLoadedEvent(lines))
    })
  }, [])

  // pass state in context to child components
  return (
    <LinesContext.Provider value={state}>
      <LinesDispatchContext.Provider value={dispatch}>
        <Layout>
          <LinesMenu />

          <Layout style={{ padding: '0 24px 24px' }}>
            <Path />
            <Content style={{
              padding: 24,
              margin: 0,
              minHeight: 280,
              background: colorBgContainer,
              borderRadius: borderRadiusLG,
            }}>
              <Stations />
            </Content>
          </Layout>
        </Layout>
      </LinesDispatchContext.Provider>
    </LinesContext.Provider>
  )
}

export default Lines

const linesReducer = (state: LinesState, event: LinesEvent) => {
  switch (event.type) {
    case "LINES_LOADED": {
      const linesLoaded = event as LinesLoadedEvent
      return { ...state, lines: linesLoaded.lines }
    }
    case "BRANCH_SELECTED": {
      const branchSelected = event as BranchSelectedEvent
      return { ...state, selectedBranchId: branchSelected.selectedBranchId }
    }
    default: {
      throw Error(`Unexpected event type ${event.type}`)
    }
  }
}