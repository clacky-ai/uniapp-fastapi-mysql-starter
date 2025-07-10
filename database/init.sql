-- 创建数据库（如果不存在）
CREATE DATABASE IF NOT EXISTS blog_demo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 使用数据库
USE blog_demo;

-- 创建用户表
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_username (username),
    INDEX idx_email (email)
);

-- 创建文章表
CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT,
    author_id INT NOT NULL,
    is_published BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_title (title),
    INDEX idx_author_id (author_id),
    INDEX idx_published (is_published)
);

-- 插入示例用户数据
INSERT INTO users (username, email, password_hash, full_name) VALUES 
('admin', 'admin@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewYLhN2vhh8vHG5.', '管理员'),
('alice', 'alice@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewYLhN2vhh8vHG5.', 'Alice Smith'),
('bob', 'bob@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewYLhN2vhh8vHG5.', 'Bob Johnson'),
('charlie', 'charlie@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewYLhN2vhh8vHG5.', 'Charlie Brown');

-- 插入示例文章数据
INSERT INTO posts (title, content, author_id, is_published) VALUES 
('欢迎来到我的博客', '这是我的第一篇博客文章，欢迎大家阅读！', 1, TRUE),
('关于 FastAPI 的学习笔记', 'FastAPI 是一个现代、快速的 Web 框架，用于构建 APIs...', 2, TRUE),
('数据库设计最佳实践', '在设计数据库时，我们需要考虑以下几个方面...', 2, FALSE),
('Python 编程技巧分享', '今天分享一些 Python 编程的实用技巧...', 3, TRUE),
('Web 开发入门指南', '对于刚开始学习 Web 开发的朋友们...', 4, FALSE);