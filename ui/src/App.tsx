//import './App.css';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Layout, theme } from 'antd';
import HeaderMenu from './components/header-menu';
import SiderMenu from './components/sider-menu';
import Path from './components/path';

const queryClient = new QueryClient()

const AppWrapper = () => {
  return (
    <QueryClientProvider client={queryClient}>
      <App />
    </QueryClientProvider>
  )
}

export default AppWrapper

const { Header, Content, Sider } = Layout;

function App() {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  return (
    <Layout style={{ height: '100vh' }}>
      <Header style={{ display: 'flex', alignItems: 'center' }}>
        <HeaderMenu />
      </Header>
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
            Content
          </Content>
        </Layout>
      </Layout>
    </Layout>
  );
}
