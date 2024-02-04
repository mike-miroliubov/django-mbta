//import './App.css';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Layout, theme } from 'antd';
import HeaderMenu from './components/header-menu';
import Lines from './components/lines';
import Trains from './components/trains';
import Current from './components/current';
import Tab from './model/tab';
import { tab } from '@testing-library/user-event/dist/tab';
import { RouterProvider } from 'react-router-dom';
import { createBrowserRouter } from 'react-router-dom'

const queryClient = new QueryClient()

const getActiveTab = (tab: Tab) => {
  switch (tab) {
    case Tab.LINES:
      return <Lines />
    case Tab.TRAINS:
      return <Trains />
    case Tab.CURRENT:
      return <Current />
  }
}

const App = (props: { tab: Tab }) => {
  const { Header } = Layout;

  return (
    <Layout style={{ height: '100vh' }}>
      <Header style={{ display: 'flex', alignItems: 'center' }}>
        <HeaderMenu tab={props.tab} />
      </Header>

      { getActiveTab(props.tab) }
    </Layout>
  );
}

const router = createBrowserRouter([
  {
      path: '/',
      element: App({ tab: Tab.LINES })
  },
  {
      path: '/lines',
      element: App({ tab: Tab.LINES })
  },
  {
      path: '/trains',
      element: App({ tab: Tab.TRAINS })
  },
  {
      path: '/current',
      element: App({ tab: Tab.CURRENT }),
  },
])

const AppWrapper = () => {
  return (
    <QueryClientProvider client={queryClient}>
      <RouterProvider router={router} />
    </QueryClientProvider>
  )
}

export default AppWrapper