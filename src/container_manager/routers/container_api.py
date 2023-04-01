from container_operation.deploy import ContainerDeploy
from container_operation.restart import ContainerRestart
from container_operation.delete import ContainerDelete
from fastapi import APIRouter


router = APIRouter(
    prefix="/container_api",
    tags=["container_api"],
    responses={404:{"description": "Not Found"}}
)

@router.post("/deploy/{user}")
async def container_deploy(user:str):
    return ContainerDeploy(user).deploy()

@router.post("/restart/{user}")
async def container_restart(user:str):
    return ContainerRestart(user).restart()

@router.post("/delete/{user}")
async def container_delete(user:str):
    return ContainerDelete(user).delete()