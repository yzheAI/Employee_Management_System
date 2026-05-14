# Employee & Department Management System (CLI → FastAPI + MySQL + JWT)

## 项目简介

本项目最初为基于 Python CLI 的学生管理系统，后逐步重构为基于 FastAPI + SQLAlchemy 的组织管理系统（Factory Management System）。

系统采用分层架构设计，实现了员工（Employee）与部门（Department）之间的一对多关系管理，并集成 JWT 身份认证、基础 RBAC 权限控制、统一响应结构与模块化 CRUD 设计。

项目在开发过程中经历了：

CLI → FastAPI Web API  
JSON → SQLite/MySQL  
单表 CRUD → ORM 关系系统  
简单脚本 → 工程化后端架构

具备较好的扩展性与中小型后端系统开发实践价值。

---

## 功能

### CLI 版本（早期）
- 添加学生
- 查看所有学生
- 根据学号查找学生
- 修改学生信息
- 删除学生

### FastAPI 版本
- 提供 RESTful API 接口
- 自动生成接口文档（/docs）
- 数据校验（Pydantic）
- 学生信息增删改查（CRUD）
- 分层架构解耦业务逻辑
- 登录注册JWT
- 异常处理 + 统一返回格式
- database url抽离
- 添加employee和department模块

### 权限控制模块
- admin 用户可进行增删改操作
- 普通用户仅可查询数据



### Student 模块
- 学生信息增删改查（CRUD）
- 数据校验与结构化返回

### User 模块
- 用户注册 / 登录
- JWT 身份认证
- 密码加密（bcrypt）
- 权限控制（admin / user）

### Announcement 模块（新增）
- 公告发布
- 公告列表查询
- 单条公告查询
- 公告删除


### Department 模块
- 部门创建 / 查询 / 删除
- 部门唯一性校验
- Employee 一对多关系


### Employee 模块
- 员工创建 / 查询 / 删除
- ForeignKey 外键关联
- Department 归属关系
- RBAC 权限控制

---

## 技术栈
- Python 3
- FastAPI
- SQLAlchemy（ORM）
- MySQL（数据存储）
- Pydantic（数据校验）
- 面向对象编程（OOP）
- 分层架构设计
- JWT
- bcrypt(密码加密)
- SQLAlchemy Relationship
- ForeignKey
- RESTful API

---

## 项目结构

```text
Student_Manager/
├── app/
│
│   ├── api/                            # API 路由层
│   │   ├── student_api.py              # legacy 模块（保留）
│   │   ├── user_api.py
│   │   ├── announcement_api.py
│   │   ├── employee_api.py
│   │   └── department_api.py
│   │
│   ├── config/                         # 配置层
│   │   ├── jwt.py
│   │   └── setting.py
│   │
│   ├── core/                           # 核心功能层
│   │   ├── logger.py
│   │   ├── response.py
│   │   ├── security.py
│   │   └── exception_handler.py
│   │
│   ├── db/                             # 数据库层
│   │   ├── session.py
│   │   │
│   │   └── crud/                       # CRUD 模块化
│   │       ├── student_crud.py
│   │       ├── user_crud.py
│   │       ├── announcement_crud.py
│   │       ├── employee_crud.py
│   │       └── department_crud.py
│   │
│   ├── models/                         # SQLAlchemy ORM 模型
│   │   ├── student.py                  # legacy
│   │   ├── user.py
│   │   ├── announcement.py
│   │   ├── employee.py
│   │   └── department.py
│   │
│   ├── schemas/                        # Pydantic 数据模型
│   │   ├── response_schema.py
│   │   │
│   │   ├── student_schema.py
│   │   ├── user_schema.py
│   │   ├── announcement_schema.py
│   │   ├── employee_schema.py
│   │   └── department_schema.py
│   │
│   ├── services/                       # 业务逻辑层（后期拆分）
│   │   ├── employee_service.py
│   │   ├── department_service.py
│   │   └── auth_service.py
│   │
│   ├── utils/                          # 工具函数层（后期扩展）
│   │   ├── pagination.py
│   │   └── validator.py
│   │
│   └── .env
│
├── logs/                               # 日志文件
│
├── tests/                              # 测试模块（后期）
│   ├── test_employee.py
│   ├── test_department.py
│   └── test_auth.py
│
├── main.py                             # FastAPI 入口
├── requirements.txt
├── README.md
└── .gitignore                         