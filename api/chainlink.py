from typing import Dict, List, Any

from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from chainlink.contract_address import CHAINS_RPC, CHAINS, Chains, Risk
from chainlink.feed.main import get_price
from utils.environment.environment_manager import EnvironmentManager, get_environment_manager

router = APIRouter(tags=["Chainlink"], prefix="/chainlink")


@router.get("/feed/{chain_id}/{risk}", response_model=Dict[str, Dict])
async def get_data_feed(
        chain_id: int,
        risk: str,
        env_manager: EnvironmentManager = Depends(get_environment_manager),
):
    return get_price(env_manager.get_key(CHAINS_RPC[chain_id]), CHAINS[chain_id][risk])


@router.get("/chains", response_model=Dict[str, int])
async def get_chains():
    res = {
        "ETH": Chains.ETH.value,
        "ARBITRUM": Chains.ARBITRUM.value
    }
    return res


@router.get("/risks", response_model=Dict[str, str])
async def get_chains():
    res = {
        "LOW": Risk.LOW.value,
        "MEDIUM": Risk.MEDIUM.value,
        "HIGH": Risk.HIGH.value
    }
    return res
