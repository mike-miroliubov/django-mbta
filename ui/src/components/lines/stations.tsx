import React from "react";
import StationService from "../../services/station-service"
import { Station } from "../../entity/station"
import { useLinesState } from "./lines-provider";

const stationService = new StationService()

const Stations = () => {
    const linesState = useLinesState()
    // store station as local state
    const [stations, setStations] = React.useState<Station[]>([])
    
    React.useEffect(() => {
        const getStations = async (branchId: string) => {
            const stations = await stationService.getStations(branchId)
            setStations(stations)
        }

        if (linesState.selectedBranchId) {
            getStations(linesState.selectedBranchId)
        }
    }, [linesState])
    
    if (!linesState.selectedBranchId) {
        return <div>Select branch to display stations</div>
    }
    if (stations.length > 0) {
        return <ul>{stations.map(s => <li key={s.id}>{s.name}</li>)}</ul>
    }
     
    return <div>No stations on selected branch</div>
}

export default Stations