app/
├── api/                # 路由接口层
│   ├── student_api.py
│   └── user_api.py
│
├── config/             # 配置层
│   ├── jwt.py
│   ├── logger.py
│   └── setting.py
│
├── core/               # 核心功能层
│   ├── response.py
│   └── security.py
│
├── db/                 # 数据库操作层
│   ├── crud.py
│   └── session.py
│
├── models/             # ORM数据库模型
│   ├── student.py
│   └── user.py
│
├── schemas/            # Pydantic数据校验模型
│   ├── response_schema.py
│   ├── student_schema.py
│   └── user_schema.py
│
├── logs/               # 日志文件目录
│
└── main.py             # 项目启动入口

路由接口层：
    定义接口路由，接受前端传来的请求
    进行参数校验（Field），调用业务逻辑（crud）
    返回统一响应结果（如：ResponseModel[StudentResponse]）

    student_api.py:
        使用FastAPI管理路由
        使用Depends依赖注入
        权限控制（admin,user）
        response_model自动响应校验
    user_api.py:
        用户登录（检验密码，生成token，返回access_token）

配置层：
    管理环境变量
    配置JWT和日志

    setting.py:
        读取.env配置文件（load_dotenv()）
        配置数据库（DB_HOST...）
    jwt.py:
        生成、解析token
        控制有效时间
    logger.py:
        控制台日志（StreamHandler()）
        日志文件（RotatingFileHandler）自动切割
        错误日志error.log

核心功能层：
    实现安全认证、统一返回格式

    response.py:
        统一封装接口返回格式
        success()、error()
    security.py:
        系统安全认证
        JWT身份解析
        登录token生成

数据库操作层：
    
    session.py:
        创建数据库引擎（create_engine()）
        创建独立数据库会话
        get_db提供会话释放资源
    crud.py:
        增删改查操作逻辑
        bcrypt密码加密存储

ORM模型层：
    定义数据库表结构

    student.py:
        定义student表
    user.py:
        定义user表

数据校验层：
    基于pydantic实现

    student_schema.py:
        学生增加、更新、返回格式
    user_schema.py:
        用户注册、登录、token格式
    response_schema.py:
        定义统一响应模型


项目整体运行流程：
    1.用户登录
        输入用户名+密码
        ↓
        验证密码
        ↓
        生成JWT Token
        ↓
        返回Token
    2.用户访问接口
        security解析Token
        ↓
        获取用户身份
        ↓
        判断权限
        ↓
        允许访问接口
    3.数据库操作
        接口层
        ↓
        crud业务层
        ↓
        SQLAIchemy ORM
        ↓
        MySQL数据库
    


    
