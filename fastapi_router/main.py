from fastapi import FastAPI
from routers.categoriea import router as category_router
from routers.items import router as item_router

app = FastAPI()

# カテゴリ用ルーターをアプリケーションに追加
app.include_router(category_router)

# 商品用ルーターをアプリケーションに追加
app.include_router(item_router)
