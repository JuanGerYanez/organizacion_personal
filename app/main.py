from fastapi import FastAPI
from usuarios import router_usuarios
from actividad_diaria import router_actividad_diaria

app = FastAPI()

app.include_router(router_usuarios, prefix="/api/v1")
app.include_router(router_actividad_diaria, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
