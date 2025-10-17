"""
Python String Metodları - Detaylı Rehber

Bu dosya Python'da kullanılabilecek tüm string metodlarını
detaylı örneklerle açıklar. String manipülasyonu için
gerekli tüm metodları öğreneceğiz.
"""

# =============================================================================
# 1. ARAMA VE KONUM BULMA METODLARİ
# =============================================================================

print("=== Arama ve Konum Bulma Metodları ===")

def arama_metodlari():
    """String arama metodları"""
    
    metin = "Python programlama dili Python çok güçlüdür"
    print(f"🎯 Örnek metin: '{metin}'")
    
    print(f"\n🔍 find() metodu:")
    print(f"find('Python'): {metin.find('Python')}")
    print(f"find('Java'): {metin.find('Java')}")  # -1 döner
    print(f"find('Python', 10): {metin.find('Python', 10)}")  # 10'dan sonra ara
    print(f"find('a', 5, 15): {metin.find('a', 5, 15)}")  # 5-15 arasında ara
    
    print(f"\n🔍 rfind() metodu (sağdan arama):")
    print(f"rfind('Python'): {metin.rfind('Python')}")
    print(f"rfind('a'): {metin.rfind('a')}")
    
    print(f"\n🔍 index() metodu:")
    print(f"index('Python'): {metin.index('Python')}")
    try:
        print(f"index('Java'): {metin.index('Java')}")  # ValueError fırlatır
    except ValueError as e:
        print(f"Hata: {e}")
    
    print(f"\n🔍 rindex() metodu (sağdan index):")
    print(f"rindex('Python'): {metin.rindex('Python')}")
    
    print(f"\n🔢 count() metodu:")
    print(f"count('a'): {metin.count('a')}")
    print(f"count('Python'): {metin.count('Python')}")
    print(f"count('programlama'): {metin.count('programlama')}")
    print(f"count('a', 0, 20): {metin.count('a', 0, 20)}")  # Belirli aralıkta
    
    # Güvenli arama fonksiyonu
    def guvenli_find(metin, aranan):
        """Güvenli arama fonksiyonu"""
        pos = metin.find(aranan)
        if pos == -1:
            return f"'{aranan}' bulunamadı"
        return f"'{aranan}' {pos}. pozisyonda bulundu"
    
    print(f"\n🛡️ Güvenli arama:")
    print(guvenli_find(metin, "Python"))
    print(guvenli_find(metin, "Java"))

arama_metodlari()

# =============================================================================
# 2. KONTROL METODLARİ (BOOLEAN DÖNEN)
# =============================================================================

print("\n=== Kontrol Metodları ===")

def kontrol_metodlari():
    """Boolean dönen kontrol metodları"""
    
    print("✅ Başlangıç ve bitiş kontrolü:")
    metin = "Python Programming"
    print(f"'{metin}'")
    print(f"startswith('Python'): {metin.startswith('Python')}")
    print(f"startswith('Java'): {metin.startswith('Java')}")
    print(f"endswith('ming'): {metin.endswith('ming')}")
    print(f"endswith('Programming'): {metin.endswith('Programming')}")
    
    # Tuple ile çoklu kontrol
    print(f"startswith(('Py', 'Ja')): {metin.startswith(('Py', 'Ja'))}")
    print(f"endswith(('ing', 'tion')): {metin.endswith(('ing', 'tion'))}")
    
    print(f"\n🔤 Karakter tipi kontrolü:")
    test_strings = ["Python123", "123456", "PYTHON", "python", "Python", "   ", ""]
    
    for test in test_strings:
        print(f"\n'{test}':")
        print(f"  isalpha(): {test.isalpha()}")      # Sadece harf
        print(f"  isdigit(): {test.isdigit()}")      # Sadece rakam
        print(f"  isalnum(): {test.isalnum()}")      # Harf veya rakam
        print(f"  isupper(): {test.isupper()}")      # Büyük harf
        print(f"  islower(): {test.islower()}")      # Küçük harf
        print(f"  istitle(): {test.istitle()}")      # Title case
        print(f"  isspace(): {test.isspace()}")      # Sadece boşluk
        
    print(f"\n📏 Daha detaylı kontroller:")
    ozel_strings = ["123.45", "Python3", "user@domain.com", "Hello World"]
    
    for test in ozel_strings:
        print(f"\n'{test}':")
        print(f"  isdecimal(): {test.isdecimal()}")  # Decimal sayı
        print(f"  isnumeric(): {test.isnumeric()}")  # Numeric karakter
        print(f"  isascii(): {test.isascii()}")      # ASCII karakter
        print(f"  isprintable(): {test.isprintable()}")  # Yazdırılabilir
        print(f"  isidentifier(): {test.isidentifier()}")  # Geçerli değişken adı

kontrol_metodlari()

# =============================================================================
# 3. DÖNÜŞTÜRME METODLARİ
# =============================================================================

print("\n=== Dönüştürme Metodları ===")

def donusturme_metodlari():
    """String dönüştürme metodları"""
    
    ornek = "python programming language"
    print(f"🎯 Örnek: '{ornek}'")
    
    print(f"\n🔄 Büyük/küçük harf dönüşümleri:")
    print(f"upper(): '{ornek.upper()}'")
    print(f"lower(): '{ornek.lower()}'")
    print(f"title(): '{ornek.title()}'")
    print(f"capitalize(): '{ornek.capitalize()}'")
    print(f"swapcase(): '{ornek.swapcase()}'")
    
    # Türkçe karakterlerle
    turkce = "İstanbul'da güzel hava var"
    print(f"\n🇹🇷 Türkçe örnek: '{turkce}'")
    print(f"upper(): '{turkce.upper()}'")
    print(f"lower(): '{turkce.lower()}'")
    print(f"casefold(): '{turkce.casefold()}'")  # Gelişmiş lower()
    
    print(f"\n🧹 Temizleme metodları:")
    bosluklu = "   Python Programming   "
    print(f"Orijinal: '{bosluklu}'")
    print(f"strip(): '{bosluklu.strip()}'")
    print(f"lstrip(): '{bosluklu.lstrip()}'")
    print(f"rstrip(): '{bosluklu.rstrip()}'")
    
    # Özel karakterleri temizleme
    ozel_karakter = "***Python***"
    print(f"\nÖzel karakter: '{ozel_karakter}'")
    print(f"strip('*'): '{ozel_karakter.strip('*')}'")
    print(f"lstrip('*'): '{ozel_karakter.lstrip('*')}'")
    print(f"rstrip('*'): '{ozel_karakter.rstrip('*')}'")
    
    # Çoklu karakter temizleme
    karisik = ".,;Python Programming!?."
    print(f"Karışık: '{karisik}'")
    print(f"strip('.,;!?'): '{karisik.strip('.,;!?')}'")

donusturme_metodlari()

# =============================================================================
# 4. DEĞİŞTİRME METODLARİ
# =============================================================================

print("\n=== Değiştirme Metodları ===")

def degistirme_metodlari():
    """String değiştirme metodları"""
    
    metin = "Python programming with Python is fun"
    print(f"🎯 Örnek: '{metin}'")
    
    print(f"\n🔄 replace() metodu:")
    print(f"replace('Python', 'Java'): '{metin.replace('Python', 'Java')}'")
    print(f"replace('Python', 'Java', 1): '{metin.replace('Python', 'Java', 1)}'")
    print(f"replace('with', 'using'): '{metin.replace('with', 'using')}'")
    
    # Çoklu değiştirme
    def coklu_replace(metin, degisimler):
        """Çoklu değiştirme işlemi"""
        for eski, yeni in degisimler.items():
            metin = metin.replace(eski, yeni)
        return metin
    
    degisimler = {
        'Python': 'Java',
        'programming': 'coding',
        'fun': 'awesome'
    }
    
    print(f"\nÇoklu değiştirme:")
    print(f"Sonuç: '{coklu_replace(metin, degisimler)}'")
    
    print(f"\n📋 translate() metodu:")
    # translate() için çeviri tablosu oluşturma
    
    # Basit çeviri
    translation_table = str.maketrans('aeiou', '12345')
    test_metin = "Hello World"
    print(f"'{test_metin}' -> '{test_metin.translate(translation_table)}'")
    
    # Karakter silme
    silme_tablosu = str.maketrans('', '', 'aeiou')  # Sesli harfleri sil
    print(f"Sesli harf silme: '{test_metin.translate(silme_tablosu)}'")
    
    # Türkçe karakter dönüşümü
    tr_to_en = str.maketrans('çğıöşüÇĞIÖŞÜ', 'cgiosuCGIOSU')
    tr_metin = "Çok güçlü bir dil"
    print(f"TR->EN: '{tr_metin}' -> '{tr_metin.translate(tr_to_en)}'")

degistirme_metodlari()

# =============================================================================
# 5. BÖLME VE BİRLEŞTİRME METODLARİ
# =============================================================================

print("\n=== Bölme ve Birleştirme Metodları ===")

def bolme_birlestirme_metodlari():
    """Bölme ve birleştirme metodları"""
    
    print("✂️ split() metodları:")
    metin = "elma,armut,kiraz,şeftali"
    print(f"Örnek: '{metin}'")
    print(f"split(','): {metin.split(',')}")
    print(f"split(',', 2): {metin.split(',', 2)}")  # Maksimum 2 bölme
    
    # Boşluk ile bölme
    cumle = "Python çok güçlü bir programlama dilidir"
    print(f"\nCümle: '{cumle}'")
    print(f"split(): {cumle.split()}")
    print(f"split(' ', 3): {cumle.split(' ', 3)}")
    
    print(f"\n✂️ rsplit() metodu (sağdan bölme):")
    dosya_yolu = "/home/user/documents/file.txt"
    print(f"Dosya yolu: '{dosya_yolu}'")
    print(f"split('/'): {dosya_yolu.split('/')}")
    print(f"rsplit('/', 1): {dosya_yolu.rsplit('/', 1)}")  # Son bölmeyi al
    
    print(f"\n✂️ partition() metodları:")
    email = "kullanici@domain.com"
    print(f"Email: '{email}'")
    before, sep, after = email.partition('@')
    print(f"partition('@'): ('{before}', '{sep}', '{after}')")
    
    rpartition_result = email.rpartition('.')
    print(f"rpartition('.'): {rpartition_result}")
    
    print(f"\n✂️ splitlines() metodu:")
    cok_satirli = """Birinci satır
İkinci satır
Üçüncü satır"""
    
    print(f"splitlines(): {cok_satirli.splitlines()}")
    print(f"splitlines(True): {cok_satirli.splitlines(True)}")  # Line break'leri koru
    
    print(f"\n🔗 join() metodu:")
    kelimeler = ["Python", "çok", "güçlü", "bir", "dildir"]
    print(f"Kelimeler: {kelimeler}")
    print(f"' '.join(): '{' '.join(kelimeler)}'")
    print(f"'-'.join(): '{'-'.join(kelimeler)}'")
    print(f"', '.join(): '{', '.join(kelimeler)}'")
    print(f"''.join(): '{' '.join(kelimeler)}'")
    
    # Sayıları birleştirme
    sayilar = [1, 2, 3, 4, 5]
    str_sayilar = [str(s) for s in sayilar]
    print(f"\nSayılar: {sayilar}")
    print(f"String join: '{'-'.join(str_sayilar)}'")

bolme_birlestirme_metodlari()

# =============================================================================
# 6. HİZALAMA VE DOLDURMA METODLARİ
# =============================================================================

print("\n=== Hizalama ve Doldurma Metodları ===")

def hizalama_metodlari():
    """String hizalama ve doldurma metodları"""
    
    metin = "Python"
    print(f"🎯 Örnek: '{metin}' (uzunluk: {len(metin)})")
    
    print(f"\n📐 center() metodu:")
    print(f"center(20): '{metin.center(20)}'")
    print(f"center(20, '*'): '{metin.center(20, '*')}'")
    print(f"center(20, '-'): '{metin.center(20, '-')}'")
    
    print(f"\n📐 ljust() metodu (sola yasla):")
    print(f"ljust(20): '{metin.ljust(20)}'")
    print(f"ljust(20, '.'): '{metin.ljust(20, '.')}'")
    
    print(f"\n📐 rjust() metodu (sağa yasla):")
    print(f"rjust(20): '{metin.rjust(20)}'")
    print(f"rjust(20, '.'): '{metin.rjust(20, '.')}'")
    
    print(f"\n📐 zfill() metodu (sıfırla doldur):")
    sayilar = ["42", "123", "7"]
    for sayi in sayilar:
        print(f"'{sayi}'.zfill(5): '{sayi.zfill(5)}'")
    
    # Negatif sayılar
    negatif = "-42"
    print(f"'{negatif}'.zfill(5): '{negatif.zfill(5)}'")
    
    print(f"\n📋 Tablo formatı örneği:")
    products = [
        ("Laptop", 15000, 5),
        ("Mouse", 50, 25),
        ("Keyboard", 200, 12)
    ]
    
    print("┌──────────┬─────────┬────────┐")
    print("│ Ürün     │ Fiyat   │ Stok   │")
    print("├──────────┼─────────┼────────┤")
    
    for name, price, stock in products:
        name_str = name.ljust(8)
        price_str = str(price).rjust(7)
        stock_str = str(stock).rjust(6)
        print(f"│ {name_str} │ {price_str} │ {stock_str} │")
    
    print("└──────────┴─────────┴────────┘")

hizalama_metodlari()

# =============================================================================
# 7. ENCODING/DECODING METODLARİ
# =============================================================================

print("\n=== Encoding/Decoding Metodları ===")

def encoding_metodlari():
    """String encoding ve decoding metodları"""
    
    turkce_metin = "Türkçe karakterler: çğıöşü"
    print(f"🇹🇷 Türkçe metin: '{turkce_metin}'")
    
    print(f"\n📦 encode() metodu:")
    utf8_bytes = turkce_metin.encode('utf-8')
    print(f"UTF-8: {utf8_bytes}")
    
    latin1_bytes = turkce_metin.encode('latin-1', errors='ignore')
    print(f"Latin-1 (ignore): {latin1_bytes}")
    
    ascii_bytes = turkce_metin.encode('ascii', errors='replace')
    print(f"ASCII (replace): {ascii_bytes}")
    
    ascii_xmlcharrefreplace = turkce_metin.encode('ascii', errors='xmlcharrefreplace')
    print(f"ASCII (xmlcharrefreplace): {ascii_xmlcharrefreplace}")
    
    print(f"\n📦 decode() byte metodları:")
    # bytes objesi oluştur
    byte_data = utf8_bytes
    
    decoded_utf8 = byte_data.decode('utf-8')
    print(f"UTF-8 decode: '{decoded_utf8}'")
    
    # Hatalı decoding
    try:
        decoded_ascii = byte_data.decode('ascii')
    except UnicodeDecodeError as e:
        print(f"ASCII decode hatası: {e}")
    
    # Hatalı decoding ile error handling
    decoded_ascii_ignore = byte_data.decode('ascii', errors='ignore')
    print(f"ASCII decode (ignore): '{decoded_ascii_ignore}'")
    
    decoded_ascii_replace = byte_data.decode('ascii', errors='replace')
    print(f"ASCII decode (replace): '{decoded_ascii_replace}'")
    
    print(f"\n🔤 expandtabs() metodu:")
    tab_metin = "Python\tProgramming\tLanguage"
    print(f"Tab'lı metin: '{tab_metin}'")
    print(f"expandtabs(): '{tab_metin.expandtabs()}'")
    print(f"expandtabs(4): '{tab_metin.expandtabs(4)}'")
    print(f"expandtabs(8): '{tab_metin.expandtabs(8)}'")

encoding_metodlari()

# =============================================================================
# 8. ÖZELLEŞTİRİLMİŞ STRİNG METODLARİ
# =============================================================================

print("\n=== Özelleştirilmiş String Metodları ===")

def ozellestirilmis_metodlar():
    """Özelleştirilmiş string işlemleri"""
    
    print("🛠️ Özel String Sınıfı:")
    
    class GelismisString(str):
        """Gelişmiş string sınıfı"""
        
        def tersle(self):
            """String'i ters çevir"""
            return self[::-1]
        
        def kelime_sayisi(self):
            """Kelime sayısını döner"""
            return len(self.split())
        
        def buyuk_harf_sayisi(self):
            """Büyük harf sayısını döner"""
            return sum(1 for c in self if c.isupper())
        
        def kucuk_harf_sayisi(self):
            """Küçük harf sayısını döner"""
            return sum(1 for c in self if c.islower())
        
        def rakam_sayisi(self):
            """Rakam sayısını döner"""
            return sum(1 for c in self if c.isdigit())
        
        def ozel_karakter_sayisi(self):
            """Özel karakter sayısını döner"""
            return sum(1 for c in self if not c.isalnum() and not c.isspace())
        
        def temizle(self):
            """Metni temizle"""
            import re
            # Çoklu boşlukları tek boşluğa çevir
            temiz = re.sub(r'\s+', ' ', self.strip())
            return GelismisString(temiz)
        
        def baslik_yap(self):
            """Her kelimenin ilk harfini büyük yap"""
            return GelismisString(' '.join(word.capitalize() for word in self.split()))
        
        def sadece_harfler(self):
            """Sadece harfleri döner"""
            return GelismisString(''.join(c for c in self if c.isalpha()))
        
        def sadece_rakamlar(self):
            """Sadece rakamları döner"""
            return GelismisString(''.join(c for c in self if c.isdigit()))
        
        def istatistik(self):
            """String istatistiklerini döner"""
            return {
                'toplam_karakter': len(self),
                'kelime_sayisi': self.kelime_sayisi(),
                'buyuk_harf': self.buyuk_harf_sayisi(),
                'kucuk_harf': self.kucuk_harf_sayisi(),
                'rakam': self.rakam_sayisi(),
                'ozel_karakter': self.ozel_karakter_sayisi(),
                'bosluk': self.count(' ')
            }
    
    # Test
    test_metin = GelismisString("  Python Programming 123!!!  ")
    print(f"Test metni: '{test_metin}'")
    
    print(f"\n📊 İstatistikler:")
    stats = test_metin.istatistik()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    print(f"\n🔧 Özel metodlar:")
    print(f"tersle(): '{test_metin.tersle()}'")
    print(f"temizle(): '{test_metin.temizle()}'")
    print(f"baslik_yap(): '{test_metin.baslik_yap()}'")
    print(f"sadece_harfler(): '{test_metin.sadece_harfler()}'")
    print(f"sadece_rakamlar(): '{test_metin.sadece_rakamlar()}'")

ozellestirilmis_metodlar()

# =============================================================================
# 9. STRİNG METOD ZİNCİRLEME
# =============================================================================

print("\n=== String Metod Zincirleme ===")

def metod_zincirleme():
    """String metodlarını zincirleme"""
    
    print("🔗 Metod Zincirleme Örnekleri:")
    
    kirli_metin = "   PYTHON programming LANGuage   "
    print(f"Orijinal: '{kirli_metin}'")
    
    # Basit zincirleme
    temiz1 = kirli_metin.strip().lower().title()
    print(f"strip().lower().title(): '{temiz1}'")
    
    # Kompleks zincirleme
    email = "  USER@DOMAIN.COM  "
    temiz_email = email.strip().lower().replace('@', ' at ').replace('.', ' dot ')
    print(f"Email dönüşümü: '{email}' -> '{temiz_email}'")
    
    # Uzun zincirleme
    metin = "python,java,javascript,c++,go"
    sonuc = metin.upper().replace(',', ' | ').center(50, '=')
    print(f"Uzun zincirleme: '{sonuc}'")
    
    print(f"\n🔄 Fonksiyonel yaklaşım:")
    
    def pipeline(text, *functions):
        """Fonksiyon pipeline'ı"""
        for func in functions:
            text = func(text)
        return text
    
    # Pipeline fonksiyonları
    ornek = "  hello WORLD python  "
    
    result = pipeline(
        ornek,
        str.strip,
        str.lower,
        lambda x: x.replace(' ', '_'),
        str.upper
    )
    
    print(f"Pipeline sonucu: '{ornek}' -> '{result}'")
    
    # Özel pipeline sınıfı
    class StringPipeline:
        def __init__(self, text):
            self.text = text
        
        def strip(self):
            self.text = self.text.strip()
            return self
        
        def lower(self):
            self.text = self.text.lower()
            return self
        
        def upper(self):
            self.text = self.text.upper()
            return self
        
        def replace(self, old, new):
            self.text = self.text.replace(old, new)
            return self
        
        def title(self):
            self.text = self.text.title()
            return self
        
        def result(self):
            return self.text
        
        def __str__(self):
            return self.text
    
    # Pipeline kullanımı
    test = "  python programming  "
    result = (StringPipeline(test)
              .strip()
              .title()
              .replace(' ', '_')
              .lower()
              .result())
    
    print(f"StringPipeline: '{test}' -> '{result}'")

metod_zincirleme()

# =============================================================================
# 10. PERFORMANS KARŞILAŞTIRMASI
# =============================================================================

print("\n=== String Metodları Performance ===")

def string_performance_karsilastirma():
    """String metodlarının performance karşılaştırması"""
    
    import time
    import random
    import string
    
    # Test verisi oluştur
    def random_string(length):
        return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=length))
    
    test_strings = [random_string(1000) for _ in range(100)]
    
    print("⚡ Performance Testleri:")
    
    # Test 1: Arama işlemleri
    print("\n1. Arama işlemleri:")
    
    start = time.perf_counter()
    for text in test_strings:
        'python' in text
    in_time = time.perf_counter() - start
    
    start = time.perf_counter()
    for text in test_strings:
        text.find('python') != -1
    find_time = time.perf_counter() - start
    
    print(f"  'in' operatörü: {in_time:.6f}s")
    print(f"  find() metodu: {find_time:.6f}s")
    print(f"  'in' {find_time/in_time:.1f}x daha hızlı")
    
    # Test 2: String birleştirme
    print("\n2. String birleştirme:")
    words = ['python', 'programming', 'language'] * 100
    
    start = time.perf_counter()
    result1 = ''
    for word in words:
        result1 += word + ' '
    plus_time = time.perf_counter() - start
    
    start = time.perf_counter()
    result2 = ' '.join(words)
    join_time = time.perf_counter() - start
    
    print(f"  += operatörü: {plus_time:.6f}s")
    print(f"  join() metodu: {join_time:.6f}s")
    print(f"  join() {plus_time/join_time:.1f}x daha hızlı")
    
    # Test 3: Büyük/küçük harf dönüşümü
    print("\n3. Case dönüşümü:")
    
    start = time.perf_counter()
    for text in test_strings:
        text.lower()
    lower_time = time.perf_counter() - start
    
    start = time.perf_counter()
    for text in test_strings:
        text.casefold()
    casefold_time = time.perf_counter() - start
    
    print(f"  lower(): {lower_time:.6f}s")
    print(f"  casefold(): {casefold_time:.6f}s")

string_performance_karsilastirma()

print("\n💡 String Metodları İpuçları:")
print("✅ join() kullanarak string birleştirin")
print("✅ 'in' operatörü ile arama yapın")
print("✅ startswith()/endswith() kullanın")
print("✅ strip() ile boşlukları temizleyin")
print("✅ Metodları zincirleme yapabilirsiniz")
print("✅ casefold() uluslararası karakterler için")
print("✅ translate() çoklu karakter değişimi için")

print("\n⚠️ Dikkat Edilecek Noktalar:")
print("• find() -1 döner, index() hata fırlatır")
print("• split() ve rsplit() farklı sonuçlar verebilir")
print("• Unicode karakterlerle encode/decode dikkatli olun")
print("• Performance için uygun metodu seçin")
print("• String immutable - her işlem yeni string oluşturur")

print("\n✅ Tüm string metodları öğrenildi!")
print("✅ Performance optimizasyonları öğrenildi!")
print("✅ Metod zincirleme teknikleri öğrenildi!")
print("✅ Özelleştirilmiş string sınıfları oluşturuldu!")