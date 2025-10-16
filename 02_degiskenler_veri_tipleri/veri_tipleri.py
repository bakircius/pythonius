# Veri Tiplerinin Detayları
# Python'daki temel veri tiplerinin özelliklerini gösterir

print("=== PYTHON VERİ TİPLERİ ===\n")

# 1. INTEGER (Tam Sayı)
print("1. INTEGER (int) - Tam Sayılar:")
pozitif_sayi = 42
negatif_sayi = -17
sifir = 0

print(f"   Pozitif sayı: {pozitif_sayi} (tip: {type(pozitif_sayi)})")
print(f"   Negatif sayı: {negatif_sayi} (tip: {type(negatif_sayi)})")
print(f"   Sıfır: {sifir} (tip: {type(sifir)})")

# Integer'ların özel özellikleri
buyuk_sayi = 123456789012345678901234567890
print(f"   Büyük sayı: {buyuk_sayi}")
print("   Python'da integer sınırı yoktur!")

print("\n" + "="*50 + "\n")

# 2. FLOAT (Ondalıklı Sayı)
print("2. FLOAT (float) - Ondalıklı Sayılar:")
pi = 3.14159
e = 2.71828
bilimsel_notasyon = 1.5e-4  # 0.00015

print(f"   Pi sayısı: {pi} (tip: {type(pi)})")
print(f"   E sayısı: {e} (tip: {type(e)})")
print(f"   Bilimsel notasyon: {bilimsel_notasyon} (tip: {type(bilimsel_notasyon)})")

# Float hassasiyet problemi
print(f"   0.1 + 0.2 = {0.1 + 0.2}")
print("   Float hassasiyet sorunu var!")

print("\n" + "="*50 + "\n")

# 3. STRING (Metin)
print("3. STRING (str) - Metinler:")
tek_tirnak = 'Merhaba'
cift_tirnak = "Dünya"
uclu_tirnak = """Bu çok satırlı
bir metin örneğidir"""

print(f"   Tek tırnak: {tek_tirnak} (tip: {type(tek_tirnak)})")
print(f"   Çift tırnak: {cift_tirnak} (tip: {type(cift_tirnak)})")
print(f"   Üçlü tırnak: {uclu_tirnak} (tip: {type(uclu_tirnak)})")

# String özellikleri
print(f"   String uzunluğu: {len(tek_tirnak)}")
print(f"   Büyük harf: {tek_tirnak.upper()}")
print(f"   Küçük harf: {cift_tirnak.lower()}")

print("\n" + "="*50 + "\n")

# 4. BOOLEAN (Mantıksal)
print("4. BOOLEAN (bool) - Mantıksal Değerler:")
dogru = True
yanlis = False

print(f"   Doğru: {dogru} (tip: {type(dogru)})")
print(f"   Yanlış: {yanlis} (tip: {type(yanlis)})")

# Boolean dönüşümleri
print("   Boolean dönüşümleri:")
print(f"   bool(1): {bool(1)}")
print(f"   bool(0): {bool(0)}")
print(f"   bool('merhaba'): {bool('merhaba')}")
print(f"   bool(''): {bool('')}")
print(f"   bool([1,2,3]): {bool([1,2,3])}")
print(f"   bool([]): {bool([])}")

print("\n" + "="*50 + "\n")

# 5. NONE (Hiçlik)
print("5. NONE - Hiçlik Değeri:")
hiclik = None
print(f"   None değeri: {hiclik} (tip: {type(hiclik)})")
print("   None, 'değer yok' anlamına gelir")

# None kullanım örnekleri
def fonksiyon():
    pass  # Hiçbir şey yapmaz

sonuc = fonksiyon()
print(f"   Fonksiyon sonucu: {sonuc}")

print("\n=== VERİ TİPİ KONTROLÜ ===\n")

# type() fonksiyonu ile tip kontrolü
deger = 42
print(f"type({deger}) = {type(deger)}")

# isinstance() fonksiyonu ile tip kontrolü
print(f"isinstance({deger}, int) = {isinstance(deger, int)}")
print(f"isinstance({deger}, str) = {isinstance(deger, str)}")

# Birden fazla tip kontrolü
print(f"isinstance({deger}, (int, float)) = {isinstance(deger, (int, float))}")

print("\n=== VERİ TİPİ ÖZETİ ===")
print("int    : Tam sayılar (1, -5, 100)")
print("float  : Ondalıklı sayılar (3.14, -2.5)")
print("str    : Metinler ('merhaba', \"dünya\")")
print("bool   : Mantıksal değerler (True, False)")
print("None   : Hiçlik değeri")