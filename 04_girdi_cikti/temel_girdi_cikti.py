# Temel Girdi ve Çıktı İşlemleri
# print() ve input() fonksiyonlarının kullanımı

print("=== TEMEL GİRDİ ÇIKTI İŞLEMLERİ ===\n")

print("1. PRİNT() FONKSİYONU TEMEL KULLANIM:")
print("-" * 38)

# Basit print kullanımı
print("Merhaba Dünya!")
print("Python öğreniyorum")

# Birden fazla değer yazdırma
print("Python", "programlama", "dili")
print("Sayılar:", 1, 2, 3, 4, 5)

# Değişkenlerle print
isim = "Ahmet"
yas = 25
print("İsim:", isim)
print("Yaş:", yas)
print("İsim:", isim, "Yaş:", yas)

print("\n2. PRİNT() FONKSİYONU PARAMETRELERİ:")
print("-" * 36)

# sep parametresi (ayıraç)
print("Elma", "Armut", "Muz")  # Varsayılan: boşluk
print("Elma", "Armut", "Muz", sep="-")
print("Elma", "Armut", "Muz", sep=" | ")
print("Elma", "Armut", "Muz", sep="")

# end parametresi (bitiş karakteri)
print("Bu satır", end=" ")
print("aynı satırda devam eder")
print("Bu satır", end="...")
print("nokta ile biter")
print("Bu normal satır")

print("\n3. INPUT() FONKSİYONU KULLANIMI:")
print("-" * 33)

# NOT: Gerçek kullanımda input() bekler, burada örnek gösteriyoruz
print("# Kullanıcıdan veri alma örnekleri:")
print('isim = input("Adınızı girin: ")')
print('yas = input("Yaşınızı girin: ")')

# Örnek değerler (gerçek input yerine)
isim_ornegi = "Mehmet"
yas_ornegi = "30"

print(f"\n# Örnek giriş değerleri:")
print(f"# Kullanıcı girdi → isim: '{isim_ornegi}'")
print(f"# Kullanıcı girdi → yas: '{yas_ornegi}'")

print(f"\n# Bu değerlerle çalışma:")
print(f"Merhaba {isim_ornegi}!")
print(f"Sen {yas_ornegi} yaşındasın")

# input() her zaman string döndürür
print(f"\nDİKKAT: input() her zaman string döner")
print(f"type('{yas_ornegi}') = {type(yas_ornegi)}")

print("\n4. INPUT() İLE SAYI ALMA:")
print("-" * 26)

print("# String'i sayıya çevirme:")
print('yas_str = input("Yaşınız: ")')
print('yas_int = int(yas_str)')
print('# veya kısa yolu:')
print('yas = int(input("Yaşınız: "))')

# Örnek dönüşüm
yas_str = "25"
yas_int = int(yas_str)
print(f"\nÖrnek: '{yas_str}' → {yas_int}")
print(f"Tip değişimi: {type(yas_str)} → {type(yas_int)}")

# Matematik işlemi
print(f"5 yıl sonra yaşınız: {yas_int + 5}")

print("\n5. ÇOKLU VERİ ALMA:")
print("-" * 19)

print("# Birden fazla değer alma:")
print('ad, soyad = input("Ad Soyad: ").split()')
print('x, y, z = input("3 sayı girin: ").split()')

# Örnek split kullanımı
ad_soyad_str = "Ali Veli"
ad, soyad = ad_soyad_str.split()
print(f"\nÖrnek: '{ad_soyad_str}' → ad='{ad}', soyad='{soyad}'")

# Sayıları ayırma
sayilar_str = "10 20 30"
x, y, z = sayilar_str.split()
print(f"String sayılar: {x}, {y}, {z}")
x, y, z = int(x), int(y), int(z)
print(f"Integer sayılar: {x}, {y}, {z}")

print("\n6. PRATİK ÖRNEKLER:")
print("-" * 18)

# Basit hesap makinesi simülasyonu
print("=== HESAP MAKİNESİ SİMÜLASYONU ===")
sayi1_str = "15"
sayi2_str = "7"

print(f"# Kullanıcı girişi: {sayi1_str} ve {sayi2_str}")

sayi1 = int(sayi1_str)
sayi2 = int(sayi2_str)

print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}")
print(f"{sayi1} - {sayi2} = {sayi1 - sayi2}")
print(f"{sayi1} * {sayi2} = {sayi1 * sayi2}")
print(f"{sayi1} / {sayi2} = {sayi1 / sayi2}")

print("\n=== KİŞİSEL BİLGİ TOPLAMA ===")
# Kişisel bilgi toplama örneği
bilgiler = {
    "ad": "Zeynep",
    "soyad": "Yılmaz", 
    "yas": "28",
    "sehir": "İstanbul"
}

print("# Toplanan bilgiler:")
for anahtar, deger in bilgiler.items():
    print(f"{anahtar}: {deger}")

print(f"\nMerhaba {bilgiler['ad']} {bilgiler['soyad']}!")
print(f"{bilgiler['yas']} yaşındasın ve {bilgiler['sehir']}'da yaşıyorsun.")

print("\n7. HATA YÖNETİMİ:")
print("-" * 16)

print("# Güvenli sayı alma:")
def guvenli_sayi_al(metin):
    """Kullanıcıdan güvenli şekilde sayı alır"""
    while True:
        try:
            girdi = input(metin)
            return int(girdi)
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")

print("""
def guvenli_sayi_al(metin):
    while True:
        try:
            girdi = input(metin)
            return int(girdi)
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")
""")

print("\n8. FORMAT ÖRNEKLERİ:")
print("-" * 17)

isim = "Python"
versiyon = 3.9
print(f"Dil: {isim}, Versiyon: {versiyon}")

# Tablo formatı
print("\n=== ÖĞREN​Cİ LİSTESİ ===")
print(f"{'İsim':<10} {'Yaş':<5} {'Not':<5}")
print("-" * 20)
print(f"{'Ali':<10} {20:<5} {85:<5}")
print(f"{'Ayşe':<10} {19:<5} {92:<5}")
print(f"{'Mehmet':<10} {21:<5} {78:<5}")

print("\n=== GİRDİ ÇIKTI ÖZETİ ===")
print("print():")
print("  - Ekrana çıktı verir")
print("  - sep: ayıraç belirler")
print("  - end: bitiş karakteri belirler")
print()
print("input():")
print("  - Kullanıcıdan girdi alır")  
print("  - Her zaman string döner")
print("  - Sayı için int() dönüşümü gerekli")
print()
print("İpuçları:")
print("  - input() sonucunu hemen dönüştür")
print("  - Hata kontrolü yap")
print("  - Kullanıcıya açık yönergeler ver")