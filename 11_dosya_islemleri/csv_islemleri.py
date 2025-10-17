"""
Python CSV Dosya İşlemleri

Bu dosya Python'da CSV (Comma Separated Values) dosyaları ile
çalışmayı kapsamlı olarak ele alır. csv modülü kullanımı,
veri okuma/yazma ve CSV dosyalarını işleme teknikleri öğreneceğiz.
"""

import csv
import os
from io import StringIO
from collections import namedtuple, OrderedDict
import json

# =============================================================================
# 1. CSV NEDİR VE TEMEL KULLANIM
# =============================================================================

print("=== CSV Dosya İşlemleri ===")

"""
CSV (Comma Separated Values) - virgülle ayrılmış değerler
- Tabular veri depolamak için yaygın format
- Excel, Google Sheets gibi uygulamalar destekler
- Basit text format, kolayca okunabilir
- Büyük veri setleri için verimli
"""

# Basit CSV verisi oluşturalım
csv_verisi = """ad,soyad,yas,sehir,maas
Ahmet,Yılmaz,25,İstanbul,5000
Ayşe,Kaya,30,Ankara,6000
Mehmet,Öz,35,İzmir,7000
Fatma,Ak,28,Bursa,5500
Ali,Veli,32,Antalya,6200"""

# CSV dosyası oluştur
with open("calisanlar.csv", "w", encoding="utf-8") as dosya:
    dosya.write(csv_verisi)

print("✅ Örnek CSV dosyası oluşturuldu")

# =============================================================================
# 2. CSV OKUMA İŞLEMLERİ
# =============================================================================

print("\n=== CSV Okuma İşlemleri ===")

# 2.1 csv.reader() ile okuma
print("--- csv.reader() ile Okuma ---")
with open("calisanlar.csv", "r", encoding="utf-8") as dosya:
    csv_okuyucu = csv.reader(dosya)
    
    # İlk satır genelde başlık
    basliklar = next(csv_okuyucu)
    print(f"Başlıklar: {basliklar}")
    
    print("Veriler:")
    for satir_no, satir in enumerate(csv_okuyucu, 1):
        print(f"  {satir_no}: {satir}")

# 2.2 csv.DictReader() ile okuma (daha kullanışlı)
print("\n--- csv.DictReader() ile Okuma ---")
with open("calisanlar.csv", "r", encoding="utf-8") as dosya:
    csv_okuyucu = csv.DictReader(dosya)
    
    print("DictReader ile veriler:")
    for satir_no, satir in enumerate(csv_okuyucu, 1):
        print(f"  {satir_no}: {dict(satir)}")
        print(f"      Ad: {satir['ad']}, Maaş: {satir['maas']}")

# 2.3 Belirli alanları okuma
print("\n--- Belirli Alanları Okuma ---")
def yuksek_maasli_calisanlar(dosya_adi, minimum_maas=6000):
    """Minimum maaşın üzerindeki çalışanları döndürür"""
    yuksek_maaslilar = []
    
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        csv_okuyucu = csv.DictReader(dosya)
        
        for satir in csv_okuyucu:
            if int(satir['maas']) >= minimum_maas:
                yuksek_maaslilar.append({
                    'ad_soyad': f"{satir['ad']} {satir['soyad']}",
                    'sehir': satir['sehir'],
                    'maas': int(satir['maas'])
                })
    
    return yuksek_maaslilar

yuksek_maaslilar = yuksek_maasli_calisanlar("calisanlar.csv")
print("6000+ maaşlı çalışanlar:")
for calisan in yuksek_maaslilar:
    print(f"  {calisan['ad_soyad']} ({calisan['sehir']}): {calisan['maas']} TL")

# =============================================================================
# 3. CSV YAZMA İŞLEMLERİ
# =============================================================================

print("\n=== CSV Yazma İşlemleri ===")

# 3.1 csv.writer() ile yazma
print("--- csv.writer() ile Yazma ---")
yeni_calisanlar = [
    ["Zeynep", "Demirci", 29, "Gaziantep", 5800],
    ["Murat", "Şen", 33, "Adana", 6500],
    ["Elif", "Güzel", 27, "Konya", 5300]
]

with open("yeni_calisanlar.csv", "w", newline="", encoding="utf-8") as dosya:
    csv_yazici = csv.writer(dosya)
    
    # Başlık yaz
    csv_yazici.writerow(["ad", "soyad", "yas", "sehir", "maas"])
    
    # Veri satırlarını yaz
    csv_yazici.writerows(yeni_calisanlar)

print("✅ Yeni çalışanlar CSV'si oluşturuldu")

# 3.2 csv.DictWriter() ile yazma (daha kullanışlı)
print("\n--- csv.DictWriter() ile Yazma ---")
departman_verileri = [
    {"departman": "IT", "calisan_sayisi": 15, "ortalama_maas": 7500},
    {"departman": "İnsan Kaynakları", "calisan_sayisi": 8, "ortalama_maas": 6000},
    {"departman": "Pazarlama", "calisan_sayisi": 12, "ortalama_maas": 6500},
    {"departman": "Finans", "calisan_sayisi": 10, "ortalama_maas": 7000}
]

with open("departmanlar.csv", "w", newline="", encoding="utf-8") as dosya:
    alanlar = ["departman", "calisan_sayisi", "ortalama_maas"]
    csv_yazici = csv.DictWriter(dosya, fieldnames=alanlar)
    
    # Başlık yaz
    csv_yazici.writeheader()
    
    # Veri satırlarını yaz
    csv_yazici.writerows(departman_verileri)

print("✅ Departman verileri CSV'si oluşturuldu")

# 3.3 Mevcut CSV'ye ekleme
print("\n--- Mevcut CSV'ye Ekleme ---")
ek_calisan = {
    "ad": "Berkay",
    "soyad": "Yıldız", 
    "yas": 26,
    "sehir": "Trabzon",
    "maas": 5700
}

with open("calisanlar.csv", "a", newline="", encoding="utf-8") as dosya:
    alanlar = ["ad", "soyad", "yas", "sehir", "maas"]
    csv_yazici = csv.DictWriter(dosya, fieldnames=alanlar)
    csv_yazici.writerow(ek_calisan)

print("✅ Yeni çalışan eklendi")

# =============================================================================
# 4. FARKLI DELIMITER'LAR VE FORMATLAR
# =============================================================================

print("\n=== Farklı Delimiter'lar ===")

# Noktalı virgül (;) ile ayrılmış CSV
noktalivi_veri = """ad;soyad;yas;sehir
Emre;Köse;31;Samsun
Deniz;Özkan;24;Eskişehir
Çağla;Arslan;28;Kayseri"""

with open("noktalivi.csv", "w", encoding="utf-8") as dosya:
    dosya.write(noktalivi_veri)

# Noktalı virgül delimiter ile okuma
print("--- Noktalı Virgül Delimiter ---")
with open("noktalivi.csv", "r", encoding="utf-8") as dosya:
    csv_okuyucu = csv.DictReader(dosya, delimiter=";")
    for satir in csv_okuyucu:
        print(f"  {satir['ad']} {satir['soyad']} - {satir['sehir']}")

# Tab ile ayrılmış (TSV)
tab_veri = """urun\tfiyat\tstok
Laptop\t15000\t25
Mouse\t150\t100
Klavye\t400\t50"""

with open("urunler.tsv", "w", encoding="utf-8") as dosya:
    dosya.write(tab_veri)

print("\n--- Tab Delimiter ---")
with open("urunler.tsv", "r", encoding="utf-8") as dosya:
    csv_okuyucu = csv.DictReader(dosya, delimiter="\t")
    for satir in csv_okuyucu:
        print(f"  {satir['urun']}: {satir['fiyat']} TL (Stok: {satir['stok']})")

# Özel delimiter ve quote character
print("\n--- Özel Formatlar ---")
ozel_veri = '''isim|"aciklama"|fiyat
"Akıllı Telefon"|"Son teknoloji, 128GB"|8500
"Tablet"|"10 inç ekran, WiFi"|3200'''

with open("ozel_format.csv", "w", encoding="utf-8") as dosya:
    dosya.write(ozel_veri)

with open("ozel_format.csv", "r", encoding="utf-8") as dosya:
    csv_okuyucu = csv.DictReader(dosya, delimiter="|", quotechar='"')
    for satir in csv_okuyucu:
        print(f"  {satir['isim']}: {satir['aciklama']} - {satir['fiyat']} TL")

# =============================================================================
# 5. CSV VERİ ANALİZİ VE İSTATİSTİKLER
# =============================================================================

print("\n=== CSV Veri Analizi ===")

def csv_analiz_et(dosya_adi):
    """CSV dosyasının temel analizini yapar"""
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        csv_okuyucu = csv.DictReader(dosya)
        veriler = list(csv_okuyucu)
    
    if not veriler:
        return {"hata": "Boş dosya"}
    
    # Temel bilgiler
    satir_sayisi = len(veriler)
    sutun_sayisi = len(veriler[0].keys())
    sutun_isimleri = list(veriler[0].keys())
    
    # Sayısal sütunları bul ve analiz et
    sayisal_analizler = {}
    
    for sutun in sutun_isimleri:
        sayisal_degerler = []
        
        for satir in veriler:
            try:
                deger = float(satir[sutun])
                sayisal_degerler.append(deger)
            except (ValueError, TypeError):
                continue
        
        if sayisal_degerler:
            sayisal_analizler[sutun] = {
                "ortalama": sum(sayisal_degerler) / len(sayisal_degerler),
                "minimum": min(sayisal_degerler),
                "maksimum": max(sayisal_degerler),
                "toplam": sum(sayisal_degerler),
                "sayisal_deger_sayisi": len(sayisal_degerler)
            }
    
    return {
        "dosya": dosya_adi,
        "satir_sayisi": satir_sayisi,
        "sutun_sayisi": sutun_sayisi,
        "sutun_isimleri": sutun_isimleri,
        "sayisal_analizler": sayisal_analizler
    }

# Çalışanlar CSV'sini analiz et
analiz = csv_analiz_et("calisanlar.csv")
print("Çalışanlar CSV Analizi:")
print(f"  Satır sayısı: {analiz['satir_sayisi']}")
print(f"  Sütun sayısı: {analiz['sutun_sayisi']}")
print(f"  Sütunlar: {', '.join(analiz['sutun_isimleri'])}")

for sutun, stats in analiz['sayisal_analizler'].items():
    print(f"\n  {sutun.title()} istatistikleri:")
    for metrik, deger in stats.items():
        if metrik != "sayisal_deger_sayisi":
            print(f"    {metrik.title()}: {deger:.2f}")

# =============================================================================
# 6. CSV VERİ MANİPÜLASYONU
# =============================================================================

print("\n=== CSV Veri Manipülasyonu ===")

def csv_filtrele(kaynak_dosya, hedef_dosya, filtre_fonksiyonu):
    """CSV dosyasını filtreler ve yeni dosyaya yazar"""
    with open(kaynak_dosya, "r", encoding="utf-8") as kaynak:
        okuyucu = csv.DictReader(kaynak)
        alanlar = okuyucu.fieldnames
        
        with open(hedef_dosya, "w", newline="", encoding="utf-8") as hedef:
            yazici = csv.DictWriter(hedef, fieldnames=alanlar)
            yazici.writeheader()
            
            for satir in okuyucu:
                if filtre_fonksiyonu(satir):
                    yazici.writerow(satir)

# İstanbul'daki çalışanları filtrele
csv_filtrele(
    "calisanlar.csv",
    "istanbul_calisanlari.csv",
    lambda satir: satir['sehir'] == 'İstanbul'
)

print("✅ İstanbul çalışanları filtrelendi")

def csv_sirala(kaynak_dosya, hedef_dosya, siralama_anahtari, ters=False):
    """CSV dosyasını belirli alana göre sıralar"""
    with open(kaynak_dosya, "r", encoding="utf-8") as kaynak:
        okuyucu = csv.DictReader(kaynak)
        veriler = list(okuyucu)
        alanlar = okuyucu.fieldnames
    
    # Sıralama anahtarı sayısal mı kontrol et
    def siralama_fonksiyonu(satir):
        deger = satir[siralama_anahtari]
        try:
            return float(deger)
        except ValueError:
            return deger
    
    sirali_veriler = sorted(veriler, key=siralama_fonksiyonu, reverse=ters)
    
    with open(hedef_dosya, "w", newline="", encoding="utf-8") as hedef:
        yazici = csv.DictWriter(hedef, fieldnames=alanlar)
        yazici.writeheader()
        yazici.writerows(sirali_veriler)

# Maaşa göre sırala (yüksekten düşüğe)
csv_sirala("calisanlar.csv", "maas_sirali.csv", "maas", ters=True)
print("✅ Maaşa göre sıralandı")

# Sıralı dosyayı kontrol et
with open("maas_sirali.csv", "r", encoding="utf-8") as dosya:
    okuyucu = csv.DictReader(dosya)
    print("Maaşa göre sıralı çalışanlar:")
    for satir in okuyucu:
        print(f"  {satir['ad']} {satir['soyad']}: {satir['maas']} TL")

# =============================================================================
# 7. CSV VE JSON DÖNÜŞÜMÜ
# =============================================================================

print("\n=== CSV - JSON Dönüşümü ===")

def csv_to_json(csv_dosya, json_dosya):
    """CSV dosyasını JSON'a dönüştürür"""
    with open(csv_dosya, "r", encoding="utf-8") as csvfile:
        okuyucu = csv.DictReader(csvfile)
        veriler = list(okuyucu)
    
    with open(json_dosya, "w", encoding="utf-8") as jsonfile:
        json.dump(veriler, jsonfile, ensure_ascii=False, indent=2)

def json_to_csv(json_dosya, csv_dosya):
    """JSON dosyasını CSV'ye dönüştürür"""
    with open(json_dosya, "r", encoding="utf-8") as jsonfile:
        veriler = json.load(jsonfile)
    
    if not veriler:
        return
    
    alanlar = veriler[0].keys()
    
    with open(csv_dosya, "w", newline="", encoding="utf-8") as csvfile:
        yazici = csv.DictWriter(csvfile, fieldnames=alanlar)
        yazici.writeheader()
        yazici.writerows(veriler)

# CSV'yi JSON'a dönüştür
csv_to_json("departmanlar.csv", "departmanlar.json")
print("✅ CSV, JSON'a dönüştürüldü")

# JSON dosyasını oku ve göster
with open("departmanlar.json", "r", encoding="utf-8") as dosya:
    json_veri = json.load(dosya)
    print("JSON içeriği:")
    print(json.dumps(json_veri, ensure_ascii=False, indent=2))

# JSON'ı tekrar CSV'ye dönüştür
json_to_csv("departmanlar.json", "departmanlar_yeni.csv")
print("✅ JSON, CSV'ye dönüştürüldü")

# =============================================================================
# 8. BÜYÜK CSV DOSYALARI İLE ÇALIŞMA
# =============================================================================

print("\n=== Büyük CSV Dosyaları ===")

# Büyük test CSV'si oluştur
def buyuk_csv_olustur(dosya_adi, satir_sayisi=10000):
    """Test için büyük CSV dosyası oluşturur"""
    import random
    
    isimler = ["Ahmet", "Ayşe", "Mehmet", "Fatma", "Ali", "Zeynep", "Murat", "Elif"]
    soyisimler = ["Yılmaz", "Kaya", "Öz", "Ak", "Veli", "Demir", "Şen", "Güzel"]
    sehirler = ["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya", "Adana"]
    
    with open(dosya_adi, "w", newline="", encoding="utf-8") as dosya:
        yazici = csv.writer(dosya)
        yazici.writerow(["id", "ad", "soyad", "yas", "sehir", "maas"])
        
        for i in range(satir_sayisi):
            yazici.writerow([
                i + 1,
                random.choice(isimler),
                random.choice(soyisimler),
                random.randint(22, 65),
                random.choice(sehirler),
                random.randint(4000, 15000)
            ])

# 1000 satırlık test dosyası
buyuk_csv_olustur("buyuk_calisanlar.csv", 1000)
print("✅ 1000 satırlık büyük CSV oluşturuldu")

# Chunk halinde okuma
def csv_chunk_isle(dosya_adi, chunk_boyutu=100):
    """Büyük CSV'yi chunk halinde işler"""
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        okuyucu = csv.DictReader(dosya)
        
        chunk = []
        for satir_no, satir in enumerate(okuyucu, 1):
            chunk.append(satir)
            
            if len(chunk) == chunk_boyutu:
                yield chunk
                chunk = []
        
        # Son chunk (tam olmayabilir)
        if chunk:
            yield chunk

# Şehir bazında toplam maaş hesapla (chunk'larla)
sehir_maaslari = {}
chunk_sayisi = 0

for chunk in csv_chunk_isle("buyuk_calisanlar.csv", 200):
    chunk_sayisi += 1
    
    for satir in chunk:
        sehir = satir['sehir']
        maas = int(satir['maas'])
        
        if sehir not in sehir_maaslari:
            sehir_maaslari[sehir] = {'toplam': 0, 'sayisi': 0}
        
        sehir_maaslari[sehir]['toplam'] += maas
        sehir_maaslari[sehir]['sayisi'] += 1

print(f"📊 {chunk_sayisi} chunk işlendi")
print("Şehir bazında ortalama maaşlar:")
for sehir, veriler in sehir_maaslari.items():
    ortalama = veriler['toplam'] / veriler['sayisi']
    print(f"  {sehir}: {ortalama:.0f} TL (Çalışan: {veriler['sayisi']})")

# =============================================================================
# 9. CSV HATA YÖNETİMİ
# =============================================================================

print("\n=== CSV Hata Yönetimi ===")

def guvenli_csv_oku(dosya_adi):
    """Hata kontrolü ile CSV okur"""
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            # CSV formatını kontrol et
            sample = dosya.read(1024)
            dosya.seek(0)
            
            # Dialect'i tahmin et
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(sample)
            
            print(f"Tespit edilen delimiter: '{dialect.delimiter}'")
            print(f"Quote character: '{dialect.quotechar}'")
            
            okuyucu = csv.DictReader(dosya, dialect=dialect)
            veriler = []
            hata_satirlari = []
            
            for satir_no, satir in enumerate(okuyucu, 2):  # 2'den başla (header 1. satır)
                try:
                    # Veri doğrulama
                    if not all(satir.values()):  # Boş alan kontrolü
                        hata_satirlari.append(f"Satır {satir_no}: Boş alanlar var")
                    else:
                        veriler.append(satir)
                except Exception as e:
                    hata_satirlari.append(f"Satır {satir_no}: {e}")
            
            return {
                "basarili": True,
                "veriler": veriler,
                "satir_sayisi": len(veriler),
                "hatalar": hata_satirlari
            }
            
    except FileNotFoundError:
        return {"basarili": False, "hata": "Dosya bulunamadı"}
    except csv.Error as e:
        return {"basarili": False, "hata": f"CSV hatası: {e}"}
    except Exception as e:
        return {"basarili": False, "hata": f"Beklenmeyen hata: {e}"}

# Güvenli okuma testi
sonuc = guvenli_csv_oku("calisanlar.csv")
if sonuc["basarili"]:
    print(f"✅ {sonuc['satir_sayisi']} satır başarıyla okundu")
    if sonuc["hatalar"]:
        print("⚠️  Hatalar:")
        for hata in sonuc["hatalar"]:
            print(f"  {hata}")
else:
    print(f"❌ Okuma hatası: {sonuc['hata']}")

# =============================================================================
# 10. CSV PERFORMANS İPUÇLARI
# =============================================================================

print("\n=== CSV Performans İpuçları ===")

import time

def performans_karsilastir():
    """Farklı CSV okuma yöntemlerinin performansını karşılaştırır"""
    
    # 1. csv.reader ile okuma
    start = time.time()
    with open("buyuk_calisanlar.csv", "r", encoding="utf-8") as dosya:
        okuyucu = csv.reader(dosya)
        veriler = list(okuyucu)
    reader_time = time.time() - start
    
    # 2. csv.DictReader ile okuma
    start = time.time()
    with open("buyuk_calisanlar.csv", "r", encoding="utf-8") as dosya:
        okuyucu = csv.DictReader(dosya)
        veriler = list(okuyucu)
    dictreader_time = time.time() - start
    
    print(f"csv.reader: {reader_time:.4f} saniye")
    print(f"csv.DictReader: {dictreader_time:.4f} saniye")
    print(f"DictReader oranı: {dictreader_time/reader_time:.2f}x yavaş")

# performans_karsilastir()  # Çok fazla çıktı olmasın diye yorum satırında

print("\n💡 CSV Performans İpuçları:")
print("  - Büyük dosyalar için chunk'larla okuyun")
print("  - Sadece gerekli sütunları işleyin")
print("  - csv.reader, csv.DictReader'dan daha hızlıdır")
print("  - Dosya okuma sırasında veri doğrulama yapmayın")
print("  - Sık kullanım için pandas library'sini düşünün")

# =============================================================================
# 11. TEMİZLİK - TEST DOSYALARINI SİL
# =============================================================================

print("\n=== Temizlik ===")

test_dosyalari = [
    "calisanlar.csv",
    "yeni_calisanlar.csv", 
    "departmanlar.csv",
    "noktalivi.csv",
    "urunler.tsv",
    "ozel_format.csv",
    "istanbul_calisanlari.csv",
    "maas_sirali.csv",
    "departmanlar.json",
    "departmanlar_yeni.csv",
    "buyuk_calisanlar.csv"
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

print("\n✅ CSV dosya işlemleri öğrenildi!")
print("✅ csv.reader ve csv.DictReader kullanımı öğrenildi!")
print("✅ CSV veri analizi ve manipülasyonu öğrenildi!")
print("✅ Büyük CSV dosyaları ile çalışma teknikleri öğrenildi!")