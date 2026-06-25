"""HTTP katmanı — sadece istek/yanıt akışını yönetir (Single Responsibility).

İş mantığı yoktur: veri çekmeyi `data_sources`'a, metin üretmeyi `LLMClient`'a
delege eder. `Depends(get_llm_client)` ile SOYUT LLMClient enjekte edilir —
route somut GeminiClient'ı bilmez (Dependency Inversion).
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

from ai_service.data_sources import fetch_source
from ai_service.llm_client import LLMClient
from ai_service.prompts import MAIN_PROMPT
from backend.dependencies import get_llm_client
from backend.schemas import ProcessRequest, ProcessResponse

router = APIRouter()


@router.post("/process", response_model=ProcessResponse)
async def process(
    req: ProcessRequest,
    llm: LLMClient = Depends(get_llm_client),
) -> ProcessResponse:
    """Örnek endpoint deseni: veri çek → prompt doldur → LLM çağır → döndür.

    TODO: Kendi endpoint(ler)ini bu desene göre yaz. Adımlar:

        1) İçeriği çek (bulunamazsa 404):
           try:
               content, url = fetch_source(req.query)
           except ValueError as e:
               raise HTTPException(status_code=404, detail=str(e))

        2) Prompt'u doldur (içeriği truncate et: content[:6000]):
           prompt = MAIN_PROMPT.format(content=content[:6000], task="...")

        3) LLM'i async çağır:
           result = await llm.generate(prompt)

        4) Response döndür:
           return ProcessResponse(result=result, source_url=url)
    """
    raise HTTPException(
        status_code=501,
        detail="TODO: backend/routes.py → process henüz yazılmadı",
    )
