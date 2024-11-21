from fastapi import APIRouter

from schemas.category import Category

router = APIRouter()


@router.get("/categories/", response_model=dict)
async def read_categories():
    """カテゴリ一覧を表示するためのエンドポイント"""
    return {"message": "カテゴリ一覧を表示", "categories": []}


@router.post("/categories/", response_model=dict)
async def create_category(category: Category):
    """カテゴリを登録するためのエンドポイント"""
    return {"message": "カテゴリを作成しました", "category": category}


@router.put("/categories/{category_id}", response_model=dict)
async def update_category(category_id: int, category: Category):
    """カテゴリを更新するためのエンドポイント"""
    return {"message": "カテゴリを更新しました",
            "category_id": category_id, "category": category}


@router.delete("/categories/{category_id}", response_model=dict)
async def delete_category(category_id: int):
    """カテゴリを削除するためのエンドポイント"""
    return {"message": "カテゴリを削除しました", "category_id": category_id}