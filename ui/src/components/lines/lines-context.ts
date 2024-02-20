import { createContext } from "react";
import Line from "../../entity/line";

export interface LinesState {
    lines: Line[]
    selectedBranchId?: string
}

export const LinesContext = createContext<LinesState>({ lines: [] })