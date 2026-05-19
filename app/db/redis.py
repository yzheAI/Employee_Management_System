import redis
from app.config.setting import settings


# 创建全局 Redis 客户端实例
redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True,  # 自动把字节转为字符串
)
