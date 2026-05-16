def paginate(query, page, size, schema):
    total = query.count()
    items = (
        query.offset((page - 1) * size).limit(size).all()
    )

    return {
        "page": page,
        "size": size,
        "total": total,
        "items": [schema.model_validate(i) for i in items],
    }
