from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sample FastAPI Project")


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    in_stock: bool = True


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "FastAPI project is running"}


@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict[str, object]:
    return {"item_id": item_id, "message": "Sample GET endpoint"}


@app.post("/items")
def create_item(item: Item) -> dict[str, object]:
    return {
        "message": "Sample POST endpoint",
        "item": item.model_dump(),
    }
