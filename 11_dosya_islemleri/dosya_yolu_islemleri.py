"""
Python Dosya Yolu İşlemleri

Bu dosya Python'da dosya ve klasör yolu işlemlerini kapsamlı olarak ele alır.
os, pathlib modülleri kullanımı, dosya sistemi navigasyonu ve
platform bağımsız yol işlemleri öğreneceğiz.
"""

import os
import sys
from pathlib import Path
import shutil
import glob
import fnmatch
from datetime import datetime
import tempfile

# =============================================================================
# 1. DOSYA YOLU TEMELLERİ
# =============================================================================

print("=== Dosya Yolu İşlemleri ===")

# Mevcut çalışma dizini
mevcut_dizin = os.getcwd()
print(f"🗂️  Mevcut çalışma dizini: {mevcut_dizin}")

# Python dosyasının bulunduğu dizin
script_dizini = os.path.dirname(os.path.abspath(__file__))
print(f"📄 Script dizini: {script_dizini}")

# Kullanıcı ana dizini
kullanici_dizini = os.path.expanduser("~")
print(f"🏠 Kullanıcı dizini: {kullanici_dizini}")

# Sistem geçici dizini
gecici_dizin = tempfile.gettempdir()
print(f"⏳ Geçici dizin: {gecici_dizin}")

# Platform bilgisi
print(f"💻 İşletim sistemi: {os.name}")
print(f"🔧 Platform: {sys.platform}")
print(f"📁 Yol ayırıcı: '{os.sep}'")

# =============================================================================
# 2. OS MODÜLÜ İLE YOL İŞLEMLERİ
# =============================================================================

print("\n=== os Modülü ile Yol İşlemleri ===")

# Yol birleştirme
dosya_yolu = os.path.join("klasor", "alt_klasor", "dosya.txt")
print(f"Birleştirilmiş yol: {dosya_yolu}")

# Yol parçalarına ayırma
klasor_adi = os.path.dirname(dosya_yolu)
dosya_adi = os.path.basename(dosya_yolu)
print(f"Klasör adı: {klasor_adi}")
print(f"Dosya adı: {dosya_adi}")

# Dosya adı ve uzantısı
isim, uzanti = os.path.splitext("dokuman.pdf")
print(f"Dosya ismi: {isim}")
print(f"Uzantı: {uzanti}")

# Mutlak yol
mutlak_yol = os.path.abspath("test.txt")
print(f"Mutlak yol: {mutlak_yol}")

# Yol var mı kontrolü
test_yollar = [
    mevcut_dizin,
    "olmayan_klasor",
    __file__,
    "olmayan_dosya.txt"
]

print("\nYol varlık kontrolü:")
for yol in test_yollar:
    if os.path.exists(yol):
        if os.path.isfile(yol):
            print(f"✅ Dosya: {yol}")
        elif os.path.isdir(yol):
            print(f"📁 Klasör: {yol}")
        else:
            print(f"❓ Diğer: {yol}")
    else:
        print(f"❌ Mevcut değil: {yol}")

# =============================================================================
# 3. PATHLIB MODÜLÜ (MODERN YAKLAŞIM)
# =============================================================================

print("\n=== pathlib Modülü (Modern Yaklaşım) ===")

# Path objesi oluşturma
mevcut_path = Path.cwd()
print(f"🗂️  Mevcut dizin (Path): {mevcut_path}")

# Dosya yolu oluşturma
dosya_path = Path("test_klasor") / "alt_klasor" / "test_dosya.txt"
print(f"Path yolu: {dosya_path}")

# Path özellikler
ornek_dosya = Path(__file__)
print(f"\nDosya analizi: {ornek_dosya}")
print(f"  İsim: {ornek_dosya.name}")
print(f"  Stem (uzantısız): {ornek_dosya.stem}")
print(f"  Uzantı: {ornek_dosya.suffix}")
print(f"  Tüm uzantılar: {ornek_dosya.suffixes}")
print(f"  Üst klasör: {ornek_dosya.parent}")
print(f"  Mutlak yol: {ornek_dosya.absolute()}")

# Path parçaları
print(f"  Path parçaları: {ornek_dosya.parts}")

# Varlık kontrolü (pathlib ile)
print(f"  Var mı? {ornek_dosya.exists()}")
print(f"  Dosya mı? {ornek_dosya.is_file()}")
print(f"  Klasör mü? {ornek_dosya.is_dir()}")

# =============================================================================
# 4. KLASÖR İŞLEMLERİ
# =============================================================================

print("\n=== Klasör İşlemleri ===")

# Test klasörü oluşturma
test_klasor = Path("dosya_test_klasoru")

# Klasör oluştur
if not test_klasor.exists():
    test_klasor.mkdir()
    print(f"✅ Klasör oluşturuldu: {test_klasor}")

# Alt klasörler oluştur
alt_klasorler = ["belgelerin", "resimler", "videolar", "arşiv/eski"]

for klasor in alt_klasorler:
    klasor_yolu = test_klasor / klasor
    klasor_yolu.mkdir(parents=True, exist_ok=True)
    print(f"📁 Alt klasör oluşturuldu: {klasor_yolu}")

# Test dosyaları oluştur
test_dosyalar = [
    "belgeler/rapor.txt",
    "belgeler/sunum.pdf", 
    "resimler/foto1.jpg",
    "resimler/foto2.png",
    "videolar/video1.mp4",
    "arşiv/eski/eski_dokuman.doc"
]

for dosya in test_dosyalar:
    dosya_yolu = test_klasor / dosya
    dosya_yolu.parent.mkdir(parents=True, exist_ok=True)
    dosya_yolu.write_text(f"Bu {dosya} dosyasının içeriğidir.", encoding="utf-8")
    print(f"📄 Dosya oluşturuldu: {dosya_yolu}")

# =============================================================================
# 5. KLASÖR TARAMA VE LİSTELEME
# =============================================================================

print("\n=== Klasör Tarama ve Listeleme ===")

def klasor_listele(klasor_yolu, detay=False):
    """Klasör içeriğini listeler"""
    klasor = Path(klasor_yolu)
    
    if not klasor.exists():
        print(f"❌ Klasör bulunamadı: {klasor}")
        return
    
    print(f"\n📂 {klasor} içeriği:")
    
    try:
        for item in sorted(klasor.iterdir()):
            if item.is_file():
                if detay:
                    boyut = item.stat().st_size
                    degisiklik = datetime.fromtimestamp(item.stat().st_mtime)
                    print(f"  📄 {item.name} ({boyut} byte, {degisiklik.strftime('%Y-%m-%d %H:%M')})")
                else:
                    print(f"  📄 {item.name}")
            elif item.is_dir():
                if detay:
                    item_sayisi = len(list(item.iterdir()))
                    print(f"  📁 {item.name}/ ({item_sayisi} öğe)")
                else:
                    print(f"  📁 {item.name}/")
    except PermissionError:
        print("  ❌ Erişim izni yok")

# Test klasörünü listele
klasor_listele(test_klasor, detay=True)

# Rekürsif listeleme
def rekursif_listele(klasor_yolu, max_derinlik=3, mevcut_derinlik=0):
    """Klasörü rekürsif olarak listeler"""
    if mevcut_derinlik >= max_derinlik:
        return
    
    klasor = Path(klasor_yolu)
    girinti = "  " * mevcut_derinlik
    
    try:
        for item in sorted(klasor.iterdir()):
            if item.is_file():
                print(f"{girinti}📄 {item.name}")
            elif item.is_dir():
                print(f"{girinti}📁 {item.name}/")
                rekursif_listele(item, max_derinlik, mevcut_derinlik + 1)
    except PermissionError:
        print(f"{girinti}❌ Erişim izni yok")

print("\n--- Rekürsif Listeleme ---")
rekursif_listele(test_klasor)

# =============================================================================
# 6. DOSYA ARAMA VE FİLTRELEME
# =============================================================================

print("\n=== Dosya Arama ve Filtreleme ===")

# Uzantıya göre arama
def uzantiya_gore_ara(klasor_yolu, uzanti):
    """Belirli uzantıdaki dosyaları bulur"""
    klasor = Path(klasor_yolu)
    bulunan_dosyalar = []
    
    # Recursive glob kullanımı
    pattern = f"**/*.{uzanti.lstrip('.')}"
    
    for dosya in klasor.glob(pattern):
        bulunan_dosyalar.append(dosya)
    
    return bulunan_dosyalar

# PDF dosyalarını ara
pdf_dosyalar = uzantiya_gore_ara(test_klasor, "pdf")
print(f"PDF dosyaları ({len(pdf_dosyalar)} adet):")
for dosya in pdf_dosyalar:
    print(f"  📄 {dosya}")

# Resim dosyalarını ara
resim_uzantilari = ["jpg", "jpeg", "png", "gif", "bmp"]
tum_resimler = []

for uzanti in resim_uzantilari:
    resimler = uzantiya_gore_ara(test_klasor, uzanti)
    tum_resimler.extend(resimler)

print(f"\nResim dosyaları ({len(tum_resimler)} adet):")
for resim in tum_resimler:
    print(f"  🖼️  {resim}")

# Dosya boyutuna göre filtreleme
def boyuta_gore_filtrele(klasor_yolu, min_boyut=0, max_boyut=float('inf')):
    """Dosyaları boyutlarına göre filtreler"""
    klasor = Path(klasor_yolu)
    filtrelenmis = []
    
    for dosya in klasor.rglob("*"):
        if dosya.is_file():
            boyut = dosya.stat().st_size
            if min_boyut <= boyut <= max_boyut:
                filtrelenmis.append((dosya, boyut))
    
    return sorted(filtrelenmis, key=lambda x: x[1], reverse=True)

# Küçük dosyalar (100 byte altı)
kucuk_dosyalar = boyuta_gore_filtrele(test_klasor, max_boyut=100)
print(f"\nKüçük dosyalar (≤100 byte):")
for dosya, boyut in kucuk_dosyalar:
    print(f"  📄 {dosya.name}: {boyut} byte")

# =============================================================================
# 7. GLOB MODÜLİ İLE PATTERN MATCHING
# =============================================================================

print("\n=== Glob Modülü ile Pattern Matching ===")

# Glob kullanımı
os.chdir(test_klasor)  # Test klasörüne geç

# Tüm .txt dosyalar
txt_dosyalar = glob.glob("**/*.txt", recursive=True)
print(f"TXT dosyaları: {txt_dosyalar}")

# İsimde "rapor" geçen dosyalar
rapor_dosyalar = glob.glob("**/rapor*", recursive=True)
print(f"'rapor' içeren dosyalar: {rapor_dosyalar}")

# Tek karakter wildcard
jpg_dosyalar = glob.glob("**/foto?.jpg", recursive=True)
print(f"foto[X].jpg dosyaları: {jpg_dosyalar}")

# Karakter aralığı
# video1-9 aralığında
video_dosyalar = glob.glob("**/video[1-9].mp4", recursive=True)
print(f"video[1-9].mp4 dosyaları: {video_dosyalar}")

# fnmatch ile pattern matching
print("\n--- fnmatch ile Pattern Matching ---")
dosya_listesi = ["test.txt", "Test.TXT", "dosya.pdf", "resim.jpg", "VIDEO.mp4"]

for pattern in ["*.txt", "*.[Tt][Xx][Tt]", "*.{pdf,jpg}", "*.[a-z]*"]:
    eslesen = [f for f in dosya_listesi if fnmatch.fnmatch(f.lower(), pattern.lower())]
    print(f"Pattern '{pattern}': {eslesen}")

# Orijinal dizine dön
os.chdir(mevcut_dizin)

# =============================================================================
# 8. DOSYA KOPYALAMA VE TAŞIMA
# =============================================================================

print("\n=== Dosya Kopyalama ve Taşıma ===")

# Yedek klasörü oluştur
yedek_klasor = Path("yedek_klasoru")
yedek_klasor.mkdir(exist_ok=True)

# Tek dosya kopyalama
kaynak_dosya = test_klasor / "belgeler" / "rapor.txt"
hedef_dosya = yedek_klasor / "rapor_yedeği.txt"

if kaynak_dosya.exists():
    shutil.copy2(kaynak_dosya, hedef_dosya)  # copy2 metadata'yı da kopyalar
    print(f"✅ Dosya kopyalandı: {kaynak_dosya} → {hedef_dosya}")

# Klasör kopyalama
kaynak_klasor = test_klasor / "resimler"
hedef_klasor = yedek_klasor / "resimler_yedeği"

if kaynak_klasor.exists():
    shutil.copytree(kaynak_klasor, hedef_klasor, dirs_exist_ok=True)
    print(f"✅ Klasör kopyalandı: {kaynak_klasor} → {hedef_klasor}")

# Dosya taşıma
tasınacak_dosya = test_klasor / "belgeler" / "sunum.pdf"
yeni_konum = yedek_klasor / "sunum_taşındı.pdf"

if tasınacak_dosya.exists():
    shutil.move(str(tasınacak_dosya), str(yeni_konum))
    print(f"✅ Dosya taşındı: {tasınacak_dosya} → {yeni_konum}")

# =============================================================================
# 9. DOSYA İZİNLERİ VE METAVERİLER
# =============================================================================

print("\n=== Dosya İzinleri ve Metaveriler ===")

def dosya_bilgileri_goster(dosya_yolu):
    """Dosya hakkında detaylı bilgi gösterir"""
    dosya = Path(dosya_yolu)
    
    if not dosya.exists():
        print(f"❌ Dosya bulunamadı: {dosya}")
        return
    
    stat = dosya.stat()
    
    print(f"\n📄 {dosya.name} bilgileri:")
    print(f"  📁 Tam yol: {dosya.absolute()}")
    print(f"  📏 Boyut: {stat.st_size:,} byte")
    print(f"  📅 Oluşturma: {datetime.fromtimestamp(stat.st_ctime)}")
    print(f"  ✏️  Değişiklik: {datetime.fromtimestamp(stat.st_mtime)}")
    print(f"  👁️  Son erişim: {datetime.fromtimestamp(stat.st_atime)}")
    
    # İzinler (Unix/Linux/Mac için)
    if hasattr(stat, 'st_mode'):
        import stat as stat_module
        mode = stat.st_mode
        
        print(f"  🔐 İzinler:")
        print(f"    Okuma: {bool(mode & stat_module.S_IRUSR)} (Kullanıcı)")
        print(f"    Yazma: {bool(mode & stat_module.S_IWUSR)} (Kullanıcı)")
        print(f"    Çalıştırma: {bool(mode & stat_module.S_IXUSR)} (Kullanıcı)")

# Test dosyasının bilgilerini göster
test_dosya = yedek_klasor / "rapor_yedeği.txt"
dosya_bilgileri_goster(test_dosya)

# =============================================================================
# 10. GEÇİCİ DOSYA VE KLASÖRLER
# =============================================================================

print("\n=== Geçici Dosya ve Klasörler ===")

# Geçici dosya oluşturma
with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as temp_dosya:
    temp_dosya.write("Bu geçici bir dosyadır.\n")
    temp_dosya.write(f"Oluşturma zamanı: {datetime.now()}\n")
    temp_dosya_yolu = temp_dosya.name

print(f"✅ Geçici dosya oluşturuldu: {temp_dosya_yolu}")

# Geçici dosyayı oku
with open(temp_dosya_yolu, 'r', encoding='utf-8') as dosya:
    print(f"📖 Geçici dosya içeriği:\n{dosya.read()}")

# Geçici klasör oluşturma
with tempfile.TemporaryDirectory() as temp_klasor:
    temp_path = Path(temp_klasor)
    print(f"📁 Geçici klasör: {temp_path}")
    
    # Geçici klasöre dosya oluştur
    temp_test_dosya = temp_path / "test.txt"
    temp_test_dosya.write_text("Geçici klasördeki test dosyası", encoding='utf-8')
    
    print(f"📄 Geçici dosya oluşturuldu: {temp_test_dosya}")
    print(f"🗂️  Klasör içeriği: {list(temp_path.iterdir())}")
    
# Geçici klasör otomatik olarak silinir

# Manuel geçici dosya temizliği
os.unlink(temp_dosya_yolu)
print("🗑️  Geçici dosya temizlendi")

# =============================================================================
# 11. DOSYA SİSTEMİ İZLEME
# =============================================================================

print("\n=== Dosya Sistemi İzleme ===")

def klasor_istatistikleri(klasor_yolu):
    """Klasör hakkında istatistik bilgiler"""
    klasor = Path(klasor_yolu)
    
    if not klasor.exists():
        return None
    
    toplam_dosya = 0
    toplam_klasor = 0
    toplam_boyut = 0
    uzanti_dagilimi = {}
    
    try:
        for item in klasor.rglob("*"):
            if item.is_file():
                toplam_dosya += 1
                boyut = item.stat().st_size
                toplam_boyut += boyut
                
                uzanti = item.suffix.lower()
                uzanti_dagilimi[uzanti] = uzanti_dagilimi.get(uzanti, 0) + 1
            elif item.is_dir():
                toplam_klasor += 1
    
    except PermissionError:
        pass
    
    return {
        'toplam_dosya': toplam_dosya,
        'toplam_klasor': toplam_klasor,
        'toplam_boyut': toplam_boyut,
        'uzanti_dagilimi': uzanti_dagilimi
    }

# Test klasörü istatistikleri
stats = klasor_istatistikleri(test_klasor)
if stats:
    print(f"📊 {test_klasor} istatistikleri:")
    print(f"  📄 Toplam dosya: {stats['toplam_dosya']}")
    print(f"  📁 Toplam klasör: {stats['toplam_klasor']}")
    print(f"  💾 Toplam boyut: {stats['toplam_boyut']:,} byte")
    print(f"  📋 Uzantı dağılımı:")
    
    for uzanti, sayi in sorted(stats['uzanti_dagilimi'].items()):
        uzanti_adi = uzanti if uzanti else "uzantısız"
        print(f"    {uzanti_adi}: {sayi} dosya")

# =============================================================================
# 12. PLATFORM BAĞIMSIZ YOL İŞLEMLERİ
# =============================================================================

print("\n=== Platform Bağımsız Yol İşlemleri ===")

def platform_bilgisi():
    """Platform spesifik bilgiler"""
    print(f"🖥️  Platform: {sys.platform}")
    print(f"📁 Yol ayırıcı: '{os.sep}'")
    print(f"🔗 Path ayırıcı: '{os.pathsep}'")
    print(f"📐 Satır sonu: {repr(os.linesep)}")
    
    # Environment variables
    onemli_envlar = ['HOME', 'USERPROFILE', 'PATH', 'PYTHONPATH']
    print(f"🌍 Environment variables:")
    for env in onemli_envlar:
        deger = os.getenv(env, 'Bulunamadı')
        if len(deger) > 50:
            deger = deger[:47] + "..."
        print(f"  {env}: {deger}")

platform_bilgisi()

# Platform bağımsız yol oluşturma
def guvenli_yol_olustur(*parcalar):
    """Platform bağımsız yol oluşturur"""
    return Path(*parcalar)

# Test
test_yol = guvenli_yol_olustur("usr", "local", "bin", "python")
print(f"\n🛤️  Platform bağımsız yol: {test_yol}")

# =============================================================================
# 13. TEMİZLİK - TEST KLASÖRLERINI SİL
# =============================================================================

print("\n=== Temizlik ===")

# Test klasörlerini sil
test_klasorleri = [test_klasor, yedek_klasor]

for klasor in test_klasorleri:
    try:
        if klasor.exists():
            shutil.rmtree(klasor)
            print(f"🗑️  Klasör silindi: {klasor}")
    except Exception as e:
        print(f"❌ {klasor} silinemedi: {e}")

print("\n✅ Dosya yolu işlemleri öğrenildi!")
print("✅ os ve pathlib modülleri öğrenildi!")
print("✅ Klasör tarama ve dosya arama teknikleri öğrenildi!")
print("✅ Dosya kopyalama, taşıma ve izin yönetimi öğrenildi!")
print("✅ Platform bağımsız yol işlemleri öğrenildi!")