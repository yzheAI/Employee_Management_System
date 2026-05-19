from app.db.redis import redis_client


def add_token_to_blacklist(token: str):
    redis_client.set(f"blacklist:token:{token}", "1")


def is_token_blacklisted(token: str) -> bool:
    return redis_client.get(f"blacklist:token:{token}") is not None

