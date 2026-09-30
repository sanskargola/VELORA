from pydantic import BaseModel


class TransactionCreate(BaseModel):
    stock_symbol: str
    transaction_type: str
    quantity: float
    price_per_unit: float


class TransactionOut(BaseModel):
    id: int
    stock_symbol: str
    transaction_type: str
    quantity: float
    price_per_unit: float
    total_amount: float

    class Config:
        from_attributes = True
