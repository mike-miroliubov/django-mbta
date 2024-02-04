import { Layout, theme } from "antd"
import SiderMenu from './sider-menu';
import Path from './path';

const Current = () => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  const { Content, Sider } = Layout;

  return (
    <Layout>
      <Layout style={{ padding: '0 24px 24px' }}>
        <Path />
        <Content style={{
          padding: 24,
          margin: 0,
          minHeight: 280,
          background: colorBgContainer,
          borderRadius: borderRadiusLG,
        }}>
          Content Current
        </Content>
      </Layout>
    </Layout>
  )
}

export default Current