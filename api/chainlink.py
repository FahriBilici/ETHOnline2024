from typing import Dict, List

from fastapi import APIRouter, Depends

from chainlink.contract_address import CHAINS_RPC, CHAINS
from chainlink.feed.main import get_price
from utils.environment.environment_manager import EnvironmentManager, get_environment_manager

router = APIRouter(tags=["Chainlink"], prefix="/chainlink")


@router.get("/feed/{chain_id}", response_model=Dict[str,Dict[str,int]])
async def get_data_feed(
        chain_id: int,
        env_manager: EnvironmentManager = Depends(get_environment_manager),
):
    return get_price(env_manager.get_key(CHAINS_RPC[chain_id]), CHAINS[chain_id])
