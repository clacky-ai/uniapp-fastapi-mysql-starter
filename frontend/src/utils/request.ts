// API 请求工具类
const BASE_URL = ''

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
      url: url,
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
  
  // 产品相关
  product: {
    list: (params?: { skip?: number; limit?: number }) => {
      const query = params ? `?skip=${params.skip || 0}&limit=${params.limit || 10}` : ''
      return request(`/api/v1/products/${query}`)
    },
    get: (id: number) => request(`/api/v1/products/${id}`),
    create: (data: any) => request('/api/v1/products/', { method: 'POST', data }),
    update: (id: number, data: any) => request(`/api/v1/products/${id}`, { method: 'PUT', data }),
    delete: (id: number) => request(`/api/v1/products/${id}`, { method: 'DELETE' })
  },
  
  // 分类相关
  category: {
    list: () => request('/api/v1/categories/'),
    get: (id: number) => request(`/api/v1/categories/${id}`),
    create: (data: any) => request('/api/v1/categories/', { method: 'POST', data }),
    update: (id: number, data: any) => request(`/api/v1/categories/${id}`, { method: 'PUT', data }),
    delete: (id: number) => request(`/api/v1/categories/${id}`, { method: 'DELETE' })
  },
  
  // 订单相关
  order: {
    list: () => request('/api/v1/orders/'),
    get: (id: number) => request(`/api/v1/orders/${id}`),
    create: (data: any) => request('/api/v1/orders/', { method: 'POST', data }),
    update: (id: number, data: any) => request(`/api/v1/orders/${id}`, { method: 'PUT', data }),
    delete: (id: number) => request(`/api/v1/orders/${id}`, { method: 'DELETE' })
  },
  
  // 统计相关
  stats: {
    dashboard: () => request('/api/v1/stats/dashboard')
  }
}