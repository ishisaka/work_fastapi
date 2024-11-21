from pydantic import BaseModel


class Category(BaseModel):
    """カテゴリのスキーマ

    Attributes:
        category_id(int): カテゴリID
        category_name(str): カテゴリ名
    """

    category_id: int
    category_name: str
