from fastapi import FastAPI

import web.auth as auth
import web.product as product
import web.user as user

app = FastAPI(debug=True)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(product.router)

@app.get('/hello')
def say_hello():
    return "Hello!"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)
