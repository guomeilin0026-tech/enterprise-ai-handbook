# 第 12 章：Docker 部署

## 12.1 Docker 是什么

Docker 可以把应用和运行环境打包起来。

你可以理解成：

```text
把项目装进一个标准盒子里，到哪里都能运行
```

## 12.2 镜像和容器

镜像：

```text
应用的打包模板
```

容器：

```text
镜像运行起来后的实例
```

## 12.3 Dockerfile

Dockerfile 描述如何构建镜像。

后端 Dockerfile 通常做：

- 选择 Python 基础镜像
- 复制代码
- 安装依赖
- 暴露端口
- 启动服务

## 12.4 docker-compose

企业 AI 项目通常有多个服务：

- 前端
- 后端
- PostgreSQL
- Qdrant
- Redis
- Nginx

docker-compose 可以一条命令启动多个服务。

## 12.5 环境变量

敏感配置不要写死在代码里。

应该放到 `.env`：

```text
OPENAI_API_KEY=xxx
DATABASE_URL=xxx
JWT_SECRET=xxx
```

GitHub 里只提交 `.env.example`，不要提交真实 `.env`。

## 12.6 Nginx

Nginx 常用于：

- 托管前端静态文件
- 反向代理后端接口
- 配置 HTTPS
- 处理跨域和域名访问

## 本章练习

- [ ] 写出 AI 项目有哪些服务
- [ ] 设计 docker-compose 服务列表
- [ ] 说明为什么不能提交真实 `.env`

