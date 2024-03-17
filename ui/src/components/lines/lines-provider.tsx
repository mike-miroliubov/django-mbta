import { PropsWithChildren, createContext, useContext, useEffect, useReducer } from "react";
import Line from "../../entity/line";
import LineService from "../../services/lines-service";

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

const lineService = new LineService()

export const LinesProvider: React.FC<PropsWithChildren> = ({ children }: PropsWithChildren) => {
    const [state, dispatch] = useReducer(linesReducer, { lines: [] })
    useEffect(() => {
        lineService.getLines().then(lines => {
          dispatch(new LinesLoadedEvent(lines))
        })
      }, [])

    return (
        <LinesContext.Provider value={state}>
            <LinesDispatchContext.Provider value={dispatch}>
                { children }
            </LinesDispatchContext.Provider>
        </LinesContext.Provider>
    )
}

const linesReducer = (state: LinesState, event: LinesEvent) => {
    switch (event.type) {
      case "LINES_LOADED": {
        const linesLoaded = event as LinesLoadedEvent
        return { ...state, lines: linesLoaded.lines }
      }
      case "BRANCH_SELECTED": {
        const branchSelected = event as BranchSelectedEvent
        return { ...state, selectedBranchId: branchSelected.selectedBranchId }
      }
      default: {
        throw Error(`Unexpected event type ${event.type}`)
      }
    }
  }


export const useLinesState = () => useContext(LinesContext)
export const useLinesDispatch = () => useContext(LinesDispatchContext)