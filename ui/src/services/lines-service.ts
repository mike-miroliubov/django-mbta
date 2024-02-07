import Line from '../entity/line'
import {api} from './api'

interface LineResponse {
    lines: Line[]
}

export default class LineService {
    public async getLines(): Promise<Line[]> {
        const response = await api.get('v1/lines')
        const data: LineResponse = response.data
        return data.lines
    }
}