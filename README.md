# Student Management System (CLI → FastAPI + MySQL + JWT)

# 项目简介
这是一个基于 Python 实现的学生管理系统，最初为命令行（CLI）版本，后逐步升级为基于 FastAPI 的 Web 应用，并完成数据存储层从 JSON 文件到 MySQL 数据库的重构。

项目采用分层架构设计，支持学生信息的增删改查，引入JWT身份认证与基础权限控制，并具备良好的可扩展性与工程化结构。

系统特点：
- 支持 **CLI → Web API 演进**
- 数据存储由 **JSON 重构为 SQLite + SQLAlchemy ORM**
- 分离 **业务模型（Entity）与 API 模型（Pydantic Schema）**
- 项目采用分层架构设计（API / Service / DB / Models / Core），实现了学生信息管理、用户认证与基础权限控制，并具备较好的可扩展性与工程化设计能力。
- 支持日志记录与错误追踪
- 实现 JWT 用户认证与基础 RBAC 权限控制
- 扩展多业务模块（Student/User/Announcement）

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

---

## 项目结构

```text
Student_Manager/
├── app/
│   ├── api/                 # API路由层
│   │   ├── student_api.py
│   │   ├── user_api.py
│   │   └── announce_api.py
│   │
│   ├── config/              # 配置层
│   │   ├── jwt.py
│   │   └── setting.py
│   │
│   ├── core/                # 核心工具层
│   │   ├── logger.py
│   │   ├── response.py
│   │   └── security.py
│   │
│   ├── db/                  # 数据库层
│   │   ├── crud.py
│   │   └── session.py
│   │
│   ├── models/              # ORM模型层
│   │   ├── student.py
│   │   ├── user.py
│   │   └── announcement.py
│   │
│   ├── schemas/             # Pydantic模型层
│   │   ├── student_schema.py
│   │   ├── user_schema.py
│   │   ├── response_schema.py
│   │   └── announcement_schema.py
│   │
│   ├── service/             # 业务逻辑层（预留扩展）
│   └── .env
│
├── logs/
├── main.py
├── README.md                                    