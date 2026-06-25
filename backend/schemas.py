"""Pydantic request/response şemaları — API'nin sözleşmesi.

FastAPI bunları otomatik doğrular ve /docs (Swagger) içinde gösterir.
Kendi endpoint'lerine göre alanları değiştir.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class ProcessRequest(BaseModel):
    # TODO: Kullanıcıdan ne alıyorsun? Alanları tanımla.
    query: str = Field(..., description="İşlenecek girdi (örn. konu, soru, URL)")


class ProcessResponse(BaseModel):
    # TODO: Ne döndürüyorsun?
    result: str = Field(..., description="LLM'in ürettiği sonuç")
    source_url: str | None = Field(None, description="Kaynak URL (varsa)")
