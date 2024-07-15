from pydantic import BaseModel


class Params(BaseModel):
    color: str = None
    is_new_part: bool = None


class SearchRequest(BaseModel):
    mark_name: str = None
    part_name: str = None
    params: Params = None
    mark_list: list[int] = None
    price_gte: float = None
    price_lte: float = None
    page: int = 1