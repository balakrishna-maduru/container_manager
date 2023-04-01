"""
    Continer manager is used to manage deployments in k8s
"""
from fastapi import FastAPI
from routers import container_api


app = FastAPI()

app.include_router(container_api.router)
@app.get("/")
async def read_root():
    return {
        "project_name": "Container_manager",
        "owner":"Balakrishna Maduru",
        "description": "Continer manager is used to manage deployments in k8s"
    }