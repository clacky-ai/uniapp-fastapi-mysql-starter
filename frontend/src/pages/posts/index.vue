<template>
	<view class="container">
		<view class="header">
			<text class="title">博客文章</text>
			<text class="subtitle">浏览所有已发布的文章</text>
		</view>
		
		<view class="loading" v-if="loading">
			<text class="loading-text">正在加载文章...</text>
		</view>
		
		<view class="error" v-else-if="error">
			<text class="error-text">{{ error }}</text>
			<button class="retry-btn" @click="loadPosts">重试</button>
		</view>
		
		<view class="posts-list" v-else>
			<view class="post-card" v-for="post in posts" :key="post.id" @click="navigateToDetail(post.id)">
				<view class="post-header">
					<text class="post-title">{{ post.title }}</text>
					<view class="post-status" v-if="post.is_published">
						<text class="status-badge published">已发布</text>
					</view>
				</view>
				
				<text class="post-content">{{ post.content || '暂无内容' }}</text>
				
				<view class="post-meta">
					<view class="author-info" v-if="post.author">
						<text class="author-name">👤 {{ post.author.full_name || post.author.username }}</text>
					</view>
					<text class="post-date">{{ formatDate(post.created_at) }}</text>
				</view>
			</view>
			
			<view class="empty" v-if="posts.length === 0">
				<text class="empty-text">暂无文章</text>
			</view>
		</view>
		
		<view class="actions">
			<button class="action-btn" @click="loadPosts">刷新列表</button>
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
const posts = ref<Post[]>([])

const loadPosts = async () => {
	loading.value = true
	error.value = ''
	
	try {
		const response = await api.posts.getPublished()
		if (response.success && response.data) {
			posts.value = response.data
		} else {
			error.value = response.error || '文章加载失败'
		}
	} catch (err: any) {
		error.value = err.message || '网络连接失败'
	} finally {
		loading.value = false
	}
}

const navigateToDetail = (postId: number) => {
	uni.navigateTo({
		url: `/pages/posts/detail?id=${postId}`
	})
}

const formatDate = (dateString: string) => {
	const date = new Date(dateString)
	return date.toLocaleDateString('zh-CN', {
		year: 'numeric',
		month: 'short',
		day: 'numeric'
	})
}

onMounted(() => {
	loadPosts()
})
</script>

<style>
.container {
	padding: 40rpx;
	min-height: 100vh;
	background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
}

.header {
	text-align: center;
	margin-bottom: 60rpx;
	padding-top: 60rpx;
}

.title {
	display: block;
	font-size: 48rpx;
	font-weight: bold;
	color: white;
	margin-bottom: 20rpx;
}

.subtitle {
	display: block;
	font-size: 28rpx;
	color: rgba(255, 255, 255, 0.8);
}

.loading {
	text-align: center;
	padding: 100rpx 0;
}

.loading-text {
	color: white;
	font-size: 32rpx;
}

.error {
	text-align: center;
	padding: 100rpx 40rpx;
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

.posts-list {
	margin-bottom: 60rpx;
}

.post-card {
	background: white;
	border-radius: 20rpx;
	padding: 40rpx;
	margin-bottom: 30rpx;
	box-shadow: 0 8rpx 30rpx rgba(0, 0, 0, 0.1);
	transition: transform 0.2s;
}

.post-card:active {
	transform: translateY(4rpx);
}

.post-header {
	display: flex;
	justify-content: space-between;
	align-items: flex-start;
	margin-bottom: 20rpx;
}

.post-title {
	font-size: 36rpx;
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
	padding: 8rpx 16rpx;
	border-radius: 20rpx;
	font-size: 24rpx;
}

.post-content {
	color: #636e72;
	font-size: 30rpx;
	line-height: 1.6;
	margin-bottom: 30rpx;
	display: -webkit-box;
	-webkit-box-orient: vertical;
	-webkit-line-clamp: 3;
	overflow: hidden;
}

.post-meta {
	display: flex;
	justify-content: space-between;
	align-items: center;
	font-size: 26rpx;
	color: #74b9ff;
}

.author-info {
	display: flex;
	align-items: center;
}

.author-name {
	color: #636e72;
}

.post-date {
	color: #b2bec3;
}

.empty {
	text-align: center;
	padding: 100rpx 0;
}

.empty-text {
	color: rgba(255, 255, 255, 0.7);
	font-size: 32rpx;
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

.action-btn:active {
	background: rgba(255, 255, 255, 0.3);
}
</style>