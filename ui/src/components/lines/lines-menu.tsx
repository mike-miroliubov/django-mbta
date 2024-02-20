import { Layout, theme } from "antd"
import SiderMenu, { SiderGroup } from '../sider-menu';
import React, { useContext } from "react";
import Line from "../../entity/line";
import { LinesContext } from "./lines-context";

const { Sider } = Layout;

const linesToSiderGroups = (lines: Line[]) => lines.map(l => ({ id: l.id, label: l.name, color: l.color } as SiderGroup))

export const LinesMenu: React.FC<{onItemSelected: (key: string) => void}> = ({onItemSelected}) => {
    // nested object deconstruction
    const { token: { colorBgContainer, borderRadiusLG } } = theme.useToken();
    const context = useContext(LinesContext)
    
    return (
        <Sider width={200} style={{ background: colorBgContainer }}>
          <SiderMenu groups={linesToSiderGroups(context.lines)} onItemSelected={onItemSelected} />
        </Sider>
    )
}