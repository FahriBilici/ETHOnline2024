from typing import Dict, List, Any

from fastapi import APIRouter, Depends

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


@router.get("/chains", response_model=List[Any])
async def get_chains():
    return list(Chains)


@router.get("/risks", response_model=List[Any])
async def get_chains():
    return list(Risk)
