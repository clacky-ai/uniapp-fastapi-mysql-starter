<template>
	<view class="debug-container">
		<view class="debug-header">
			<text class="debug-title">API连接调试</text>
		</view>
		
		<view class="debug-info">
			<view class="info-item">
				<text class="info-label">当前域名:</text>
				<text class="info-value">{{ currentHost }}</text>
			</view>
			<view class="info-item">
				<text class="info-label">API基础URL:</text>
				<text class="info-value">{{ apiBaseUrl }}</text>
			</view>
			<view class="info-item">
				<text class="info-label">完整API地址:</text>
				<text class="info-value">{{ fullApiUrl }}</text>
			</view>
		</view>
		
		<view class="debug-actions">
			<button class="debug-btn" @click="testConnection">测试连接</button>
		</view>
		
		<view class="debug-result">
			<text class="result-title">测试结果:</text>
			<text class="result-text" :class="{ success: testSuccess, error: !testSuccess }">
				{{ testResult }}
			</text>
		</view>
	</view>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const currentHost = ref('')
const apiBaseUrl = ref('')
const fullApiUrl = ref('')
const testResult = ref('尚未测试')
const testSuccess = ref(false)

const initDebugInfo = () => {
	if (typeof window !== 'undefined' && window.location) {
		currentHost.value = window.location.host
		
		// 复制request.ts中的逻辑
		const { protocol, hostname, port } = window.location
		
		if (hostname.includes('clackypaas.com')) {
			apiBaseUrl.value = '(使用相对路径/代理)'
			fullApiUrl.value = '/api/v1/stats/dashboard'
		} else if (hostname === 'localhost' || hostname === '127.0.0.1') {
			apiBaseUrl.value = '(使用代理)'
			fullApiUrl.value = '/api/v1/stats/dashboard'
		} else {
			apiBaseUrl.value = 'http://localhost:8000'
			fullApiUrl.value = 'http://localhost:8000/api/v1/stats/dashboard'
		}
	} else {
		currentHost.value = '无法获取（非浏览器环境）'
		apiBaseUrl.value = 'localhost:8000'
		fullApiUrl.value = 'http://localhost:8000/api/v1/stats/dashboard'
	}
}

const testConnection = async () => {
	testResult.value = '正在测试...'
	testSuccess.value = false
	
	try {
		const response = await uni.request({
			url: fullApiUrl.value,
			method: 'GET',
			timeout: 5000
		})
		
		if (response.statusCode === 200) {
			testResult.value = `连接成功! 数据: ${JSON.stringify(response.data)}`
			testSuccess.value = true
		} else {
			testResult.value = `连接失败: HTTP ${response.statusCode}`
			testSuccess.value = false
		}
	} catch (error: any) {
		testResult.value = `连接错误: ${error.message || '未知错误'}`
		testSuccess.value = false
	}
}

onMounted(() => {
	initDebugInfo()
})
</script>

<style>
.debug-container {
	padding: 40rpx;
	background: #f5f5f5;
	min-height: 100vh;
}

.debug-header {
	text-align: center;
	margin-bottom: 60rpx;
}

.debug-title {
	font-size: 42rpx;
	font-weight: bold;
	color: #333;
}

.debug-info {
	background: white;
	border-radius: 20rpx;
	padding: 40rpx;
	margin-bottom: 40rpx;
}

.info-item {
	display: flex;
	margin-bottom: 30rpx;
	align-items: flex-start;
}

.info-label {
	font-weight: bold;
	color: #666;
	width: 200rpx;
	flex-shrink: 0;
}

.info-value {
	color: #333;
	flex: 1;
	word-break: break-all;
}

.debug-actions {
	text-align: center;
	margin-bottom: 40rpx;
}

.debug-btn {
	background: #007aff;
	color: white;
	border: none;
	border-radius: 50rpx;
	padding: 20rpx 60rpx;
	font-size: 32rpx;
}

.debug-result {
	background: white;
	border-radius: 20rpx;
	padding: 40rpx;
}

.result-title {
	display: block;
	font-weight: bold;
	color: #333;
	margin-bottom: 20rpx;
}

.result-text {
	display: block;
	word-break: break-all;
	line-height: 1.6;
}

.result-text.success {
	color: #00b894;
}

.result-text.error {
	color: #e74c3c;
}
</style>