import { Menu } from 'antd';
import { MenuItemType } from 'antd/es/menu/hooks/useItems';

const headerItems: MenuItemType[] = [
    {key: 1, label: 'nav 1'},
    {key: 2, label: 'nav 2'},
    {key: 3, label: 'nav 3'},
  ]

const HeaderMenu = () => {
    return (
        <Menu
            theme="dark"
            mode="horizontal"
            defaultSelectedKeys={['2']}
            items={headerItems}
            style={{ flex: 1, minWidth: 0 }} />
    )
}

export default HeaderMenu