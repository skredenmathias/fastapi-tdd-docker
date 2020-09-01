from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary

# Utility function that creates new summaries
# 1. Takes payload object
# 2. Creates a TextSummary instance
# 3. Returns the generated ID
async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary='dummy summary',
    )
    await summary.save()
    return summary.id


# @router.post('/', response_model=SummaryPayloadSchema, status_code=201)