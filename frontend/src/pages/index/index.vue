<template>
	<view class="container">
		<view class="header">
			<text class="title">系统数据面板</text>
			<text class="subtitle">实时后台API数据展示</text>
		</view>
		
		<view class="loading" v-if="loading">
			<text class="loading-text">正在加载数据...</text>
		</view>
		
		<view class="error" v-else-if="error">
			<text class="error-text">{{ error }}</text>
			<button class="retry-btn" @click="loadData">重试</button>
		</view>
		
		<view class="stats-grid" v-else>

			
			<view class="stat-card">
				<view class="stat-icon">👥</view>
				<view class="stat-number">{{ stats.total_users }}</view>
				<text class="stat-label">用户总数</text>
			</view>
			
			<view class="stat-card">
				<view class="stat-icon">🔥</view>
				<view class="stat-number">{{ stats.active_users }}</view>
				<text class="stat-label">活跃用户</text>
			</view>
		</view>
		
		<view class="status-card" v-if="!loading && !error">
			<view class="status-indicator" :class="{ active: stats.system_status === 'running' }"></view>
			<text class="status-text">{{ stats.message }}</text>
			<text class="status-time">最后更新: {{ lastUpdate }}</text>
		</view>
		
		<view class="actions">
			<button class="action-btn" @click="loadData">刷新数据</button>

			<button class="action-btn debug" @click="navigateTo('/pages/debug')">调试API</button>
		</view>
		
		<view class="footer">
			<text class="footer-text">API: /api/v1/stats/dashboard (通过代理)</text>
		</view>
	</view>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { api } from '@/utils/request'

interface StatsData {
	total_users: number
	active_users: number
	system_status: string
	message: string
}

const loading = ref(true)
const error = ref('')
const stats = ref<StatsData>({
	total_users: 0,
	active_users: 0,
	system_status: 'unknown',
	message: ''
})
const lastUpdate = ref('')

const loadData = async () => {
	loading.value = true
	error.value = ''
	
	try {
		const response = await api.stats.dashboard()
		if (response.success && response.data) {
			stats.value = response.data
			lastUpdate.value = new Date().toLocaleTimeString()
		} else {
			error.value = response.error || '数据加载失败'
		}
	} catch (err: any) {
		error.value = err.message || '网络连接失败'
	} finally {
		loading.value = false
	}
}

const navigateTo = (url: string) => {
	uni.navigateTo({ url })
}

onMounted(() => {
	loadData()
})
</script>

<style>
.container {
	padding: 40rpx;
	min-height: 100vh;
	background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
	padding: 60rpx 40rpx;
	background: rgba(255, 255, 255, 0.1);
	border-radius: 20rpx;
	margin-bottom: 40rpx;
}

.error-text {
	display: block;
	color: #ff6b6b;
	font-size: 28rpx;
	margin-bottom: 30rpx;
}

.retry-btn {
	background: #ff6b6b;
	color: white;
	border: none;
	border-radius: 10rpx;
	padding: 20rpx 40rpx;
	font-size: 28rpx;
}

.stats-grid {
	display: grid;
	grid-template-columns: 1fr 1fr;
	gap: 30rpx;
	margin-bottom: 40rpx;
}

.stat-card {
	background: white;
	border-radius: 20rpx;
	padding: 40rpx 30rpx;
	text-align: center;
	box-shadow: 0 8rpx 30rpx rgba(0, 0, 0, 0.1);
}

.stat-icon {
	font-size: 50rpx;
	margin-bottom: 20rpx;
}

.stat-number {
	display: block;
	font-size: 48rpx;
	font-weight: bold;
	color: #667eea;
	margin-bottom: 10rpx;
}

.stat-label {
	display: block;
	font-size: 24rpx;
	color: #666;
}

.status-card {
	background: rgba(255, 255, 255, 0.1);
	border-radius: 20rpx;
	padding: 30rpx;
	margin-bottom: 40rpx;
	display: flex;
	flex-direction: column;
	align-items: center;
}

.status-indicator {
	width: 20rpx;
	height: 20rpx;
	border-radius: 50%;
	background: #ccc;
	margin-bottom: 20rpx;
}

.status-indicator.active {
	background: #4ade80;
}

.status-text {
	color: white;
	font-size: 32rpx;
	font-weight: 500;
	margin-bottom: 10rpx;
}

.status-time {
	color: rgba(255, 255, 255, 0.6);
	font-size: 24rpx;
}

.actions {
	display: flex;
	flex-direction: column;
	gap: 20rpx;
	margin-bottom: 40rpx;
}

.action-btn {
	background: white;
	color: #667eea;
	border: none;
	border-radius: 15rpx;
	padding: 30rpx;
	font-size: 28rpx;
	font-weight: 500;
}

.action-btn.secondary {
	background: rgba(255, 255, 255, 0.2);
	color: white;
}

.action-btn.debug {
	background: rgba(255, 107, 107, 0.2);
	border: 2rpx solid rgba(255, 107, 107, 0.3);
	color: white;
}

.footer {
	text-align: center;
	margin-top: auto;
}

.footer-text {
	font-size: 20rpx;
	color: rgba(255, 255, 255, 0.5);
	line-height: 1.4;
}
</style>