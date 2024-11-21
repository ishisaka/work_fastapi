from pydantic import BaseModel


class Item(BaseModel):
    """アイテムを表すクラス。

    アイテムのID、名前、カテゴリIDを含む。特定の商品の情報を管理
    するために使用される。

    Attributes:
        item_id (int): アイテムのID。
        item_name (str): アイテムの名前。
        category_id (int): カテゴリのID。
    """

    item_id: int
    item_name: str
    category_id: int
