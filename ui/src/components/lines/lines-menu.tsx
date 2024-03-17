import { Layout, theme } from "antd"
import SiderMenu, { SiderGroup } from '../sider-menu';
import React from "react";
import Line from "../../entity/line";
import { BranchSelectedEvent, useLinesDispatch, useLinesState } from "./lines-provider";
import { useQuery } from "@tanstack/react-query";
import LineService from "../../services/lines-service";

const { Sider } = Layout;

const linesToSiderGroups = (lines: Line[] | undefined) => lines?.map(l => ({ id: l.id, label: l.name, color: l.color } as SiderGroup))

const lineService = new LineService()

export const LinesMenu: React.FC = () => {
    // nested object deconstruction
    const { token: { colorBgContainer } } = theme.useToken();
    const query = useQuery({ 
        queryKey: ['lines'], 
        queryFn: lineService.getLines,
        staleTime: 1000 * 60 // refresh every hour
    })
    const linesDispatch = useLinesDispatch()
    
    return (
        <Sider width={200} style={{ background: colorBgContainer }}>
          <SiderMenu 
            groups={linesToSiderGroups(query.data)} 
            onItemSelected={(key) => linesDispatch && linesDispatch(new BranchSelectedEvent(key))} />
        </Sider>
    )
}