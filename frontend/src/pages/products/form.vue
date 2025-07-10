<template>
  <view class="form-page">
    <view class="header">
      <text class="title">{{ isEdit ? '编辑商品' : '添加商品' }}</text>
    </view>
    
    <form @submit="handleSubmit">
      <view class="form-group">
        <text class="label">商品名称</text>
        <input 
          class="input" 
          type="text" 
          v-model="form.name" 
          placeholder="请输入商品名称"
        />
      </view>
      
      <view class="form-group">
        <text class="label">商品价格</text>
        <input 
          class="input" 
          type="number" 
          v-model="form.price" 
          placeholder="请输入商品价格"
        />
      </view>
      
      <view class="form-group">
        <text class="label">商品描述</text>
        <textarea 
          class="textarea" 
          v-model="form.description" 
          placeholder="请输入商品描述"
        />
      </view>
      
      <view class="form-group">
        <text class="label">分类</text>
        <picker 
          mode="selector" 
          :range="categories" 
          range-key="name"
          :value="selectedCategoryIndex"
          @change="onCategoryChange"
        >
          <view class="picker">
            {{ selectedCategory ? selectedCategory.name : '请选择分类' }}
          </view>
        </picker>
      </view>
      
      <view class="form-actions">
        <button class="submit-btn" @click="handleSubmit" :disabled="submitting">
          {{ submitting ? '保存中...' : '保存' }}
        </button>
        <button class="cancel-btn" @click="goBack">取消</button>
      </view>
    </form>
  </view>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { api } from '@/utils/request'

interface Category {
  id: number
  name: string
}

interface ProductForm {
  name: string
  price: number | string
  description: string
  category_id: number | null
}

const form = ref<ProductForm>({
  name: '',
  price: '',
  description: '',
  category_id: null
})

const categories = ref<Category[]>([])
const selectedCategoryIndex = ref(0)
const submitting = ref(false)
const productId = ref<number | null>(null)

const isEdit = computed(() => productId.value !== null)
const selectedCategory = computed(() => {
  return categories.value[selectedCategoryIndex.value] || null
})

// 获取分类列表
const fetchCategories = async () => {
  try {
    const response = await api.category.list()
    if (response.success) {
      categories.value = response.data || []
    }
  } catch (error) {
    console.error('获取分类失败:', error)
  }
}

// 获取商品详情（编辑模式）
const fetchProduct = async (id: number) => {
  try {
    const response = await api.product.get(id)
    if (response.success && response.data) {
      const product = response.data
      form.value = {
        name: product.name,
        price: product.price,
        description: product.description,
        category_id: product.category_id
      }
      
      // 设置选中的分类
      if (product.category_id) {
        const categoryIndex = categories.value.findIndex(c => c.id === product.category_id)
        if (categoryIndex !== -1) {
          selectedCategoryIndex.value = categoryIndex
        }
      }
    }
  } catch (error) {
    console.error('获取商品详情失败:', error)
  }
}

// 分类选择变化
const onCategoryChange = (e: any) => {
  selectedCategoryIndex.value = e.detail.value
  const category = categories.value[e.detail.value]
  form.value.category_id = category ? category.id : null
}

// 提交表单
const handleSubmit = async () => {
  if (!form.value.name.trim()) {
    uni.showToast({
      title: '请输入商品名称',
      icon: 'none'
    })
    return
  }
  
  if (!form.value.price || Number(form.value.price) <= 0) {
    uni.showToast({
      title: '请输入有效的商品价格',
      icon: 'none'
    })
    return
  }
  
  submitting.value = true
  
  try {
    const data = {
      name: form.value.name.trim(),
      price: Number(form.value.price),
      description: form.value.description.trim(),
      category_id: form.value.category_id
    }
    
    let response
    if (isEdit.value && productId.value) {
      response = await api.product.update(productId.value, data)
    } else {
      response = await api.product.create(data)
    }
    
    if (response.success) {
      uni.showToast({
        title: isEdit.value ? '更新成功' : '创建成功',
        icon: 'success'
      })
      
      setTimeout(() => {
        uni.navigateBack()
      }, 1500)
    } else {
      uni.showToast({
        title: response.error || '保存失败',
        icon: 'none'
      })
    }
  } catch (error: any) {
    uni.showToast({
      title: error.message || '网络错误',
      icon: 'none'
    })
  } finally {
    submitting.value = false
  }
}

// 返回
const goBack = () => {
  uni.navigateBack()
}

onMounted(async () => {
  // 获取页面参数
  const pages = getCurrentPages()
  const currentPage = pages[pages.length - 1]
  const options = (currentPage as any).options || {}
  
  if (options.id) {
    productId.value = Number(options.id)
  }
  
  // 获取分类列表
  await fetchCategories()
  
  // 如果是编辑模式，获取商品详情
  if (productId.value) {
    await fetchProduct(productId.value)
  }
})
</script>

<style scoped>
.form-page {
  padding: 20rpx;
}

.header {
  margin-bottom: 40rpx;
}

.title {
  font-size: 36rpx;
  font-weight: bold;
}

.form-group {
  margin-bottom: 40rpx;
}

.label {
  display: block;
  font-size: 28rpx;
  color: #333;
  margin-bottom: 15rpx;
}

.input, .textarea {
  width: 100%;
  border: 2rpx solid #e1e1e1;
  border-radius: 8rpx;
  padding: 20rpx;
  font-size: 28rpx;
  box-sizing: border-box;
}

.textarea {
  height: 150rpx;
  resize: none;
}

.picker {
  border: 2rpx solid #e1e1e1;
  border-radius: 8rpx;
  padding: 20rpx;
  font-size: 28rpx;
  color: #333;
}

.form-actions {
  margin-top: 60rpx;
  display: flex;
  gap: 30rpx;
}

.submit-btn, .cancel-btn {
  flex: 1;
  border: none;
  border-radius: 8rpx;
  padding: 20rpx;
  font-size: 32rpx;
}

.submit-btn {
  background-color: #007aff;
  color: white;
}

.submit-btn[disabled] {
  background-color: #ccc;
}

.cancel-btn {
  background-color: #f5f5f5;
  color: #333;
}
</style>