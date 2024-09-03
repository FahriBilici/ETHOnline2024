from fastapi import APIRouter, Depends

from chainlink.ai.main import ask_ai, get_response
from chainlink.contract_address import GALADRIEL_CONTRACT
from utils.constants.environment_keys import EnvironmentKeys
from utils.environment.environment_manager import EnvironmentManager, get_environment_manager

router = APIRouter(tags=["Galadriel"], prefix="/galadriel")


@router.get("/feed/ask/{message}", response_model=str)
async def ask_galadriel(
        message: str,
        env_manager: EnvironmentManager = Depends(get_environment_manager),
):
    return ask_ai(
        env_manager.get_key(EnvironmentKeys.GALADRIEL_RPC.value),
        GALADRIEL_CONTRACT,
        message,
        env_manager.get_key(EnvironmentKeys.PRIVATE_KEY.value)
    )


@router.get("/response", response_model=str)
async def get_galadriel_answer(
        env_manager: EnvironmentManager = Depends(get_environment_manager),
):
    return get_response(env_manager.get_key(EnvironmentKeys.GALADRIEL_RPC.value), GALADRIEL_CONTRACT)
