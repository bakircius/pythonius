# Temel Değişken Kullanımı
# Bu dosya Python'da değişken tanımlama ve kullanma örneklerini gösterir

print("=== DEĞİŞKEN TANIMLAMA ===\n")

# Değişken tanımlama (atama operatörü =)
isim = "Ahmet"
yas = 25
boy = 1.75
ogrenci_mi = True

print("Tanımlanan değişkenler:")
print(f"İsim: {isim}")
print(f"Yaş: {yas}")
print(f"Boy: {boy}")
print(f"Öğrenci mi: {ogrenci_mi}")

print("\n=== DEĞİŞKEN İSİMLENDİRME KURALLARI ===\n")

# Doğru değişken isimleri
ad_soyad = "Ali Veli"
sayi_1 = 10
_ozel_degisken = "gizli"
SABIT_DEGER = 100

print("Doğru değişken isimleri:")
print(f"ad_soyad: {ad_soyad}")
print(f"sayi_1: {sayi_1}")
print(f"_ozel_degisken: {_ozel_degisken}")
print(f"SABIT_DEGER: {SABIT_DEGER}")

# Yanlış örnekler (yorum olarak)
# 2sayi = 10        # Sayı ile başlayamaz
# ad-soyad = "test" # Tire karakteri kullanılamaz
# class = "sınıf"   # Anahtar kelime kullanılamaz

print("\n=== ÇOKLU DEĞİŞKEN ATAMA ===\n")

# Aynı anda birden fazla değişken tanımlama
x, y, z = 10, 20, 30
print(f"x = {x}, y = {y}, z = {z}")

# Aynı değeri birden fazla değişkene atama
a = b = c = 5
print(f"a = {a}, b = {b}, c = {c}")

# Değişken değerlerini değiştirme
print("\nDeğişken değerlerini değiştirme:")
sayi = 100
print(f"İlk değer: {sayi}")
sayi = sayi + 50
print(f"Değişen değer: {sayi}")

# Değişken değerlerini takas etme
print("\nDeğişken takas etme:")
x, y = 10, 20
print(f"Önce: x = {x}, y = {y}")
x, y = y, x  # Python'da kolay takas
print(f"Sonra: x = {x}, y = {y}")

print("\n=== DEĞİŞKEN SCOPE (KAPSAM) ===\n")

# Global değişken
global_degisken = "Ben globalim"

def fonksiyon_ornegi():
    # Local değişken
    local_degisken = "Ben lokalim"
    print(f"Fonksiyon içinde: {global_degisken}")
    print(f"Fonksiyon içinde: {local_degisken}")

fonksiyon_ornegi()
print(f"Fonksiyon dışında: {global_degisken}")
# print(local_degisken)  # Bu hata verir, çünkü local değişken