from pydantic import BaseModel


class IpfsSaveRequest(BaseModel):
    message: str
