import { useStationsQuery } from "../../services/station-service"
import { useLinesState } from "./lines-provider";

const Stations = () => {
    const linesState = useLinesState()

    const stations = useStationsQuery(linesState.selectedBranchId)

    if (!linesState.selectedBranchId) {
        return <div>Select branch to display stations</div>
    }
    if (stations.data && stations.data.length > 0) {
        return <ul>{stations.data.map(s => <li key={s.id}>{s.name}</li>)}</ul>
    }

    return <div>No stations on selected branch</div>
}

export default Stations