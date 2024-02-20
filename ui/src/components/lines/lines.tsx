import { Layout, theme } from "antd"
import Path from '../path';
import LineService from "../../services/lines-service";
import React, { useReducer } from "react";
import Line from "../../entity/line";
import Stations from "./stations";
import { LinesContext, LinesState } from "./lines-context";
import { LinesMenu } from "./lines-menu";

const lineService = new LineService()
const { Content } = Layout;

const Lines = () => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  const [state, dispatch] = useReducer(linesReducer, {lines: []})

  React.useEffect(() => {
    lineService.getLines().then(lines => {
      dispatch(new LinesLoadedEvent(lines))
    })
  }, [])

  const onItemSelected = (key: string) => { 
    dispatch(new BranchSelectedEvent(key))
  }

  return (
    <Layout>
      { /* pass state in context to child components */ }
      <LinesContext.Provider value={state}>
        <LinesMenu onItemSelected={onItemSelected} />

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
      </LinesContext.Provider>
    </Layout>
  )
}

export default Lines

type LinesEventType = 'LINES_LOADED' | 'BRANCH_SELECTED'

interface LinesEvent {
  type: LinesEventType
}

class LinesLoadedEvent implements LinesEvent {
  readonly type: LinesEventType = 'LINES_LOADED'
  lines: Line[]

  constructor(lines: Line[]) {
    this.lines = lines
  }
}

class BranchSelectedEvent implements LinesEvent {
  readonly type: LinesEventType = 'BRANCH_SELECTED'
  selectedBranchId: string

  constructor(selectedBranchId: string) {
    this.selectedBranchId = selectedBranchId
  }
}

const linesReducer = (state: LinesState, event: LinesEvent) => {
  switch(event.type) {
    case "LINES_LOADED": {
      const linesLoaded = event as LinesLoadedEvent
      return {...state, lines: linesLoaded.lines}
    }
    case "BRANCH_SELECTED": {
      const branchSelected = event as BranchSelectedEvent
      return {...state, selectedBranchId: branchSelected.selectedBranchId}
    }
    default: {
      throw Error(`Unexpected event type ${event.type}`)
    }
  }
}