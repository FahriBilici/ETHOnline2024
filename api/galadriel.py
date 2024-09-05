from typing import Dict, Any

from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from chainlink.ai.main import ask_ai, get_response
from chainlink.contract_address import GALADRIEL_CONTRACT
from utils.constants.environment_keys import EnvironmentKeys
from utils.environment.environment_manager import EnvironmentManager, get_environment_manager

router = APIRouter(tags=["Galadriel"], prefix="/galadriel")


@router.get("/feed/ask/{message}", response_model=Dict[Any, Any])
async def ask_galadriel(
        message: str,
        env_manager: EnvironmentManager = Depends(get_environment_manager),
):
    return JSONResponse(content=
    {"Res": ask_ai(
        env_manager.get_key(EnvironmentKeys.GALADRIEL_RPC.value),
        GALADRIEL_CONTRACT,
        message,
        env_manager.get_key(EnvironmentKeys.PRIVATE_KEY.value))
    }
    )


@router.get("/response", response_model=Dict[Any, Any])
async def get_galadriel_answer(
        env_manager: EnvironmentManager = Depends(get_environment_manager),
):
    return JSONResponse(content=
                        {"Res": get_response(env_manager.get_key(EnvironmentKeys.GALADRIEL_RPC.value),
                                             GALADRIEL_CONTRACT)
                         })
