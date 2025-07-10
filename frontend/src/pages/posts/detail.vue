<template>
	<view class="container">
		<view class="loading" v-if="loading">
			<text class="loading-text">正在加载文章...</text>
		</view>
		
		<view class="error" v-else-if="error">
			<text class="error-text">{{ error }}</text>
			<button class="retry-btn" @click="loadPost">重试</button>
		</view>
		
		<view class="post-detail" v-else-if="post">
			<view class="post-header">
				<text class="post-title">{{ post.title }}</text>
				<view class="post-status" v-if="post.is_published">
					<text class="status-badge published">已发布</text>
				</view>
			</view>
			
			<view class="post-meta">
				<view class="author-info" v-if="post.author">
					<text class="author-name">👤 作者：{{ post.author.full_name || post.author.username }}</text>
				</view>
				<text class="post-date">📅 发布时间：{{ formatDate(post.created_at) }}</text>
				<text class="post-updated" v-if="post.updated_at !== post.created_at">
					🔄 更新时间：{{ formatDate(post.updated_at) }}
				</text>
			</view>
			
			<view class="post-content">
				<text class="content-text">{{ post.content || '暂无内容' }}</text>
			</view>
		</view>
		
		<view class="actions" v-if="!loading && !error">
			<button class="action-btn" @click="goBack">返回列表</button>
			<button class="action-btn secondary" @click="loadPost">刷新</button>
		</view>
	</view>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { api } from '@/utils/request'

interface Author {
	id: number
	username: string
	full_name?: string
}

interface Post {
	id: number
	title: string
	content?: string
	is_published: boolean
	author?: Author
	created_at: string
	updated_at: string
}

const loading = ref(true)
const error = ref('')
const post = ref<Post | null>(null)
const postId = ref<number | null>(null)

const loadPost = async () => {
	if (!postId.value) {
		error.value = '文章ID无效'
		loading.value = false
		return
	}
	
	loading.value = true
	error.value = ''
	
	try {
		const response = await api.posts.getById(postId.value)
		if (response.success && response.data) {
			post.value = response.data
		} else {
			error.value = response.error || '文章加载失败'
		}
	} catch (err: any) {
		error.value = err.message || '网络连接失败'
	} finally {
		loading.value = false
	}
}

const formatDate = (dateString: string) => {
	const date = new Date(dateString)
	return date.toLocaleString('zh-CN', {
		year: 'numeric',
		month: 'short',
		day: 'numeric',
		hour: '2-digit',
		minute: '2-digit'
	})
}

const goBack = () => {
	uni.navigateBack()
}

onMounted(() => {
	// 获取页面参数
	const pages = getCurrentPages()
	const currentPage = pages[pages.length - 1]
	const options = (currentPage as any).options
	
	if (options.id) {
		postId.value = parseInt(options.id)
		loadPost()
	} else {
		error.value = '缺少文章ID参数'
		loading.value = false
	}
})
</script>

<style>
.container {
	padding: 40rpx;
	min-height: 100vh;
	background: linear-gradient(135deg, #a29bfe 0%, #6c5ce7 100%);
}

.loading {
	text-align: center;
	padding: 200rpx 0;
}

.loading-text {
	color: white;
	font-size: 32rpx;
}

.error {
	text-align: center;
	padding: 200rpx 40rpx;
}

.error-text {
	display: block;
	color: #ff6b6b;
	font-size: 32rpx;
	margin-bottom: 40rpx;
}

.retry-btn {
	background: #ff6b6b;
	color: white;
	border: none;
	border-radius: 50rpx;
	padding: 20rpx 40rpx;
	font-size: 28rpx;
}

.post-detail {
	background: white;
	border-radius: 20rpx;
	padding: 40rpx;
	margin-bottom: 60rpx;
	box-shadow: 0 8rpx 30rpx rgba(0, 0, 0, 0.1);
}

.post-header {
	display: flex;
	justify-content: space-between;
	align-items: flex-start;
	margin-bottom: 30rpx;
	padding-bottom: 30rpx;
	border-bottom: 2rpx solid #f1f3f4;
}

.post-title {
	font-size: 42rpx;
	font-weight: bold;
	color: #2d3436;
	flex: 1;
	line-height: 1.4;
}

.post-status {
	margin-left: 20rpx;
}

.status-badge {
	background: #00b894;
	color: white;
	padding: 10rpx 20rpx;
	border-radius: 20rpx;
	font-size: 24rpx;
}

.post-meta {
	margin-bottom: 40rpx;
	padding-bottom: 30rpx;
	border-bottom: 1rpx solid #f1f3f4;
}

.author-info, .post-date, .post-updated {
	display: block;
	color: #636e72;
	font-size: 28rpx;
	margin-bottom: 10rpx;
}

.post-date {
	color: #74b9ff;
}

.post-updated {
	color: #fdcb6e;
}

.post-content {
	line-height: 1.8;
}

.content-text {
	color: #2d3436;
	font-size: 32rpx;
	line-height: 1.8;
	white-space: pre-wrap;
}

.actions {
	display: flex;
	justify-content: center;
	gap: 30rpx;
	margin-bottom: 60rpx;
}

.action-btn {
	background: rgba(255, 255, 255, 0.2);
	color: white;
	border: 2rpx solid rgba(255, 255, 255, 0.3);
	border-radius: 50rpx;
	padding: 20rpx 40rpx;
	font-size: 28rpx;
	min-width: 160rpx;
}

.action-btn.secondary {
	background: transparent;
}

.action-btn:active {
	background: rgba(255, 255, 255, 0.3);
}
</style>