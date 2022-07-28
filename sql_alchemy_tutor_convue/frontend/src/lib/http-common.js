import axios from 'axios'

const instance = axios.create({
  headers: {
    'Cache-Control': 'no-cache'
  },
  baseURL: '/api/v1'
})

export default instance
