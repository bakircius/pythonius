# Tip Dönüşümleri (Type Casting)
# Veri tiplerini birbirine dönüştürme örnekleri

print("=== TİP DÖNÜŞÜMLERİ (TYPE CASTING) ===\n")

print("1. STRING'DEN SAYIYA DÖNÜŞÜM:")
print("-" * 35)

# String'den int'e dönüşüm
str_sayi = "123"
int_sayi = int(str_sayi)
print(f"String: '{str_sayi}' → int: {int_sayi}")
print(f"Tip değişimi: {type(str_sayi)} → {type(int_sayi)}")

# String'den float'a dönüşüm
str_ondalik = "3.14"
float_ondalik = float(str_ondalik)
print(f"String: '{str_ondalik}' → float: {float_ondalik}")

# Hatalı dönüşüm örneği (yorum olarak)
# hata = int("merhaba")  # ValueError verir!

print("\n2. SAYIDAN STRING'E DÖNÜŞÜM:")
print("-" * 35)

# Int'den string'e
sayi = 456
str_sayi = str(sayi)
print(f"int: {sayi} → String: '{str_sayi}'")

# Float'dan string'e
ondalik = 2.718
str_ondalik = str(ondalik)
print(f"float: {ondalik} → String: '{str_ondalik}'")

print("\n3. SAYILAR ARASI DÖNÜŞÜM:")
print("-" * 30)

# Int'den float'a
tam_sayi = 10
ondalik_sayi = float(tam_sayi)
print(f"int: {tam_sayi} → float: {ondalik_sayi}")

# Float'dan int'e (ondalık kısmı atılır!)
ondalik = 3.99
tam_sayi = int(ondalik)
print(f"float: {ondalik} → int: {tam_sayi}")
print("DİKKAT: Ondalık kısım atıldı, yuvarlanmadı!")

print("\n4. BOOLEAN DÖNÜŞÜMLER:")
print("-" * 25)

# Sayılardan boolean'a
print("Sayılardan bool'a:")
print(f"bool(0) = {bool(0)}")          # False
print(f"bool(1) = {bool(1)}")          # True
print(f"bool(-5) = {bool(-5)}")        # True
print(f"bool(0.0) = {bool(0.0)}")      # False
print(f"bool(3.14) = {bool(3.14)}")    # True

# String'lerden boolean'a
print("\nString'lerden bool'a:")
print(f"bool('') = {bool('')}")            # False (boş string)
print(f"bool('merhaba') = {bool('merhaba')}")  # True
print(f"bool('0') = {bool('0')}")          # True (string olarak '0')
print(f"bool('False') = {bool('False')}")  # True (string olarak 'False')

# Boolean'dan diğer tiplere
print("\nBool'dan diğer tiplere:")
print(f"int(True) = {int(True)}")      # 1
print(f"int(False) = {int(False)}")    # 0
print(f"str(True) = '{str(True)}'")    # 'True'
print(f"str(False) = '{str(False)}'")  # 'False'

print("\n5. KULLANICI GİRİŞİ DÖNÜŞÜMLERİ:")
print("-" * 35)

# input() her zaman string döner, dönüştürmek gerekir
print("Kullanıcı girişi örnekleri:")
print("# Kullanıcıdan yaş al")
print("yas_str = input('Yaşınız: ')")
print("yas_int = int(yas_str)")
print()
print("# Kısa yolu")
print("yas = int(input('Yaşınız: '))")

print("\n6. GÜVENLİ TİP DÖNÜŞÜMÜ:")
print("-" * 28)

# Hata kontrolü ile güvenli dönüşüm
def guvenli_int_donusumu(deger):
    """String'i güvenli şekilde int'e çevirir"""
    try:
        return int(deger)
    except ValueError:
        print(f"'{deger}' sayıya dönüştürülemez!")
        return None

# Test örnekleri
test_degerleri = ["123", "3.14", "merhaba", "0", "-45"]

print("Güvenli dönüşüm testleri:")
for deger in test_degerleri:
    sonuc = guvenli_int_donusumu(deger)
    print(f"'{deger}' → {sonuc}")

print("\n7. KARMAŞIK DÖNÜŞÜM ÖRNEKLERİ:")
print("-" * 32)

# Birden fazla dönüşüm
metin_sayi = "42"
sonuc = str(int(metin_sayi) * 2)
print(f"'{metin_sayi}' → int → *2 → str = '{sonuc}'")

# Liste elemanlarını dönüştürme
str_sayilar = ["1", "2", "3", "4", "5"]
int_sayilar = [int(x) for x in str_sayilar]
print(f"String liste: {str_sayilar}")
print(f"Int liste: {int_sayilar}")

print("\n=== TİP DÖNÜŞÜM ÖZETİ ===")
print("int(x)   : x'i tam sayıya çevir")
print("float(x) : x'i ondalıklı sayıya çevir")
print("str(x)   : x'i string'e çevir")
print("bool(x)  : x'i boolean'a çevir")
print()
print("DİKKAT:")
print("- input() her zaman string döner")
print("- Geçersiz dönüşümler ValueError hatası verir")
print("- float→int dönüşümünde ondalık kısım atılır")