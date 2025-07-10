// API 请求工具类
// 动态检测API基础URL
function getBaseUrl(): string {
  // 在uni-app环境中，如果是H5端且使用了代理，直接使用相对路径
  if (typeof window !== 'undefined' && window.location) {
    const { protocol, hostname, port } = window.location
    
    // 如果是外网访问（包含clackypaas.com域名），使用代理
    if (hostname.includes('clackypaas.com')) {
      return '' // 使用相对路径，通过vite代理
    }
    
    // 本地开发环境
    if (hostname === 'localhost' || hostname === '127.0.0.1') {
      return '' // 使用代理
    }
  }
  
  // 默认返回本地后端地址
  return 'http://localhost:8000'
}

const BASE_URL = getBaseUrl()

interface RequestOptions {
  method?: 'GET' | 'POST' | 'PUT' | 'DELETE'
  data?: any
  headers?: Record<string, string>
}

interface ApiResponse<T = any> {
  success: boolean
  data?: T
  message?: string
  error?: string
}

// 通用请求函数
export async function request<T = any>(
  url: string, 
  options: RequestOptions = {}
): Promise<ApiResponse<T>> {
  const { method = 'GET', data, headers = {} } = options
  
  try {
    const config: UniApp.RequestOptions = {
      url: BASE_URL + url,
      method: method as any,
      header: {
        'Content-Type': 'application/json',
        ...headers
      },
      data: data || {},
      timeout: 10000
    }

    const response = await uni.request(config)
    
    if (response.statusCode >= 200 && response.statusCode < 300) {
      return {
        success: true,
        data: response.data as T
      }
    } else {
      return {
        success: false,
        error: `HTTP ${response.statusCode}: ${response.errMsg || 'Request failed'}`
      }
    }
  } catch (error: any) {
    return {
      success: false,
      error: error.message || 'Network error'
    }
  }
}

// API 接口定义
export const api = {
  // 用户相关
  user: {
    login: (data: { username: string; password: string }) =>
      request('/api/v1/auth/login', { method: 'POST', data }),
    register: (data: { username: string; email: string; password: string }) =>
      request('/api/v1/users/', { method: 'POST', data }),
    getProfile: () => request('/api/v1/users/me'),
    updateProfile: (data: any) => request('/api/v1/users/me', { method: 'PUT', data })
  },
  
  // 文章相关
  posts: {
    list: (params?: { skip?: number; limit?: number }) => {
      const query = params ? `?skip=${params.skip || 0}&limit=${params.limit || 10}` : ''
      return request(`/api/v1/posts/${query}`)
    },
    getPublished: (params?: { skip?: number; limit?: number }) => {
      const query = params ? `?skip=${params.skip || 0}&limit=${params.limit || 10}` : ''
      return request(`/api/v1/posts/published${query}`)
    },
    getById: (id: number) => request(`/api/v1/posts/${id}`),
    create: (data: any) => request('/api/v1/posts/', { method: 'POST', data }),
    update: (id: number, data: any) => request(`/api/v1/posts/${id}`, { method: 'PUT', data }),
    delete: (id: number) => request(`/api/v1/posts/${id}`, { method: 'DELETE' }),
    getMy: (params?: { skip?: number; limit?: number }) => {
      const query = params ? `?skip=${params.skip || 0}&limit=${params.limit || 10}` : ''
      return request(`/api/v1/posts/my${query}`)
    }
  },
  
  // 统计相关
  stats: {
    dashboard: () => request('/api/v1/stats/dashboard')
  }
}