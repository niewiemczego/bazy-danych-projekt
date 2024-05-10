from pydantic import BaseModel

class SneakerBase(BaseModel):
    name: str
    brand_id:
    colors: list[str]
    price: float

class SneakerCreate(SneakerBase)