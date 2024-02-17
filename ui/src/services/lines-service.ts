import Line from '../entity/line'
import {api} from './api'

interface LineResponse {
    lines: Line[]
}

export default class LineService {
    public async getLines(): Promise<Line[]> {
        const response = await api.get<LineResponse>('v1/lines')
        return response.data.lines
    }
}