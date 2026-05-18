# Factory Management System (CLI → FastAPI + MySQL + JWT)

## 项目简介

本项目是一个基于 FastAPI + SQLAlchemy + MySQL 的企业组织管理系统，
采用分层架构设计，实现了员工（Employee）、部门（Department）、公告（Announcement）与用户（User）等模块的统一管理。

项目在开发过程中经历了：

CLI → FastAPI Web API  
JSON → SQLite/MySQL  
单表 CRUD → ORM 关系系统  
简单脚本 → 工程化后端架构

具备较好的扩展性与中小型后端系统开发实践价值。

技术栈:
- FastAPI
- SQLAlchemy
- MySQL
- JWT 身份认证
- Pydantic
- RESTful API
- Python

---

## 功能

系统支持：

- JWT 身份认证
- RBAC 权限控制
- RESTful API
- 分页与模糊查询
- ORM 关系映射
- 统一响应结构
- 模块化 CRUD 设计
- 全局异常处理

app
├── api            # 接口层
├── core           # 核心配置 / 安全认证
├── crud           # 数据访问层
├── db             # 数据库配置
├── models         # ORM 模型
├── schemas        # Pydantic 数据模型
├── services       # 业务逻辑层
├── utils          # 工具类, 统一 Query Layer

                