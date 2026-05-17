from sqlalchemy.orm import Query


def apply_filters(query: Query, conditions: list):
    for condition in conditions:
        query = query.filter(condition)

    return query
