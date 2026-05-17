from sqlalchemy.orm import Query


def base_query(db, model):
    return db.query(model).filter(model.is_deleted == False)


def apply_filters(query: Query, conditions: list):
    for condition in conditions:
        query = query.filter(condition)

    return query
