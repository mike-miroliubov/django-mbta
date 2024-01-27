import React from 'react';
//import './App.css';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Layout, Menu, theme, Breadcrumb } from 'antd';
import { MenuItemType, SubMenuType } from 'antd/es/menu/hooks/useItems';

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

const headerItems: MenuItemType[] = [
  {key: 1, label: 'nav 1'},
  {key: 2, label: 'nav 2'},
  {key: 3, label: 'nav 3'},
]

const siderItems: SubMenuType[] = [
  {
    key: '1', 
    label: `subnav 1`,
    children: [
      { key: 11, label: 'sub1' },
      { key: 12, label: 'sub2' },
      { key: 13, label: 'sub3' },
    ]
  },
  {key: '2', label: `subnav 2`, children: [{ key: 21, label: 'sub4' }]},
  {key: '3', label: `subnav 3`, children: []},
]

function App() {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  return (
    <Layout style={{ height: '100vh' }}>
      <Header style={{ display: 'flex', alignItems: 'center' }}>
        <Menu
            theme="dark"
            mode="horizontal"
            defaultSelectedKeys={['2']}
            items={headerItems}
            style={{ flex: 1, minWidth: 0 }}
          />
      </Header>
      <Layout>
        <Sider width={200} style={{ background: colorBgContainer }}>
          <Menu
            mode="inline"
            defaultSelectedKeys={['11']}
            defaultOpenKeys={['1']}
            style={{ height: '100%', borderRight: 0 }}
            items={siderItems}
          />
        </Sider>

        <Layout style={{ padding: '0 24px 24px' }}>
          <Breadcrumb style={{ margin: '16px 0' }}>
            <Breadcrumb.Item>Whatever</Breadcrumb.Item>
            <Breadcrumb.Item>Whatever</Breadcrumb.Item>
            <Breadcrumb.Item>Whatever</Breadcrumb.Item>
          </Breadcrumb>
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
