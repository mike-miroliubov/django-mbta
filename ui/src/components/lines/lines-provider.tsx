import { PropsWithChildren, createContext, useContext, useReducer } from "react";

export interface LinesState {
    selectedBranchId?: string
}

export type LinesEventType = 'BRANCH_SELECTED'

export interface LinesEvent {
    type: LinesEventType
}

export class BranchSelectedEvent implements LinesEvent {
    readonly type: LinesEventType = 'BRANCH_SELECTED'
    selectedBranchId?: string

    constructor(selectedBranchId: string) {
        this.selectedBranchId = selectedBranchId
    }
}

export const LinesContext = createContext<LinesState>({ })
export const LinesDispatchContext = createContext<React.Dispatch<LinesEvent> | null>(null)

export const LinesProvider: React.FC<PropsWithChildren> = ({ children }: PropsWithChildren) => {
    const [state, dispatch] = useReducer(linesReducer, { selectedBranchId: undefined })

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
      case "BRANCH_SELECTED": {
        const branchSelected = event as BranchSelectedEvent
        console.log(`State change, branch selected: ${branchSelected.selectedBranchId}`)
        return { ...state, selectedBranchId: branchSelected.selectedBranchId }
      }
      default: {
        throw Error(`Unexpected event type ${event.type}`)
      }
    }
  }


export const useLinesState = () => useContext(LinesContext)
export const useLinesDispatch = () => useContext(LinesDispatchContext)