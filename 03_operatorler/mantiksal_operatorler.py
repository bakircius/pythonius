# Mantıksal Operatörler
# Boolean değerlerle mantıksal işlemler yapan operatörler

print("=== MANTIKSAL OPERATÖRLER ===\n")

print("1. TEMEL MANTIKSAL OPERATÖRLER:")
print("-" * 34)

# Test değerleri
dogru = True
yanlis = False

print(f"dogru = {dogru}, yanlis = {yanlis}\n")

# AND operatörü
print("AND (ve) operatörü:")
print(f"dogru and dogru = {dogru and dogru}")
print(f"dogru and yanlis = {dogru and yanlis}")
print(f"yanlis and dogru = {yanlis and dogru}")
print(f"yanlis and yanlis = {yanlis and yanlis}")
print("AND: Her iki koşul da True olmalı\n")

# OR operatörü  
print("OR (veya) operatörü:")
print(f"dogru or dogru = {dogru or dogru}")
print(f"dogru or yanlis = {dogru or yanlis}")
print(f"yanlis or dogru = {yanlis or dogru}")
print(f"yanlis or yanlis = {yanlis or yanlis}")
print("OR: En az bir koşul True olmalı\n")

# NOT operatörü
print("NOT (değil) operatörü:")
print(f"not dogru = {not dogru}")
print(f"not yanlis = {not yanlis}")
print("NOT: Değeri tersine çevirir\n")

print("2. KARŞILAŞTIRMA İLE MANTIK:")
print("-" * 29)

a = 10
b = 5
c = 15

print(f"a = {a}, b = {b}, c = {c}\n")

# AND ile karşılaştırma
print(f"(a > b) and (a < c) = ({a} > {b}) and ({a} < {c}) = {(a > b) and (a < c)}")
print(f"(a > b) and (a > c) = ({a} > {b}) and ({a} > {c}) = {(a > b) and (a > c)}")

# OR ile karşılaştırma
print(f"(a < b) or (a < c) = ({a} < {b}) or ({a} < {c}) = {(a < b) or (a < c)}")
print(f"(a < b) or (a > c) = ({a} < {b}) or ({a} > {c}) = {(a < b) or (a > c)}")

# NOT ile karşılaştırma
print(f"not (a > b) = not ({a} > {b}) = {not (a > b)}")

print("\n3. KARMAŞIK MANTIKSAL İFADELER:")
print("-" * 33)

yas = 20
gelir = 3000
ogrenci = True

print(f"yas = {yas}, gelir = {gelir}, ogrenci = {ogrenci}\n")

# Kredi başvuru kontrolü
kredi_uygun = (yas >= 18) and (gelir >= 2000) and (not ogrenci)
print(f"Kredi uygunluğu: {kredi_uygun}")
print("Şartlar: 18+ yaş AND 2000+ gelir AND öğrenci değil")

# İndirim kontrolü
indirim_var = (yas < 25) or (yas > 65) or ogrenci
print(f"İndirim hakkı: {indirim_var}")
print("Şartlar: 25 yaş altı OR 65 yaş üstü OR öğrenci")

print("\n4. KISA DEVRE DEĞERLENDİRME (SHORT CIRCUIT):")
print("-" * 47)

print("AND için kısa devre:")
print("False and print('Bu çalışmaz') →", end=" ")
sonuc = False and print("Bu çalışmaz")
print(f"Sonuç: {sonuc}")

print("\nOR için kısa devre:")
print("True or print('Bu da çalışmaz') →", end=" ")
sonuc = True or print("Bu da çalışmaz")
print(f"Sonuç: {sonuc}")

print("\nKısa devre açıklaması:")
print("- AND'de ilk False görülünce durur")
print("- OR'da ilk True görülünce durur")

print("\n5. MANTIK TABLOLARI:")
print("-" * 20)

print("AND Tablosu:")
print("True  and True  =", True and True)
print("True  and False =", True and False)
print("False and True  =", False and True)
print("False and False =", False and False)

print("\nOR Tablosu:")
print("True  or True  =", True or True)
print("True  or False =", True or False)
print("False or True  =", False or True)
print("False or False =", False or False)

print("\nNOT Tablosu:")
print("not True  =", not True)
print("not False =", not False)

print("\n6. ÖNCELIK SIRASI:")
print("-" * 17)

# Operatör önceliği: not > and > or
x, y, z = True, False, True

print(f"x = {x}, y = {y}, z = {z}")
print(f"x or y and z = {x or y and z}")
print("Bu şuna eşit: x or (y and z)")
print(f"x or (y and z) = {x or (y and z)}")
print(f"(x or y) and z = {(x or y) and z}")

print("\nÖncelik sırası:")
print("1. not (en yüksek)")
print("2. and")
print("3. or (en düşük)")

print("\n7. BOOLEAN DEĞERİ OLMAYAN İFADELER:")
print("-" * 36)

# Truthy ve Falsy değerler
print("Falsy değerler (False gibi davranır):")
falsy_degerler = [0, 0.0, "", [], {}, None, False]
for deger in falsy_degerler:
    print(f"bool({deger!r}) = {bool(deger)}")

print("\nTruthy değerler (True gibi davranır):")
truthy_degerler = [1, -1, 3.14, "merhaba", [1, 2], {"a": 1}, True]
for deger in truthy_degerler:
    print(f"bool({deger!r}) = {bool(deger)}")

print("\n8. PRATİK KULLANIM ÖRNEKLERİ:")
print("-" * 28)

# Kullanıcı doğrulama
kullanici_adi = "admin"
sifre = "123456"
aktif = True

giris_basarili = (kullanici_adi == "admin") and (sifre == "123456") and aktif
print(f"Giriş başarılı: {giris_basarili}")

# Sayı aralığı kontrolü
sayi = 15
aralikta = 10 <= sayi <= 20
print(f"{sayi} sayısı 10-20 aralığında: {aralikta}")

# Çoklu koşul kontrolü
hava_durumu = "güneşli"
sicaklik = 25
piknik_uygun = (hava_durumu == "güneşli") and (sicaklik > 20)
print(f"Piknik için uygun: {piknik_uygun}")

print("\n9. KARMAŞIK KOŞUL ÖRNEKLERİ:")
print("-" * 28)

# Üyelik sistemi
yas = 17
uyelik_tipi = "premium"
aktif_uye = True

# Giriş yetkisi
giris_yetkisi = ((yas >= 18) or (uyelik_tipi == "premium")) and aktif_uye
print(f"Yaş: {yas}, Üyelik: {uyelik_tipi}, Aktif: {aktif_uye}")
print(f"Giriş yetkisi: {giris_yetkisi}")

# İndirim hesaplama
toplam_fiyat = 500
uye_indirim = uyelik_tipi in ["premium", "gold"]
miktar_indirim = toplam_fiyat > 200

indirim_hakki = uye_indirim or miktar_indirim
print(f"\nToplam: {toplam_fiyat}, İndirim hakkı: {indirim_hakki}")

print("\n=== MANTIKSAL OPERATÖR ÖZETİ ===")
print("and : Her iki koşul da True olmalı")
print("or  : En az bir koşul True olmalı") 
print("not : Değeri tersine çevirir")
print()
print("Öncelik: not > and > or")
print("Kısa devre: İlk sonuç belli olunca durur")