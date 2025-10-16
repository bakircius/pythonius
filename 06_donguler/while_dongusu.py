# While Döngüsü
# Koşula bağlı döngü yapısı

print("=== WHILE DÖNGÜSÜ ===\n")

print("1. TEMEL WHILE DÖNGÜSÜ:")
print("-" * 23)

# Basit while döngüsü
sayac = 1
print("1'den 5'e kadar sayma:")
while sayac <= 5:
    print(f"Sayaç: {sayac}")
    sayac += 1  # sayac = sayac + 1

print("Döngü bitti")

# Geriye sayma
print("\n5'ten 1'e geriye sayma:")
sayac = 5
while sayac >= 1:
    print(f"Sayaç: {sayac}")
    sayac -= 1

print("\n2. KOŞUL KONTROLLÜ DÖNGÜ:")
print("-" * 26)

# Kullanıcı girişi simülasyonu
denemeler = ["şifre123", "yanlış", "12345", "python"]
deneme_sayisi = 0
dogru_sifre = "python"

print("Şifre kontrol simülasyonu:")
while deneme_sayisi < len(denemeler):
    girilen_sifre = denemeler[deneme_sayisi]
    print(f"Deneme {deneme_sayisi + 1}: '{girilen_sifre}'")
    
    if girilen_sifre == dogru_sifre:
        print("✓ Şifre doğru! Giriş başarılı.")
        break
    else:
        print("✗ Yanlış şifre.")
        deneme_sayisi += 1

if deneme_sayisi >= len(denemeler):
    print("❌ Çok fazla yanlış deneme!")

print("\n3. SONSUZ DÖNGÜ VE BREAK:")
print("-" * 27)

# Menü sistemi simülasyonu
secimler = ["1", "2", "3", "4"]  # Simüle edilmiş kullanıcı seçimleri
secim_index = 0

print("Menü sistemi simülasyonu:")
while True:
    print("\n=== MENÜ ===")
    print("1. Seçenek 1")
    print("2. Seçenek 2") 
    print("3. Seçenek 3")
    print("4. Çıkış")
    
    if secim_index < len(secimler):
        secim = secimler[secim_index]
        print(f"Kullanıcı seçimi: {secim}")
        secim_index += 1
    else:
        secim = "4"  # Döngüyü sonlandır
    
    if secim == "1":
        print("Seçenek 1 seçildi")
    elif secim == "2":
        print("Seçenek 2 seçildi")
    elif secim == "3":
        print("Seçenek 3 seçildi")
    elif secim == "4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim!")

print("\n4. SAYICI İLE WHILE:")
print("-" * 20)

# Faktöriyel hesaplama
n = 5
faktoriyel = 1
sayac = 1

print(f"{n}! hesaplama:")
while sayac <= n:
    faktoriyel *= sayac
    print(f"{sayac}! = {faktoriyel}")
    sayac += 1

print(f"Sonuç: {n}! = {faktoriyel}")

# Fibonacci serisi
print(f"\nİlk 8 Fibonacci sayısı:")
a, b = 0, 1
sayac = 0
while sayac < 8:
    print(f"F({sayac}) = {a}")
    a, b = b, a + b
    sayac += 1

print("\n5. LİSTE İŞLEMLERİ:")
print("-" * 18)

# Liste elemanlarını işleme
sayilar = [10, 25, 7, 33, 15, 42, 8]
print(f"Orijinal liste: {sayilar}")

# 20'den büyük sayıları bulma
index = 0
bulunanlar = []
while index < len(sayilar):
    if sayilar[index] > 20:
        bulunanlar.append(sayilar[index])
    index += 1

print(f"20'den büyük sayılar: {bulunanlar}")

# Liste elemanlarının toplamı
toplam = 0
index = 0
while index < len(sayilar):
    toplam += sayilar[index]
    index += 1

print(f"Toplam: {toplam}")

print("\n6. STRING İŞLEMLERİ:")
print("-" * 19)

# Karakter sayma
metin = "Python Programlama"
print(f"Metin: '{metin}'")

index = 0
sesli_harfler = "aeiouAEIOU"
sesli_sayisi = 0

while index < len(metin):
    if metin[index] in sesli_harfler:
        sesli_sayisi += 1
    index += 1

print(f"Sesli harf sayısı: {sesli_sayisi}")

# Kelime bulma
aranan_kelime = "Python"
index = 0
bulundu = False

while index <= len(metin) - len(aranan_kelime):
    if metin[index:index + len(aranan_kelime)] == aranan_kelime:
        print(f"'{aranan_kelime}' kelimesi {index}. pozisyonda bulundu")
        bulundu = True
        break
    index += 1

if not bulundu:
    print(f"'{aranan_kelime}' kelimesi bulunamadı")

print("\n7. KOŞULLU ARTIRMA:")
print("-" * 20)

# Asal sayı bulma
sayi = 2
asal_sayilar = []
sayac = 0

print("İlk 10 asal sayı:")
while sayac < 10:
    # Asal kontrolü
    asal = True
    bolen = 2
    while bolen * bolen <= sayi:
        if sayi % bolen == 0:
            asal = False
            break
        bolen += 1
    
    if asal:
        asal_sayilar.append(sayi)
        print(f"Asal {sayac + 1}: {sayi}")
        sayac += 1
    
    sayi += 1

print(f"Bulunan asal sayılar: {asal_sayilar}")

print("\n8. NESTED WHILE (İÇ İÇE):")
print("-" * 25)

# Çarpım tablosu
print("Çarpım tablosu (3x3):")
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"{i}x{j}={i*j:2}", end="  ")
        j += 1
    print()  # Yeni satır
    i += 1

# Matris toplama
print("\nMatris işlemi:")
matris1 = [[1, 2], [3, 4]]
matris2 = [[5, 6], [7, 8]]
sonuc = [[0, 0], [0, 0]]

satir = 0
while satir < 2:
    sutun = 0
    while sutun < 2:
        sonuc[satir][sutun] = matris1[satir][sutun] + matris2[satir][sutun]
        sutun += 1
    satir += 1

print(f"Matris 1: {matris1}")
print(f"Matris 2: {matris2}")
print(f"Toplam: {sonuc}")

print("\n9. WHILE VS FOR KARŞILAŞTIRMA:")
print("-" * 30)

# Aynı işlemi for ve while ile
print("For döngüsü ile:")
for i in range(1, 6):
    print(f"Kare: {i}² = {i**2}")

print("\nWhile döngüsü ile:")
i = 1
while i <= 5:
    print(f"Kare: {i}² = {i**2}")
    i += 1

# Liste iterasyonu
liste = ["a", "b", "c", "d"]

print(f"\nListe: {liste}")
print("For ile:")
for eleman in liste:
    print(f"Eleman: {eleman}")

print("While ile:")
index = 0
while index < len(liste):
    print(f"Eleman: {liste[index]}")
    index += 1

print("\n10. PERFORMANCE VE GÜVENLIK:")
print("-" * 29)

# Güvenli while döngüsü
max_deneme = 1000  # Sonsuz döngü koruması
deneme = 0
hedef = 42

print("Güvenli rastgele sayı arama simülasyonu:")
import random
random.seed(42)  # Tekrarlanabilir sonuç için

while deneme < max_deneme:
    rastgele_sayi = random.randint(1, 100)
    deneme += 1
    
    if rastgele_sayi == hedef:
        print(f"✓ Hedef sayı {hedef}, {deneme}. denemede bulundu!")
        break
    elif deneme % 100 == 0:  # Her 100 denemede rapor
        print(f"Deneme {deneme}: {rastgele_sayi}")

if deneme >= max_deneme:
    print(f"❌ {max_deneme} denemede hedef bulunamadı")

print("\n11. COMMON PATTERNS:")
print("-" * 18)

# Input validation pattern
print("Girdi doğrulama pattern:")
valid_inputs = ["evet", "hayır", "e", "h"]
user_inputs = ["belki", "evet"]  # Simüle edilmiş girdiler
input_index = 0

while input_index < len(user_inputs):
    user_input = user_inputs[input_index].lower()
    print(f"Kullanıcı girişi: '{user_input}'")
    
    if user_input in valid_inputs:
        print("✓ Geçerli giriş")
        break
    else:
        print("✗ Geçersiz giriş, tekrar deneyin")
        input_index += 1

# Accumulator pattern
print("\nAccumulator pattern:")
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cift_toplam = 0
index = 0

while index < len(sayilar):
    if sayilar[index] % 2 == 0:
        cift_toplam += sayilar[index]
    index += 1

print(f"Çift sayıların toplamı: {cift_toplam}")

print("\n12. HATA YÖNETİMİ:")
print("-" * 17)

# ZeroDivisionError koruması
pay = 100
payda_listesi = [5, 2, 0, 4]
index = 0

print("Güvenli bölme işlemleri:")
while index < len(payda_listesi):
    payda = payda_listesi[index]
    
    if payda != 0:
        sonuc = pay / payda
        print(f"{pay} ÷ {payda} = {sonuc}")
    else:
        print(f"{pay} ÷ {payda} = Sıfıra bölme hatası!")
    
    index += 1

print("\n=== WHILE DÖNGÜSÜ ÖZETİ ===")
print("Söz dizimi:")
print("while koşul:")
print("    # kod bloku")
print("    # koşulu değiştiren kod")
print()
print("Temel kurallar:")
print("• Koşul başta kontrol edilir")
print("• Koşul False olana kadar devam eder")
print("• Sonsuz döngüye dikkat!")
print("• break ile erken çıkış")
print("• continue ile sonraki iterasyon")
print()
print("Ne zaman kullanılır:")
print("• Kaç kez döneceği belli değilse")
print("• Koşula bağlı işlemler")
print("• Kullanıcı girişi kontrolü")
print("• Menü sistemleri")
print()
print("For vs While:")
print("• For: Bilinen tekrar sayısı")
print("• While: Koşula bağlı tekrar")
print("• For genelde daha güvenli")
print("• While daha esnek")