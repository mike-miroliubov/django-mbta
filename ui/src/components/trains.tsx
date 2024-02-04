import { Layout, theme } from "antd"
import SiderMenu from './sider-menu';
import Path from './path';

const Trains = () => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  const { Content, Sider } = Layout;

  return (
    <Layout>
      <Sider width={200} style={{ background: colorBgContainer }}>
        <SiderMenu />
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
          Content Trains
        </Content>
      </Layout>
    </Layout>
  )
}

export default Trains