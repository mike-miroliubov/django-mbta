import React from "react";
import StationService from "../services/station-service"
import { Station } from "../entity/station"

const stationService = new StationService()

const Stations = ({branchId}: {branchId?: string}) => {
    const [stations, setStations] = React.useState<Station[]>([])
    
    React.useEffect(() => {
        const getStations = async (branchId: string) => {
            const stations = await stationService.getStations(branchId)
            setStations(stations)
        }

        if (branchId) {
            getStations(branchId)
        }
    }, [branchId])
    
    const buildList = () => {
        if (!branchId) {
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