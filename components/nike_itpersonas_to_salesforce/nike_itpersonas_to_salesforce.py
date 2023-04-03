
from typing import Any, Optional
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class Department(BaseModel):
    industry: str
    name: str


class NikeITPersonasToSalesforceIn(BaseModel):
    api_key: str
    department: Department


class NikeITPersonasToSalesforceOut(BaseModel):
    success: bool


class NikeITPersonasToSalesforce(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: NikeITPersonasToSalesforceIn, callbacks: Optional[Any]
    ) -> NikeITPersonasToSalesforceOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        success = results_dict[-1].success
        out = NikeITPersonasToSalesforceOut(success=success)
        return out


load_dotenv()

nike_it_personas_to_salesforce_app = FastAPI()


@nike_it_personas_to_salesforce_app.post("/transform/")
async def transform(
    args: NikeITPersonasToSalesforceIn,
) -> NikeITPersonasToSalesforceOut:
    nike_it_personas_to_salesforce = NikeITPersonasToSalesforce()
    return await nike_it_personas_to_salesforce.transform(args, callbacks=None)
