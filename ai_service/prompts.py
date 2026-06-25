"""Prompt template'leri — iş mantığının 'modele ne sorduğu' burada durur.

Template'leri saf string olarak tut, routes.py içinde `.format()` ile doldur.
Use-case'ine göre yaz.
"""

# TODO: Ana prompt'unu yaz. {content} ve ihtiyacın olan diğer değişkenleri
# .format() ile dolduracaksın.
MAIN_PROMPT = (
    "Aşağıdaki içeriği kullanarak istenen görevi yerine getir.\n\n"
    "İçerik:\n{content}\n\n"
    "Görev: {task}"
)

# İpucu — Grounding (sadece verilen metne dayan):
# Modelin uydurmaması için net talimat ver, örn:
#   "Cevap içerikte yoksa 'Bu bilgi metinde yer almıyor.' de."
