import Branch from "../entity/branch";
import { api } from "./api";

interface BranchResponse {
    branches: Branch[]
}

export default class BranchService {
    public async getBranches(lineId: string): Promise<Branch[]> {
        const response = await api.get(`v1/lines/${lineId}/branches`)
        return (response.data as BranchResponse).branches
    }
}