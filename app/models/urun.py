from pydantic import BaseModel, Field


class UrunOlustur(BaseModel):
    """Yeni ürün eklerken kullanıcıdan alınan bilgiler."""
    ad: str = Field(min_length=1)
    fiyat: float = Field(gt=0)
    stok_adedi: int = Field(default=0, ge=0)


class Urun(UrunOlustur):
    """Sistemde kayıtlı ürün: eklenen bilgilere ek olarak bir id'si var."""
    id: int