"""
Python JSON Dosya İşlemleri

Bu dosya Python'da JSON (JavaScript Object Notation) dosyaları ile
çalışmayı kapsamlı olarak ele alır. json modülü kullanımı,
veri okuma/yazma, serialization ve JSON API'leri öğreneceğiz.
"""

import json
import os
from datetime import datetime, date
from decimal import Decimal
import urllib.request
import urllib.parse

# =============================================================================
# 1. JSON NEDİR VE TEMEL KULLANIM
# =============================================================================

print("=== JSON Dosya İşlemleri ===")

"""
JSON (JavaScript Object Notation)
- Hafif veri değişim formatı
- İnsan tarafından okunabilir
- Dil bağımsız (Python, JavaScript, Java, vb.)
- Web API'lerde yaygın kullanım
- Anahtar-değer çiftleri ve diziler içerir

Python - JSON Karşılığı:
- dict → object
- list → array  
- str → string
- int/float → number
- True/False → true/false
- None → null
"""

# Basit Python verisi
python_verisi = {
    "ad": "Ahmet",
    "soyad": "Yılmaz", 
    "yas": 30,
    "evli": True,
    "cocuklar": ["Ali", "Ayşe"],
    "adres": {
        "sehir": "İstanbul",
        "ilce": "Kadıköy",
        "posta_kodu": 34710
    },
    "maas": None
}

print("Python verisi:")
print(python_verisi)

# Python'dan JSON'a dönüştürme (serialization)
json_string = json.dumps(python_verisi, ensure_ascii=False, indent=2)
print("\nJSON string:")
print(json_string)

# =============================================================================
# 2. JSON YAZMA İŞLEMLERİ
# =============================================================================

print("\n=== JSON Yazma İşlemleri ===")

# 2.1 Dosyaya JSON yazma
calisan_bilgileri = {
    "calisanlar": [
        {
            "id": 1,
            "ad": "Ahmet",
            "soyad": "Yılmaz",
            "departman": "IT",
            "maas": 8500,
            "ise_baslama": "2020-01-15",
            "yetenekler": ["Python", "SQL", "Docker"],
            "aktif": True
        },
        {
            "id": 2,
            "ad": "Ayşe",
            "soyad": "Kaya",
            "departman": "İnsan Kaynakları",
            "maas": 7200,
            "ise_baslama": "2019-03-10",
            "yetenekler": ["İletişim", "Organizasyon", "Excel"],
            "aktif": True
        },
        {
            "id": 3,
            "ad": "Mehmet",
            "soyad": "Öz",
            "departman": "Pazarlama",
            "maas": 6800,
            "ise_baslama": "2021-07-01",
            "yetenekler": ["Dijital Pazarlama", "Analytics", "Photoshop"],
            "aktif": False
        }
    ],
    "sirket": {
        "ad": "TechCorp",
        "kurulus_yili": 2015,
        "calisan_sayisi": 150,
        "lokasyon": "İstanbul"
    },
    "olusturma_tarihi": datetime.now().isoformat()
}

# JSON dosyasına yaz
with open("calisanlar.json", "w", encoding="utf-8") as dosya:
    json.dump(calisan_bilgileri, dosya, ensure_ascii=False, indent=2)

print("✅ Çalışan bilgileri JSON dosyasına yazıldı")

# 2.2 Farklı formatlarla yazma
# Kompakt format (boşluk yok)
with open("calisanlar_kompakt.json", "w", encoding="utf-8") as dosya:
    json.dump(calisan_bilgileri, dosya, ensure_ascii=False, separators=(',', ':'))

# Sıralı anahtarlar
with open("calisanlar_sirali.json", "w", encoding="utf-8") as dosya:
    json.dump(calisan_bilgileri, dosya, ensure_ascii=False, indent=2, sort_keys=True)

print("✅ Farklı formatlarda JSON dosyaları oluşturuldu")

# =============================================================================
# 3. JSON OKUMA İŞLEMLERİ
# =============================================================================

print("\n=== JSON Okuma İşlemleri ===")

# 3.1 Dosyadan JSON okuma
with open("calisanlar.json", "r", encoding="utf-8") as dosya:
    okunan_veri = json.load(dosya)

print("JSON dosyasından okunan veri:")
print(f"Şirket: {okunan_veri['sirket']['ad']}")
print(f"Çalışan sayısı: {len(okunan_veri['calisanlar'])}")

# 3.2 Belirli verilere erişim
print("\nÇalışan detayları:")
for calisan in okunan_veri['calisanlar']:
    durum = "Aktif" if calisan['aktif'] else "Pasif"
    print(f"  {calisan['ad']} {calisan['soyad']} - {calisan['departman']} ({durum})")
    print(f"    Yetenekler: {', '.join(calisan['yetenekler'])}")

# 3.3 JSON string'den veri okuma
json_string = '{"isim": "Python", "versiyon": 3.9, "ozellikler": ["OOP", "Dinamik", "Yorumlamalı"]}'
veri = json.loads(json_string)
print(f"\nJSON string'den: {veri}")

# =============================================================================
# 4. JSON VERİ MANİPÜLASYONU
# =============================================================================

print("\n=== JSON Veri Manipülasyonu ===")

def json_filtrele(json_dosya, filtre_fonksiyonu):
    """JSON dosyasındaki çalışanları filtreler"""
    with open(json_dosya, "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)
    
    filtrelenmis_calisanlar = []
    for calisan in veri['calisanlar']:
        if filtre_fonksiyonu(calisan):
            filtrelenmis_calisanlar.append(calisan)
    
    return filtrelenmis_calisanlar

# IT departmanındaki çalışanları filtrele
it_calisanlari = json_filtrele("calisanlar.json", lambda c: c['departman'] == 'IT')
print("IT departmanındaki çalışanlar:")
for calisan in it_calisanlari:
    print(f"  {calisan['ad']} {calisan['soyad']}: {calisan['maas']} TL")

# Yüksek maaşlı çalışanlar
yuksek_maasli = json_filtrele("calisanlar.json", lambda c: c['maas'] > 7000)
print(f"\n7000+ maaşlı çalışan sayısı: {len(yuksek_maasli)}")

def json_guncelle(json_dosya, calisan_id, guncellemeler):
    """JSON dosyasındaki çalışan bilgilerini günceller"""
    with open(json_dosya, "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)
    
    for calisan in veri['calisanlar']:
        if calisan['id'] == calisan_id:
            calisan.update(guncellemeler)
            break
    
    with open(json_dosya, "w", encoding="utf-8") as dosya:
        json.dump(veri, dosya, ensure_ascii=False, indent=2)

# Çalışan bilgisini güncelle
json_guncelle("calisanlar.json", 1, {"maas": 9000, "departman": "Senior IT"})
print("✅ Çalışan bilgisi güncellendi")

# =============================================================================
# 5. ÖZEL VERİ TİPLERİ VE SERİALİZATİON
# =============================================================================

print("\n=== Özel Veri Tipleri ===")

# JSON desteklemeyen Python veri tipleri
ozel_veriler = {
    "tarih": datetime.now(),
    "dogum_tarihi": date(1990, 5, 15),
    "ondalik": Decimal("123.45"),
    "küme": {1, 2, 3, 4, 5},
    "tuple": (1, 2, 3)
}

print("Orijinal veri tipleri:")
for anahtar, deger in ozel_veriler.items():
    print(f"  {anahtar}: {deger} ({type(deger).__name__})")

# Özel encoder sınıfı
class OzelJSONEncoder(json.JSONEncoder):
    """Özel veri tiplerini JSON'a dönüştüren encoder"""
    
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, date):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, set):
            return list(obj)
        elif isinstance(obj, tuple):
            return list(obj)
        
        # Varsayılan davranış
        return super().default(obj)

# Özel encoder ile JSON'a dönüştür
json_string = json.dumps(ozel_veriler, cls=OzelJSONEncoder, ensure_ascii=False, indent=2)
print("\nÖzel encoder ile JSON:")
print(json_string)

# Özel decoder fonksiyonu
def ozel_decoder(dct):
    """JSON'dan özel veri tiplerini geri döndüren decoder"""
    for anahtar, deger in dct.items():
        # ISO format tarih string'ini datetime'a çevir
        if isinstance(deger, str) and 'T' in deger:
            try:
                dct[anahtar] = datetime.fromisoformat(deger.replace('Z', '+00:00'))
            except ValueError:
                pass
    return dct

# Özel decoder ile geri dönüştür
geri_donusum = json.loads(json_string, object_hook=ozel_decoder)
print("\nÖzel decoder ile geri dönüştürülen:")
for anahtar, deger in geri_donusum.items():
    print(f"  {anahtar}: {deger} ({type(deger).__name__})")

# =============================================================================
# 6. JSON ŞEMA DOĞRULAMA
# =============================================================================

print("\n=== JSON Şema Doğrulama ===")

def json_dogrula(veri, sema):
    """Basit JSON şema doğrulaması"""
    hatalar = []
    
    def dogrula_obje(obj, schema, yol=""):
        if schema.get("type") == "object":
            if not isinstance(obj, dict):
                hatalar.append(f"{yol}: object türü bekleniyor, {type(obj).__name__} bulundu")
                return
            
            # Gerekli alanları kontrol et
            for gerekli in schema.get("required", []):
                if gerekli not in obj:
                    hatalar.append(f"{yol}: gerekli alan eksik: {gerekli}")
            
            # Özellikleri kontrol et
            for alan, alan_sema in schema.get("properties", {}).items():
                if alan in obj:
                    dogrula_obje(obj[alan], alan_sema, f"{yol}.{alan}")
        
        elif schema.get("type") == "array":
            if not isinstance(obj, list):
                hatalar.append(f"{yol}: array türü bekleniyor")
                return
            
            # Öğeleri kontrol et
            if "items" in schema:
                for i, item in enumerate(obj):
                    dogrula_obje(item, schema["items"], f"{yol}[{i}]")
        
        elif schema.get("type") == "string":
            if not isinstance(obj, str):
                hatalar.append(f"{yol}: string türü bekleniyor")
        
        elif schema.get("type") == "number":
            if not isinstance(obj, (int, float)):
                hatalar.append(f"{yol}: number türü bekleniyor")
        
        elif schema.get("type") == "boolean":
            if not isinstance(obj, bool):
                hatalar.append(f"{yol}: boolean türü bekleniyor")
    
    dogrula_obje(veri, sema)
    return hatalar

# Çalışan şeması
calisan_semasi = {
    "type": "object",
    "required": ["id", "ad", "soyad", "departman"],
    "properties": {
        "id": {"type": "number"},
        "ad": {"type": "string"},
        "soyad": {"type": "string"},
        "departman": {"type": "string"},
        "maas": {"type": "number"},
        "yetenekler": {
            "type": "array",
            "items": {"type": "string"}
        },
        "aktif": {"type": "boolean"}
    }
}

# Test verisi
test_calisan = {
    "id": 1,
    "ad": "Test",
    "soyad": "Kullanıcı",
    "departman": "Test",
    "maas": 5000,
    "yetenekler": ["Python", "Testing"],
    "aktif": True
}

# Doğrulama
hatalar = json_dogrula(test_calisan, calisan_semasi)
if hatalar:
    print("❌ Doğrulama hataları:")
    for hata in hatalar:
        print(f"  {hata}")
else:
    print("✅ JSON şema doğrulaması başarılı")

# =============================================================================
# 7. JSON API İLE ÇALIŞMA
# =============================================================================

print("\n=== JSON API İle Çalışma ===")

def api_veri_cek(url):
    """API'den JSON veri çeker"""
    try:
        with urllib.request.urlopen(url) as response:
            veri = json.loads(response.read().decode('utf-8'))
            return {"basarili": True, "veri": veri}
    except Exception as e:
        return {"basarili": False, "hata": str(e)}

# Test API'si (JSONPlaceholder)
api_url = "https://jsonplaceholder.typicode.com/users/1"

print("📡 API'den veri çekiliyor...")
try:
    sonuc = api_veri_cek(api_url)
    if sonuc["basarili"]:
        kullanici = sonuc["veri"]
        print(f"✅ Kullanıcı bilgisi alındı:")
        print(f"  Ad: {kullanici['name']}")
        print(f"  Email: {kullanici['email']}")
        print(f"  Şehir: {kullanici['address']['city']}")
        
        # API verisini dosyaya kaydet
        with open("api_kullanici.json", "w", encoding="utf-8") as dosya:
            json.dump(kullanici, dosya, ensure_ascii=False, indent=2)
        print("📁 API verisi dosyaya kaydedildi")
    else:
        print(f"❌ API hatası: {sonuc['hata']}")
except:
    print("⚠️  Internet bağlantısı gerekli (API test atlandı)")

# =============================================================================
# 8. JSON VERİ ANALİZİ
# =============================================================================

print("\n=== JSON Veri Analizi ===")

def json_analiz_et(json_dosya):
    """JSON dosyasının yapısal analizini yapar"""
    with open(json_dosya, "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)
    
    def veri_analizi(obj, derinlik=0, yol="root"):
        analiz = {
            "tip": type(obj).__name__,
            "yol": yol,
            "derinlik": derinlik
        }
        
        if isinstance(obj, dict):
            analiz["anahtar_sayisi"] = len(obj)
            analiz["anahtarlar"] = list(obj.keys())
            analiz["alt_objeler"] = []
            
            for anahtar, deger in obj.items():
                alt_analiz = veri_analizi(deger, derinlik + 1, f"{yol}.{anahtar}")
                analiz["alt_objeler"].append(alt_analiz)
        
        elif isinstance(obj, list):
            analiz["eleman_sayisi"] = len(obj)
            if obj:
                analiz["ornek_tip"] = type(obj[0]).__name__
                if len(obj) <= 3:  # Küçük listeler için tüm elemanları analiz et
                    analiz["alt_objeler"] = []
                    for i, eleman in enumerate(obj):
                        alt_analiz = veri_analizi(eleman, derinlik + 1, f"{yol}[{i}]")
                        analiz["alt_objeler"].append(alt_analiz)
        
        elif isinstance(obj, str):
            analiz["uzunluk"] = len(obj)
        
        elif isinstance(obj, (int, float)):
            analiz["deger"] = obj
        
        return analiz
    
    return veri_analizi(veri)

# JSON analizi
analiz = json_analiz_et("calisanlar.json")

def analiz_yazdir(analiz_obj, girinti=0):
    """Analiz sonucunu düzenli şekilde yazdırır"""
    space = "  " * girinti
    print(f"{space}{analiz_obj['yol']} ({analiz_obj['tip']})")
    
    if "anahtar_sayisi" in analiz_obj:
        print(f"{space}  Anahtar sayısı: {analiz_obj['anahtar_sayisi']}")
    
    if "eleman_sayisi" in analiz_obj:
        print(f"{space}  Eleman sayısı: {analiz_obj['eleman_sayisi']}")
    
    if "uzunluk" in analiz_obj:
        print(f"{space}  Uzunluk: {analiz_obj['uzunluk']}")
    
    if "deger" in analiz_obj:
        print(f"{space}  Değer: {analiz_obj['deger']}")
    
    if "alt_objeler" in analiz_obj:
        for alt_obj in analiz_obj["alt_objeler"]:
            analiz_yazdir(alt_obj, girinti + 1)

print("JSON yapısal analizi:")
analiz_yazdir(analiz)

# =============================================================================
# 9. JSON PERFORMANS VE OPTİMİZASYON
# =============================================================================

print("\n=== JSON Performans ===")

import time

# Büyük JSON verisi oluştur
def buyuk_json_olustur(dosya_adi, kayit_sayisi=1000):
    """Test için büyük JSON dosyası oluşturur"""
    import random
    
    veriler = []
    for i in range(kayit_sayisi):
        veri = {
            "id": i + 1,
            "ad": f"Kullanıcı_{i+1}",
            "email": f"user{i+1}@example.com",
            "yas": random.randint(18, 65),
            "skor": random.uniform(0, 100),
            "aktif": random.choice([True, False]),
            "etiketler": [f"etiket_{j}" for j in range(random.randint(1, 5))],
            "profil": {
                "bio": f"Bu kullanıcı {i+1} numaralı kullanıcıdır.",
                "lokasyon": random.choice(["İstanbul", "Ankara", "İzmir"]),
                "puan": random.randint(1, 5)
            }
        }
        veriler.append(veri)
    
    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        json.dump({"kullanicilar": veriler}, dosya, ensure_ascii=False)

# 1000 kayıtlık JSON oluştur
buyuk_json_olustur("buyuk_veri.json", 1000)
print("✅ 1000 kayıtlık büyük JSON oluşturuldu")

def json_performans_test():
    """JSON okuma/yazma performansını test eder"""
    
    # Okuma performansı
    start = time.time()
    with open("buyuk_veri.json", "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)
    okuma_suresi = time.time() - start
    
    # Yazma performansı (kompakt)
    start = time.time()
    with open("buyuk_veri_kompakt.json", "w", encoding="utf-8") as dosya:
        json.dump(veri, dosya, ensure_ascii=False, separators=(',', ':'))
    yazma_kompakt = time.time() - start
    
    # Yazma performansı (formatlı)
    start = time.time()
    with open("buyuk_veri_formatli.json", "w", encoding="utf-8") as dosya:
        json.dump(veri, dosya, ensure_ascii=False, indent=2)
    yazma_formatli = time.time() - start
    
    # Dosya boyutları
    boyut_kompakt = os.path.getsize("buyuk_veri_kompakt.json")
    boyut_formatli = os.path.getsize("buyuk_veri_formatli.json")
    
    print(f"JSON Performans Sonuçları:")
    print(f"  Okuma: {okuma_suresi:.4f} saniye")
    print(f"  Yazma (kompakt): {yazma_kompakt:.4f} saniye")
    print(f"  Yazma (formatlı): {yazma_formatli:.4f} saniye")
    print(f"  Dosya boyutu (kompakt): {boyut_kompakt:,} byte")
    print(f"  Dosya boyutu (formatlı): {boyut_formatli:,} byte")
    print(f"  Boyut farkı: {boyut_formatli/boyut_kompakt:.2f}x")

json_performans_test()

# =============================================================================
# 10. JSON HATA YÖNETİMİ
# =============================================================================

print("\n=== JSON Hata Yönetimi ===")

def guvenli_json_oku(dosya_adi):
    """Hata kontrolü ile JSON okur"""
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            veri = json.load(dosya)
            return {"basarili": True, "veri": veri}
    
    except FileNotFoundError:
        return {"basarili": False, "hata": "Dosya bulunamadı"}
    
    except json.JSONDecodeError as e:
        return {
            "basarili": False, 
            "hata": f"JSON format hatası: {e.msg} (satır {e.lineno}, sütun {e.colno})"
        }
    
    except UnicodeDecodeError:
        return {"basarili": False, "hata": "Karakter encoding hatası"}
    
    except Exception as e:
        return {"basarili": False, "hata": f"Beklenmeyen hata: {e}"}

# Hatalı JSON test et
hatali_json = '''
{
    "ad": "Test",
    "yas": 25,
    "hobi": ["okuma", "yazma",] // Hatalı virgül
}
'''

with open("hatali.json", "w", encoding="utf-8") as dosya:
    dosya.write(hatali_json)

sonuc = guvenli_json_oku("hatali.json")
if sonuc["basarili"]:
    print("✅ JSON başarıyla okundu")
else:
    print(f"❌ JSON okuma hatası: {sonuc['hata']}")

# Düzeltilmiş JSON
duzgun_json = '''
{
    "ad": "Test",
    "yas": 25,
    "hobi": ["okuma", "yazma"]
}
'''

with open("duzgun.json", "w", encoding="utf-8") as dosya:
    dosya.write(duzgun_json)

sonuc = guvenli_json_oku("duzgun.json")
if sonuc["basarili"]:
    print("✅ Düzgün JSON başarıyla okundu")
    print(f"  Veri: {sonuc['veri']}")

# =============================================================================
# 11. TEMİZLİK - TEST DOSYALARINI SİL
# =============================================================================

print("\n=== Temizlik ===")

test_dosyalari = [
    "calisanlar.json",
    "calisanlar_kompakt.json",
    "calisanlar_sirali.json",
    "api_kullanici.json",
    "buyuk_veri.json",
    "buyuk_veri_kompakt.json",
    "buyuk_veri_formatli.json",
    "hatali.json",
    "duzgun.json"
]

silinen_sayisi = 0
for dosya in test_dosyalari:
    try:
        if os.path.exists(dosya):
            os.remove(dosya)
            silinen_sayisi += 1
    except Exception as e:
        print(f"❌ {dosya} silinemedi: {e}")

print(f"🗑️  {silinen_sayisi} test dosyası temizlendi")

print("\n✅ JSON dosya işlemleri öğrenildi!")
print("✅ JSON serialization/deserialization öğrenildi!")
print("✅ Özel veri tipleri ve encoder/decoder öğrenildi!")
print("✅ JSON API kullanımı ve veri analizi öğrenildi!")
print("✅ JSON performans optimizasyonu ve hata yönetimi öğrenildi!")