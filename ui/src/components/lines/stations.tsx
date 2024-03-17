import StationService from "../../services/station-service"
import { useLinesState } from "./lines-provider";
import { useQuery } from "@tanstack/react-query";

const stationService = new StationService()

const Stations = () => {
    const linesState = useLinesState()

    const stations = useQuery({
        queryKey: ['stations', linesState.selectedBranchId],
        queryFn: async () => {
            if (linesState.selectedBranchId) {
                return stationService.getStations(linesState.selectedBranchId)
            }
            return []
        },
        staleTime: 1000 * 60 // refresh every hour
    })

    if (!linesState.selectedBranchId) {
        return <div>Select branch to display stations</div>
    }
    if (stations.data && stations.data.length > 0) {
        return <ul>{stations.data.map(s => <li key={s.id}>{s.name}</li>)}</ul>
    }

    return <div>No stations on selected branch</div>
}

export default Stations