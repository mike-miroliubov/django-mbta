import { useQuery } from '@tanstack/react-query'
import Line from '../entity/line'
import {api} from './api'

interface LineResponse {
    lines: Line[]
}

const getLines: () => Promise<Line[]> = async () => {
    const response = await api.get<LineResponse>('v1/lines')
    return response.data.lines
}

export const useLinesQuery = () => useQuery({ 
    queryKey: ['lines'], 
    queryFn: getLines,
    staleTime: 1000 * 60 // refresh every hour
})