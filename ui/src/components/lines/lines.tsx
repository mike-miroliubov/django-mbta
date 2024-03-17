import { Layout, theme } from "antd"
import Path from '../path';
import Stations from "./stations";
import { LinesProvider } from "./lines-provider";
import { LinesMenu } from "./lines-menu";

const { Content } = Layout;

const Lines = () => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  // pass state in context to child components
  return (
    <LinesProvider>
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
    </LinesProvider>
  )
}

export default Lines