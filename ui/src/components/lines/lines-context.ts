import { createContext } from "react";
import Line from "../../entity/line";

export interface LinesState {
    lines: Line[]
    selectedBranchId?: string
}

export type LinesEventType = 'LINES_LOADED' | 'BRANCH_SELECTED'

export interface LinesEvent {
    type: LinesEventType
}

export class LinesLoadedEvent implements LinesEvent {
    readonly type: LinesEventType = 'LINES_LOADED'
    lines: Line[]

    constructor(lines: Line[]) {
        this.lines = lines
    }
}

export class BranchSelectedEvent implements LinesEvent {
    readonly type: LinesEventType = 'BRANCH_SELECTED'
    selectedBranchId: string

    constructor(selectedBranchId: string) {
        this.selectedBranchId = selectedBranchId
    }
}

export const LinesContext = createContext<LinesState>({ lines: [] })
export const LinesDispatchContext = createContext<React.Dispatch<LinesEvent> | null>(null)