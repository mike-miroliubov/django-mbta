import React, { useContext } from "react";
import StationService from "../../services/station-service"
import { Station } from "../../entity/station"
import { LinesContext } from "./lines-context";

const stationService = new StationService()

const Stations = () => {
    const context = useContext(LinesContext)
    // store station as local state
    const [stations, setStations] = React.useState<Station[]>([])
    
    React.useEffect(() => {
        const getStations = async (branchId: string) => {
            const stations = await stationService.getStations(branchId)
            setStations(stations)
        }

        if (context.selectedBranchId) {
            getStations(context.selectedBranchId)
        }
    }, [context])
    
    const buildList = () => {
        if (!context.selectedBranchId) {
            return <></>
        }
        if (stations.length > 0) {
            return <ul>{stations.map(s => <li key={s.id}>{s.name}</li>)}</ul>
        }
        else return <div>No stations on selected branch</div>
    }

    return buildList()
}

export default Stations