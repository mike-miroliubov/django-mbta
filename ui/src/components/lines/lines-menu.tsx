import { Layout, theme } from "antd"
import SiderMenu, { SiderGroup } from '../sider-menu';
import React from "react";
import Line from "../../entity/line";
import { BranchSelectedEvent, useLinesDispatch, useLinesState } from "./lines-provider";

const { Sider } = Layout;

const linesToSiderGroups = (lines: Line[]) => lines.map(l => ({ id: l.id, label: l.name, color: l.color } as SiderGroup))

export const LinesMenu: React.FC = () => {
    // nested object deconstruction
    const { token: { colorBgContainer } } = theme.useToken();
    const linesState = useLinesState()
    const linesDispatch = useLinesDispatch()
    
    return (
        <Sider width={200} style={{ background: colorBgContainer }}>
          <SiderMenu groups={linesToSiderGroups(linesState.lines)} onItemSelected={(key) => linesDispatch && linesDispatch(new BranchSelectedEvent(key))} />
        </Sider>
    )
}