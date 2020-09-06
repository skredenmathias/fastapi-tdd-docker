from typing import Union, List

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


# Utility function that creates new summaries
# 1. Takes payload object
# 2. Creates a TextSummary instance
# 3. Returns the generated ID
async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="dummy summary",)
    await summary.save()
    return summary.id


# Union[dict, None] is equivalent to Optional[dict]
# the values method creates a ValuesQuery object.
# Then, if the TextSummary exists, we return it as a dict.
async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary[0]
    return None


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries


async def delete(id: int) -> int:
    summary = await TextSummary.filter(id=id).first().delete()
    return summary


async def put(id: int, payload: SummaryPayloadSchema) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).update(url=payload.url, summary=payload.summary)
    if summary:
        updated_summary = await TextSummary.filter(id=id).first().values()
        return updated_summary[0]
    return None
