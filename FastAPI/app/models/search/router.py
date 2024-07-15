import asyncpg
from fastapi import APIRouter, Depends
import json

from FastAPI.app.database.db import get_db
from FastAPI.app.models.search.schemas import SearchRequest

router_search = APIRouter(
    prefix="/search",
)


def to_title_case(s):
    return s[0].upper() + s[1:].lower() if s else s


@router_search.post("/part/")
async def search_part(request: SearchRequest,
                      conn: asyncpg.Connection = Depends(get_db)):
    query = """
    SELECT p.*, m.name as mark_name, m.producer_country_name, mdl.name as model_name
    FROM search_parts_part p
    JOIN search_parts_mark m ON p.mark_id = m.id
    JOIN search_parts_model mdl ON p.model_id = mdl.id
    WHERE 1=1
    """

    values = []
    params_counter = 1

    if request.mark_name:
        mark_name = to_title_case(request.mark_name)
        query += f" AND m.name = ${params_counter}"
        values.append(mark_name)
        params_counter += 1

    if request.part_name:
        part_name = to_title_case(request.part_name)
        query += f" AND p.name = ${params_counter}"
        values.append(part_name)
        params_counter += 1

    if request.mark_list:
        mark_list_placeholder = ", ".join(map(str, request.mark_list))
        query += f" AND p.mark_id IN ({mark_list_placeholder})"

    if request.params:
        if request.params.color:
            color = to_title_case(request.params.color)
            query += f" AND p.json_data->>'color' = ${params_counter}"
            values.append(color)
            params_counter += 1
        if request.params.is_new_part is not None:
            query += f" AND p.json_data->>'is_new_part' = ${params_counter}"
            values.append(json.dumps(request.params.is_new_part))
            params_counter += 1

    if request.price_gte is not None:
        query += f" AND p.price >= ${params_counter}"
        values.append(request.price_gte)
        params_counter += 1

    if request.price_lte is not None:
        query += f" AND p.price <= ${params_counter}"
        values.append(request.price_lte)
        params_counter += 1

    limit = 10
    offset = (request.page - 1) * limit
    query += f" LIMIT ${params_counter} OFFSET ${params_counter + 1}"
    values.extend([limit, offset])

    rows = await conn.fetch(query, *values)

    count_query = f"SELECT COUNT(*) FROM ({query}) subquery"
    sum_query = f"SELECT SUM(price) FROM ({query}) subquery"
    total_count = await conn.fetchval(count_query, *values)
    total_sum = await conn.fetchval(sum_query, *values) or 0

    response = []
    for row in rows:
        response.append({
            "mark": {
                "id": row["mark_id"],
                "name": row["mark_name"],
                "producer_country_name": row["producer_country_name"]
            },
            "model": {
                "id": row["model_id"],
                "name": row["model_name"]
            },
            "name": row["name"],
            "json_data": json.loads(row["json_data"]),
            "price": row["price"]
        })

    return {
        "response": response,
        "count": total_count,
        "summ": total_sum
    }