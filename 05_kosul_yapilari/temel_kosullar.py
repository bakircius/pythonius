# Temel Koşullar
# if, elif, else yapılarının kullanımı

print("=== TEMEL KOŞUL YAPILARI ===\n")

print("1. BASIT IF YAPISI:")
print("-" * 18)

# Temel if kullanımı
yas = 18
print(f"Yaş: {yas}")

if yas >= 18:
    print("Reşitsiniz!")

print("Program devam ediyor...\n")

# Başka if örnekleri
sayi = 10
print(f"Sayı: {sayi}")

if sayi > 0:
    print("Sayı pozitiftir")

if sayi % 2 == 0:
    print("Sayı çifttir")

print("\n2. IF-ELSE YAPISI:")
print("-" * 17)

# if-else kullanımı
yas = 16
print(f"Yaş: {yas}")

if yas >= 18:
    print("Reşitsiniz")
else:
    print("Reşit değilsiniz")

# Başka if-else örnekleri
sayi = -5
print(f"\nSayı: {sayi}")

if sayi >= 0:
    print("Sayı pozitif veya sıfır")
else:
    print("Sayı negatif")

# Çift/tek kontrolü
sayi = 7
print(f"\nSayı: {sayi}")

if sayi % 2 == 0:
    print("Çift sayı")
else:
    print("Tek sayı")

print("\n3. IF-ELIF-ELSE YAPISI:")
print("-" * 22)

# Not değerlendirme
not_degeri = 85
print(f"Not: {not_degeri}")

if not_degeri >= 90:
    print("Harf notu: AA")
elif not_degeri >= 85:
    print("Harf notu: BA")
elif not_degeri >= 80:
    print("Harf notu: BB")
elif not_degeri >= 75:
    print("Harf notu: CB")
elif not_degeri >= 70:
    print("Harf notu: CC")
elif not_degeri >= 65:
    print("Harf notu: DC")
elif not_degeri >= 60:
    print("Harf notu: DD")
else:
    print("Harf notu: FF")

# Mevsim belirleme
ay = 7
print(f"\nAy: {ay}")

if ay in [12, 1, 2]:
    print("Mevsim: Kış")
elif ay in [3, 4, 5]:
    print("Mevsim: İlkbahar")
elif ay in [6, 7, 8]:
    print("Mevsim: Yaz")
elif ay in [9, 10, 11]:
    print("Mevsim: Sonbahar")
else:
    print("Geçersiz ay numarası")

print("\n4. ÇOKLU KOŞUL KONTROLLERI:")
print("-" * 27)

# Yaş ve gelir kontrolü
yas = 25
gelir = 3000
print(f"Yaş: {yas}, Gelir: {gelir}")

if yas >= 18 and gelir >= 2000:
    print("Kredi başvurusuna uygunsunuz")
elif yas >= 18:
    print("Yaş uygun ama gelir yetersiz")
elif gelir >= 2000:
    print("Gelir uygun ama yaş küçük")
else:
    print("Ne yaş ne de gelir uygun")

# Öğrenci indirimi
yas = 19
ogrenci = True
print(f"\nYaş: {yas}, Öğrenci: {ogrenci}")

if yas < 25 or ogrenci:
    print("Öğrenci indirimi alabilirsiniz")
else:
    print("İndirim hakkınız bulunmuyor")

print("\n5. KOŞUL ÖNCELİĞİ:")
print("-" * 17)

# Koşulların sırası önemli
puan = 95
print(f"Puan: {puan}")

# Doğru sıralama (büyükten küçüğe)
if puan >= 90:
    print("Mükemmel performans")
elif puan >= 80:
    print("İyi performans")
elif puan >= 70:
    print("Orta performans")
else:
    print("Geliştirilmesi gereken performans")

print("\n6. BOOLEAN KOŞULLAR:")
print("-" * 19)

# Boolean değişkenlerle
aktif = True
premium = False
print(f"Aktif: {aktif}, Premium: {premium}")

if aktif:
    print("Hesap aktif")
    if premium:
        print("Premium özelliklere erişim var")
    else:
        print("Temel özelliklere erişim var")
else:
    print("Hesap aktif değil")

# Boolean kombinasyonlar
yasakli = False
sureli_yasakli = False
print(f"\nYasaklı: {yasakli}, Süreli yasaklı: {sureli_yasakli}")

if not yasakli and not sureli_yasakli:
    print("Giriş izni var")
elif sureli_yasakli:
    print("Süreli yasak aktif")
else:
    print("Kalıcı yasak var")

print("\n7. STRING KOŞULLARI:")
print("-" * 18)

# String karşılaştırma
kullanici_tipi = "admin"
print(f"Kullanıcı tipi: {kullanici_tipi}")

if kullanici_tipi == "admin":
    print("Yönetici yetkilerine sahipsiniz")
elif kullanici_tipi == "moderator":
    print("Moderatör yetkileriniz var")
elif kullanici_tipi == "user":
    print("Normal kullanıcı yetkileriniz var")
else:
    print("Tanımsız kullanıcı tipi")

# String içerik kontrolü
email = "user@gmail.com"
print(f"\nE-mail: {email}")

if "@gmail.com" in email:
    print("Gmail kullanıcısı")
elif "@hotmail.com" in email:
    print("Hotmail kullanıcısı")
elif "@" in email:
    print("Geçerli e-mail formatı")
else:
    print("Geçersiz e-mail")

print("\n8. NONE KONTROLLERI:")
print("-" * 17)

# None değer kontrolü
deger = None
print(f"Değer: {deger}")

if deger is None:
    print("Değer tanımlanmamış")
else:
    print(f"Değer: {deger}")

# Liste boş kontrolü
liste = []
print(f"\nListe: {liste}")

if not liste:  # Boş liste False değerine eşit
    print("Liste boş")
else:
    print(f"Liste: {liste}")

print("\n9. SAYI ARALIK KONTROLLERI:")
print("-" * 26)

# Aralık kontrolü
sayi = 15
print(f"Sayı: {sayi}")

if 10 <= sayi <= 20:
    print("Sayı 10-20 aralığında")
elif 1 <= sayi < 10:
    print("Sayı 1-9 aralığında")
elif 21 <= sayi <= 100:
    print("Sayı 21-100 aralığında")
else:
    print("Sayı belirlenen aralıklarda değil")

# Sıcaklık değerlendirmesi
sicaklik = 25
print(f"\nSıcaklık: {sicaklik}°C")

if sicaklik < 0:
    print("Donuyor")
elif sicaklik < 10:
    print("Çok soğuk")
elif sicaklik < 20:
    print("Soğuk")
elif sicaklik < 30:
    print("Ilık")
elif sicaklik < 40:
    print("Sıcak")
else:
    print("Çok sıcak")

print("\n10. PRATİK ÖRNEKLER:")
print("-" * 19)

# Şifre kontrolü
sifre = "Python123"
print(f"Şifre: {sifre}")

if len(sifre) >= 8:
    if any(c.isupper() for c in sifre):
        if any(c.islower() for c in sifre):
            if any(c.isdigit() for c in sifre):
                print("Güçlü şifre ✓")
            else:
                print("Şifrede rakam olmalı")
        else:
            print("Şifrede küçük harf olmalı")
    else:
        print("Şifrede büyük harf olmalı")
else:
    print("Şifre en az 8 karakter olmalı")

# BMI hesaplama ve değerlendirme
boy = 1.75  # metre
kilo = 70   # kg
bmi = kilo / (boy ** 2)

print(f"\nBoy: {boy}m, Kilo: {kilo}kg")
print(f"BMI: {bmi:.1f}")

if bmi < 18.5:
    print("Zayıf")
elif bmi < 25:
    print("Normal kilolu")
elif bmi < 30:
    print("Fazla kilolu")
else:
    print("Obez")

print("\n=== KOŞUL YAPILARI ÖZETİ ===")
print("if koşul:")
print("    # koşul True ise çalışır")
print()
print("if koşul:")
print("    # koşul True ise")
print("else:")
print("    # koşul False ise")
print()
print("if koşul1:")
print("    # koşul1 True ise")
print("elif koşul2:")
print("    # koşul1 False, koşul2 True ise")
print("else:")
print("    # tüm koşullar False ise")
print()
print("DİKKAT:")
print("- Girintileme (indentation) önemli!")
print("- Koşul sırası önemli!")
print("- Boolean değerler: True/False")
print("- Karşılaştırma operatörleri: ==, !=, <, >, <=, >=")
print("- Mantıksal operatörler: and, or, not")