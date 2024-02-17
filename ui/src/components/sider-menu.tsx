import { Menu } from 'antd';
import { SubMenuType, MenuItemType } from 'antd/es/menu/hooks/useItems';
import { useState } from 'react';
import BranchService from '../services/branch-service';

// const siderItems: SubMenuType[] = [
//   {
//     key: '1',
//     label: `subnav 1`,
//     children: [
//       { key: 11, label: 'sub1' },
//       { key: 12, label: 'sub2' },
//       { key: 13, label: 'sub3' },
//     ]
//   },
//   { key: '2', label: `subnav 2`, children: [{ key: 21, label: 'sub4' }] },
//   { key: '3', label: `subnav 3`, children: [] },
// ]

export interface SiderGroup {
  id: string
  label: string
  color: string
}

const branchService = new BranchService()

interface SiderProps { 
  groups?: SiderGroup[]
  onItemSelected?: (key: string) => void
}

const SiderMenu = ({ groups, onItemSelected }: SiderProps) => {
  const [openedGroups, setOpenedGroups] = useState<string[]>([])
  const [menuItems, setMenuItems] = useState<SubMenuType[]>([])

  if (menuItems.length == 0 && groups && groups.length > 0) {
    setMenuItems((groups || []).map(it => ({ key: it.id, label: it.label, children: [] })))
  }

  const onGroupOpen = async (openKeys: string[]) => {
    // create copy of menuItems, because React cannot recognise changes in object
    const itemsCopy = [...menuItems]

    // find newly opened groups
    const newlyOpened = openKeys.filter(key => !openedGroups.includes(key))

    await Promise.all(newlyOpened.map(async (openKey) => {
      const branches = await branchService.getBranches(openKey)
      const item = itemsCopy.find(it => it.key == openKey)
      if (item) {
        item.children = branches.map(it => ({ key: it.id, label: it.name }))
      }
    }))

    setMenuItems(itemsCopy)
    setOpenedGroups(openKeys)
  }

  return (
    <Menu
      mode="inline"
      //defaultSelectedKeys={['11']}
      defaultOpenKeys={openedGroups}
      style={{ height: '100%', borderRight: 0 }}
      items={[...menuItems]}
      onOpenChange={onGroupOpen}
      onSelect={onItemSelected && ((info) => {
        onItemSelected(info.key)
        info.domEvent.stopPropagation()
      })}
    />
  );
}

export default SiderMenu