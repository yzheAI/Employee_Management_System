# Factory Management System 

## 项目简介

本项目是一个基于 FastAPI + SQLAlchemy + MySQL 的企业组织管理系统，
采用分层架构设计，实现了员工（Employee）、部门（Department）、公告（Announcement）与用户（User）等模块的统一管理。
系统包含了RBAC权限控制、动态查询构建、软删除机制、统一异常处理与分页排序等工程化设计，具备完整的后端系统架构能力。


项目在开发过程中经历了：

CLI → FastAPI Web API  
JSON → SQLite/MySQL  
单表 CRUD → ORM 关系系统  
简单脚本 → 工程化后端架构


## 技术栈:
- FastAPI
- SQLAlchemy
- MySQL
- JWT 身份认证
- Pydantic
- RESTful API
- Python
- alembic数据库迁移



## 系统架构

API Layer → Service Layer → CRUD Layer → Database

- API层：处理请求与权限控制
- Service层：业务逻辑
- CRUD层：数据库操作封装
- Core层：权限、异常、响应封装


app
├── api            # 接口层
├── core           # 核心配置 / 安全认证
├── crud           # 数据访问层
├── db             # 数据库配置
├── models         # ORM 模型
├── schemas        # Pydantic 数据模型
├── services       # 业务逻辑层
├── utils          # 工具类, 统一 Query Layer


## 功能模块

### User模块
- 用户注册、登录
- JWT认证
- 管理员创建用户

### Employee模块
- 员工增删改查
- 动态查询
- 排序+分页

### Department模块
- 部门增删改查
- 查询部门员工
- 动态查询
- 排序+分页

### Announcement模块
- 公告增删改查
                

## 项目亮点
- 基于FastAPI分层架构设计，实现API、Service、CRUD分离，提高代码可维护性和扩展性
- 基于FastAPI实现RBAC权限控制系统，支持多角色访问
- 封装动态查询系统，可以条件过滤、排序、分页，提高查询能力
- 引入软删除机制，避免操作失误
- 使用JWT进行用户认证和登录鉴权
- 封装统一响应结构，规范接口返回格式
- 引入日志系统，可进行日志记录
- 使用SQLAlchemy ORM完成数据库操作
- 使用Query Builder抽象通用查询逻辑，减少代码重复，提高开发效率
- alembic数据库迁移
- - 使用 Redis 实现 JWT Token 黑名单机制，支持用户主动注销与 Token 失效控制





## 项目启动方式
1. 安装依赖：pip install -r requirements.txt
2. 修改 .env文件
3. 初始化数据库：alembic upgrade head
4. 启动项目：uvicorn app.main:app --reload