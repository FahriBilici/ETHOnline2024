from tempfile import NamedTemporaryFile

from fastapi import APIRouter, Depends
from lighthouseweb3 import Lighthouse

from api.data.ipfs_data import IpfsSaveRequest
from utils.constants.environment_keys import EnvironmentKeys
from utils.environment.environment_manager import EnvironmentManager, get_environment_manager

router = APIRouter(tags=["IPFS"], prefix="/ipfs")


@router.post("/save", response_model=str)
async def save(
        ipfs_save_request: IpfsSaveRequest,
        env_manager: EnvironmentManager = Depends(get_environment_manager),
):
    lh = Lighthouse(token=env_manager.get_key(EnvironmentKeys.LIGHTHOUSE_KEY.value))
    with NamedTemporaryFile(delete=True, mode='w') as temp_file:
        temp_file.write(ipfs_save_request.message)
        temp_file_path = temp_file.name
        upload_res = lh.upload(temp_file_path)
        return upload_res["data"]["Hash"]


@router.get("/url/{cid}", response_model=str)
async def get_url(
        cid: str
):
    return f"https://chatui.dogukangun.de/chat/{cid}"
