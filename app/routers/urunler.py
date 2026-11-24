from fastapi import APIRouter

from app.models.urun import Urun, UrunOlustur

router = APIRouter(prefix="/urunler", tags=["Ürünler"])

# Veritabanı gelene kadar ürünleri geçici olarak bellekte tutuyoruz
urunler: list[Urun] = []


@router.post("/", response_model=Urun, status_code=201)
def urun_ekle(yeni: UrunOlustur):
    urun = Urun(id=len(urunler) + 1, **yeni.model_dump())
    urunler.append(urun)
    return urun


@router.get("/", response_model=list[Urun])
def urunleri_listele():
    return urunler