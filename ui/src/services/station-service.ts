import { Station } from "../entity/station";
import { api } from "./api";

interface StationResponse {
    stations: Station[]
}

export default class StationService {
    public async getStations(branchId: string): Promise<Station[]> {
        const response = await api.get<StationResponse>(`v1/branches/${branchId}/stations`)
        return response.data.stations
    }
}