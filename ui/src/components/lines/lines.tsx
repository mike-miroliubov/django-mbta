import { Layout, theme } from "antd"
import SiderMenu, { SiderGroup } from '../sider-menu';
import Path from '../path';
import LineService from "../../services/lines-service";
import React from "react";
import Line from "../../entity/line";
import Stations from "./stations";
import { LinesContext } from "./lines-context";
import { LinesMenu } from "./lines-menu";

const lineService = new LineService()
const { Content } = Layout;

const Lines = () => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  // useState React Hook sets component state
  // https://react.dev/learn/state-a-components-memory
  const [lines, setLines] = React.useState<Line[]>([])
  const [selectedBranchId, setSelectedBranchId] = React.useState<string>('')

  React.useEffect(() => {
    lineService.getLines().then(lines => {
      setLines(lines)
    })
  }, [])

  const onItemSelected = (key: string) => { 
    setSelectedBranchId(key)
  }

  return (
    <Layout>
      { /* pass state in context to child components */ }
      <LinesContext.Provider value={{lines: lines, selectedBranchId: selectedBranchId}}>
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