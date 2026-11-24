# mini-erp

Küçük işletmelerin stok, sipariş ve müşteri kayıtlarını tutabileceği basit bir ERP uygulaması. Python ve FastAPI ile yazıyoruz. Proje üniversitedeki dönem projemiz olarak grupça geliştiriliyor, henüz bitmedi.

İleride doğal dille soru sorup stok bilgisi alabilmeyi de eklemeyi düşünüyoruz (örneğin "kaç kalem kaldı?" gibi).

## Şu an neler çalışıyor

Şimdilik sadece ürün işlemleri var:

- `POST /urunler/` ile yeni ürün eklenir (ad, fiyat, stok adedi)
- `GET /urunler/` ile eklenen ürünler listelenir

Ürünler şimdilik bellekte duruyor, yani uygulamayı kapatınca silinir. Veritabanını sonraki adımda ekleyeceğiz.

## Nasıl çalıştırırım

Önce projeyi bilgisayarına indir:

```
git clone https://github.com/aycgee/mini-erp.git
cd mini-erp
```

Sonra sanal ortam oluşturup aç (Windows PowerShell için):

```
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Gerekli paketleri kur ve uygulamayı başlat:

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Tarayıcıda `http://127.0.0.1:8000/docs` adresini açarsan endpoint'leri orada deneyebilirsin.

## Testler

Sanal ortam açıkken proje klasöründe şunu yaz:

```
python -m pytest
```

## Sırada ne var

Veritabanı bağlantısı, müşteri, tedarikçi, sipariş ve raporlama modülleri, en son da doğal dille sorgulama.

Çalışırken uyduğumuz kurallar (branch isimleri, commit mesajları) için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasına bakabilirsin.