from fastapi import Cookie, FastAPI, Response, Header
from typing import Optional

app = FastAPI()

#curl localhost:8000/
@app.get("/")
def read_root():
    return {"Hola": "PUTOS"}

#curl localhost:8000/items/42?q=PUTOS
#curl localhost:8000/items/42
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    # otra_funcion_para_item_id(item_id)
    # otra_function_para_q(q) 
    return {"item_id": item_id, "q": q}

#curl localhost:8000/items/ niega el endpoint por que no es mediante post "{"detail":"Method Not Allowed"}"
#curl -X POST localhost:8000/items/ acepta el endpoint retorna "{"item": "our_item"}"
@app.post("/items/", status_code=201)
def post_item():
    return {"item": "our_item"}

#curl --cookie "my_cookie=home_made" localhost:8000/cookie/ -i  retorn la cookie  -i return el data (metadata)
@app.get("/cookie/")
def read_cookie(my_cookie = Cookie(None)):
    return {"my_cookie": my_cookie}

#curl localhost:8000/setcookie/ -i // se setean los valores de la cookie mediante la respúesta (RESPONSE)
@app.get("/setcookie/")
def set_cookie(response: Response):
    response.set_cookie(key="llave",
                        value="valñor")
    return {"message": "The cooki se a creado "}

#curl localhost:8000/headers/ -i solo retorna el header  -i detalle de request
@app.get("/headers/")
def return_header(user_agent = Header(None)):
    return {"User-Agent": user_agent}

#curl localhost:8000/setheader/ -i  se setea el valor de el header -i detalle del request
@app.get("/setheader/")
def set_header(response: Response):
    response.headers["response_header"] = "my_header"
    return {"message": "header set"}