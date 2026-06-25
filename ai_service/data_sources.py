"""Veri kaynağı katmanı — Single Responsibility: sadece dış veriyi çeker.

Bu modül HTTP/LLM bilmez. Bir sorgu alır, ham içeriği ve kaynak URL'ini
döndürür. Kendi use-case'ine göre DOLDUR.

Ücretsiz / API key gerektirmeyen örnek kaynaklar:
  - Wikipedia        → `wikipedia-api` (sadece User-Agent ister)
  - HackerNews       → REST API (httpx ile GET)
  - arXiv / RSS      → `feedparser`
  - Açık veri portal → httpx ile GET
"""

from __future__ import annotations


def fetch_source(query: str) -> tuple[str, str]:
    """Sorguya karşılık ham metin içeriğini ve kaynak URL'ini döndürür.

    Returns:
        (content, source_url)

    Raises:
        ValueError: İçerik bulunamazsa. (routes.py bunu yakalayıp 404'e çevirir.)

    TODO: Kendi veri kaynağını burada çek.

    Örnek (Wikipedia — requirements.txt'e `wikipedia-api` ekle):

        import wikipediaapi

        _wiki = wikipediaapi.Wikipedia(
            user_agent="MyApp (mail@example.com)",
            language="tr",
        )

        page = _wiki.page(query)
        if not page.exists():
            raise ValueError("İçerik bulunamadı")
        return page.text, page.fullurl
    """
    raise NotImplementedError(
        "ai_service/data_sources.py → fetch_source henüz yazılmadı"
    )
