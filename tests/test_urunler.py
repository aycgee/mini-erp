from fastapi.testclient import TestClient

from app.main import app
from app.routers import urunler

client = TestClient(app)


def setup_function():
    # Her testten önce ürün listesini boşalt, testler birbirini etkilemesin
    urunler.urunler.clear()


def test_urun_ekle():
    cevap = client.post("/urunler/", json={"ad": "Kalem", "fiyat": 5, "stok_adedi": 10})
    assert cevap.status_code == 201
    assert cevap.json()["id"] == 1
    assert cevap.json()["ad"] == "Kalem"


def test_urunleri_listele():
    client.post("/urunler/", json={"ad": "Kalem", "fiyat": 5, "stok_adedi": 10})
    cevap = client.get("/urunler/")
    assert cevap.status_code == 200
    assert len(cevap.json()) == 1


def test_gecersiz_fiyat_reddedilir():
    cevap = client.post("/urunler/", json={"ad": "Kalem", "fiyat": 0, "stok_adedi": 10})
    assert cevap.status_code == 422