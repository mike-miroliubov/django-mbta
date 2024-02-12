import { Layout, theme } from "antd"
import SiderMenu, { SiderGroup } from './sider-menu';
import Path from './path';
import LineService from "../services/lines-service";
import React from "react";
import Line from "../entity/line";

const lineService = new LineService()

const Lines = () => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  const { Content, Sider } = Layout;

  // useState React Hook sets component state
  // https://react.dev/learn/state-a-components-memory
  const [lines, setLines] = React.useState<Line[]>([])

  React.useEffect(() => {
    lineService.getLines().then(lines => {
      setLines(lines)
    })
  }, [])

  // (lines: Line[]) => SiderGroup[]
  const linesToSiderGroups = (lines: Line[]) => lines.map(l => ({ id: l.id, label: l.name, color: l.color } as SiderGroup))
  
  return (
    <Layout>
      <Sider width={200} style={{ background: colorBgContainer }}>
        <SiderMenu groups={linesToSiderGroups(lines)} />
      </Sider>

      <Layout style={{ padding: '0 24px 24px' }}>
        <Path />
        <Content style={{
          padding: 24,
          margin: 0,
          minHeight: 280,
          background: colorBgContainer,
          borderRadius: borderRadiusLG,
        }}>
          {lines.map(l => l.name).join(",")}
        </Content>
      </Layout>
    </Layout>
  )
}

export default Lines