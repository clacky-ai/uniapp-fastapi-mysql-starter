-- 创建数据库（如果不存在）
CREATE DATABASE IF NOT EXISTS user_demo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 使用数据库
USE user_demo;

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



-- 插入示例用户数据 (所有用户密码都是 'secret')
INSERT INTO users (username, email, password_hash, full_name) VALUES 
('admin', 'admin@example.com', '$2b$12$XpPawJNW7JquQRp6G1noN.L7AA0n/DP9C8cl0gT8N/63l3Qf1GNzu', '管理员'),
('alice', 'alice@example.com', '$2b$12$XpPawJNW7JquQRp6G1noN.L7AA0n/DP9C8cl0gT8N/63l3Qf1GNzu', 'Alice Smith'),
('bob', 'bob@example.com', '$2b$12$XpPawJNW7JquQRp6G1noN.L7AA0n/DP9C8cl0gT8N/63l3Qf1GNzu', 'Bob Johnson'),
('charlie', 'charlie@example.com', '$2b$12$XpPawJNW7JquQRp6G1noN.L7AA0n/DP9C8cl0gT8N/63l3Qf1GNzu', 'Charlie Brown');

