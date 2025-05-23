from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    desc: str | None = None


class STask(STaskAdd):
    id: int


class STaskId(BaseModel):
    ok: bool = True
    task_id: int