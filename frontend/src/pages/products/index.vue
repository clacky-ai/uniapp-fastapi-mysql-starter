<template>
  <view class="about-page">
    <view class="header">
      <view class="hero-section">
        <view class="logo">🚀</view>
        <text class="app-name">FastAPI + UniApp</text>
        <text class="app-subtitle">全栈开发示例项目</text>
      </view>
    </view>
    
    <view class="content">
      <view class="section">
        <text class="section-title">项目介绍</text>
        <text class="section-text">
          这是一个基于 FastAPI 和 UniApp 构建的全栈应用示例，展示了现代Web开发技术栈的集成应用。
        </text>
      </view>
      
      <view class="tech-stack">
        <text class="section-title">技术栈</text>
        
        <view class="tech-category">
          <text class="tech-category-title">后端技术</text>
          <view class="tech-tags">
            <view class="tech-tag">FastAPI</view>
            <view class="tech-tag">Python 3.12</view>
            <view class="tech-tag">SQLAlchemy</view>
            <view class="tech-tag">MySQL 8.0</view>
            <view class="tech-tag">Uvicorn</view>
          </view>
        </view>
        
        <view class="tech-category">
          <text class="tech-category-title">前端技术</text>
          <view class="tech-tags">
            <view class="tech-tag">UniApp</view>
            <view class="tech-tag">Vue 3</view>
            <view class="tech-tag">TypeScript</view>
            <view class="tech-tag">Vite</view>
          </view>
        </view>
      </view>
      
      <view class="features">
        <text class="section-title">主要功能</text>
        <view class="feature-list">
          <view class="feature-item">
            <view class="feature-icon">📊</view>
            <view class="feature-content">
              <text class="feature-name">实时数据展示</text>
              <text class="feature-desc">通过API获取并展示后台数据统计</text>
            </view>
          </view>
          
          <view class="feature-item">
            <view class="feature-icon">🔗</view>
            <view class="feature-content">
              <text class="feature-name">前后端分离</text>
              <text class="feature-desc">RESTful API设计，前后端完全解耦</text>
            </view>
          </view>
          
          <view class="feature-item">
            <view class="feature-icon">📱</view>
            <view class="feature-content">
              <text class="feature-name">跨平台支持</text>
              <text class="feature-desc">H5、小程序、App多端统一开发</text>
            </view>
          </view>
          
          <view class="feature-item">
            <view class="feature-icon">⚡</view>
            <view class="feature-content">
              <text class="feature-name">高性能架构</text>
              <text class="feature-desc">异步处理、数据库连接池优化</text>
            </view>
          </view>
        </view>
      </view>
      
      <view class="info-cards">
        <view class="info-card">
          <text class="info-title">开发环境</text>
          <text class="info-content">Clacky Cloud IDE</text>
        </view>
        
        <view class="info-card">
          <text class="info-title">部署方式</text>
          <text class="info-content">Docker 容器化</text>
        </view>
        
        <view class="info-card">
          <text class="info-title">版本信息</text>
          <text class="info-content">v1.0.0</text>
        </view>
      </view>
    </view>
    
    <view class="footer">
      <button class="back-btn" @click="goBack">返回首页</button>
      <text class="copyright">© 2024 FastAPI + UniApp Demo</text>
    </view>
  </view>
</template>

<script setup lang="ts">
const goBack = () => {
  uni.navigateBack()
}
</script>

<style scoped>
.about-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 80rpx 40rpx 60rpx;
  text-align: center;
}

.hero-section {
  color: white;
}

.logo {
  font-size: 120rpx;
  margin-bottom: 30rpx;
}

.app-name {
  display: block;
  font-size: 48rpx;
  font-weight: bold;
  margin-bottom: 20rpx;
}

.app-subtitle {
  display: block;
  font-size: 28rpx;
  opacity: 0.9;
}

.content {
  padding: 40rpx;
}

.section {
  margin-bottom: 50rpx;
}

.section-title {
  display: block;
  font-size: 36rpx;
  font-weight: bold;
  color: #333;
  margin-bottom: 30rpx;
}

.section-text {
  display: block;
  font-size: 28rpx;
  line-height: 1.6;
  color: #666;
}

.tech-stack {
  margin-bottom: 50rpx;
}

.tech-category {
  margin-bottom: 40rpx;
}

.tech-category-title {
  display: block;
  font-size: 30rpx;
  font-weight: 600;
  color: #555;
  margin-bottom: 20rpx;
}

.tech-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 15rpx;
}

.tech-tag {
  background: #667eea;
  color: white;
  padding: 12rpx 24rpx;
  border-radius: 25rpx;
  font-size: 24rpx;
  font-weight: 500;
}

.features {
  margin-bottom: 50rpx;
}

.feature-list {
  display: flex;
  flex-direction: column;
  gap: 30rpx;
}

.feature-item {
  display: flex;
  align-items: flex-start;
  background: white;
  padding: 30rpx;
  border-radius: 15rpx;
  box-shadow: 0 4rpx 20rpx rgba(0, 0, 0, 0.08);
}

.feature-icon {
  font-size: 50rpx;
  margin-right: 25rpx;
  margin-top: 5rpx;
}

.feature-content {
  flex: 1;
}

.feature-name {
  display: block;
  font-size: 32rpx;
  font-weight: 600;
  color: #333;
  margin-bottom: 10rpx;
}

.feature-desc {
  display: block;
  font-size: 26rpx;
  color: #666;
  line-height: 1.4;
}

.info-cards {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 20rpx;
  margin-bottom: 50rpx;
}

.info-card {
  background: white;
  padding: 30rpx 20rpx;
  border-radius: 12rpx;
  text-align: center;
  box-shadow: 0 4rpx 20rpx rgba(0, 0, 0, 0.08);
}

.info-title {
  display: block;
  font-size: 24rpx;
  color: #999;
  margin-bottom: 10rpx;
}

.info-content {
  display: block;
  font-size: 28rpx;
  font-weight: 600;
  color: #333;
}

.footer {
  padding: 40rpx;
  text-align: center;
}

.back-btn {
  background: #667eea;
  color: white;
  border: none;
  border-radius: 25rpx;
  padding: 25rpx 50rpx;
  font-size: 30rpx;
  font-weight: 500;
  margin-bottom: 30rpx;
}

.copyright {
  display: block;
  font-size: 24rpx;
  color: #999;
}
</style>