# Gravar como 'hello_fastapi.py'
# Executar:
#       $ uvicorn hello_fastapi:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"2xitem_id": item_id * 2, "q": q}


# Por omissão FastAPI gera JSON
