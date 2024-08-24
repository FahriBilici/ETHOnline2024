from pydantic import BaseModel


class ChainlinkDatafeedRequest(BaseModel):
    chain_id: str
