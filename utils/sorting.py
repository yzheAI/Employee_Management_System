def apply_sort(query, order_column, order_by, order, model):
    column = order_column.get(order_by, model.id)
    if order == 'desc':
        query = query.order_by(column.desc())
    else:
        query = query.order_by(column.asc())
    return query
