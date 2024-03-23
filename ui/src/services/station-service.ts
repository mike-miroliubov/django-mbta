import { useQuery } from "@tanstack/react-query";
import { Station } from "../entity/station";
import { api } from "./api";

interface StationResponse {
    stations: Station[]
}

const getStations = async (branchId: string) => {
    const response = await api.get<StationResponse>(`v1/branches/${branchId}/stations`)
    return response.data.stations
}

export const useStationsQuery = (branchId?: string) => useQuery({
    queryKey: ['stations', branchId],
    queryFn: async () => {
        if (!branchId) {
            return []
        }

        return getStations(branchId)
    },
    staleTime: 1000 * 60 // refresh every hour
})