import { Menu } from 'antd';
import { MenuItemType } from 'antd/es/menu/hooks/useItems';
import Tab from '../model/tab'
import { useNavigate } from "react-router-dom";

const headerItems: MenuItemType[] = [
    {key: Tab.LINES.toString(), label: 'Lines'},
    {key: Tab.TRAINS.toString(), label: 'Trains'},
    {key: Tab.CURRENT.toString(), label: 'Current State'},
  ]

const HeaderMenu = (props: { tab: Tab }) => {
    const navigate = useNavigate()

    const go = (info: { key: any }) => {
        console.log(`/${info.key}`)
        navigate(`/${info.key}`)
    }

    return (
        <Menu
            theme="dark"
            mode="horizontal"
            defaultSelectedKeys={[props.tab.toString()]}
            items={headerItems}
            onClick={go}
            style={{ flex: 1, minWidth: 0 }} />
    )
}

export default HeaderMenu