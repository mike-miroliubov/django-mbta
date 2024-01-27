import { Menu } from 'antd';
import { SubMenuType } from 'antd/es/menu/hooks/useItems';

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

const SiderMenu = () => {
    return (
        <Menu
            mode="inline"
            defaultSelectedKeys={['11']}
            defaultOpenKeys={['1']}
            style={{ height: '100%', borderRight: 0 }}
            items={siderItems}
          />
    );
}

export default SiderMenu