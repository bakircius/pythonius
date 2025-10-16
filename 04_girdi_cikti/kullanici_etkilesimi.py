# Kullanıcı Etkileşimi
# İnteraktif programlar ve kullanıcı deneyimi örnekleri

print("=== KULLANICI ETKİLEŞİMİ ÖRNEKLERİ ===\n")

print("1. BASIT SORU-CEVAP SİSTEMİ:")
print("-" * 29)

# Basit tanışma programı (simülasyon)
def tanisma_simulasyonu():
    """Kullanıcıyla tanışma simülasyonu"""
    print("=== TANIŞMA PROGRAMI ===")
    
    # Simüle edilmiş kullanıcı girdileri
    simulasyon_cevaplari = {
        "İsminiz nedir?": "Ahmet",
        "Kaç yaşındasınız?": "25",
        "Hangi şehirde yaşıyorsunuz?": "İstanbul",
        "En sevdiğiniz renk nedir?": "Mavi"
    }
    
    kullanici_bilgileri = {}
    
    for soru, cevap in simulasyon_cevaplari.items():
        print(f"\n{soru}")
        print(f"Kullanıcı girişi: {cevap}")
        
        if "yaş" in soru.lower():
            kullanici_bilgileri["yas"] = int(cevap)
        elif "isim" in soru.lower():
            kullanici_bilgileri["isim"] = cevap
        elif "şehir" in soru.lower():
            kullanici_bilgileri["sehir"] = cevap
        elif "renk" in soru.lower():
            kullanici_bilgileri["renk"] = cevap
    
    # Kişiselleştirilmiş mesaj
    print(f"\n=== ÖZET ===")
    print(f"Merhaba {kullanici_bilgileri['isim']}!")
    print(f"{kullanici_bilgileri['yas']} yaşındasın ve {kullanici_bilgileri['sehir']}'da yaşıyorsun.")
    print(f"En sevdiğin renk {kullanici_bilgileri['renk']}.")
    
    # Yaşa göre yorum
    if kullanici_bilgileri["yas"] < 18:
        print("Henüz gençsin, hayatta başarılar!")
    elif kullanici_bilgileri["yas"] < 65:
        print("Hayatının en verimli döneminde")
    else:
        print("Tecrübe ve bilgi dolu yıllar!")

tanisma_simulasyonu()

print("\n" + "="*50 + "\n")

print("2. HESAP MAKİNESİ ETKİLEŞİMİ:")
print("-" * 31)

def hesap_makinesi_simulasyonu():
    """İnteraktif hesap makinesi simülasyonu"""
    print("=== HESAP MAKİNESİ ===")
    
    # Simülasyon verileri
    test_islemleri = [
        ("15", "+", "7"),
        ("20", "-", "8"),
        ("6", "*", "9"),
        ("45", "/", "5")
    ]
    
    for sayi1_str, operator, sayi2_str in test_islemleri:
        print(f"\nBirinci sayı: {sayi1_str}")
        print(f"İşlem (+, -, *, /): {operator}")
        print(f"İkinci sayı: {sayi2_str}")
        
        try:
            sayi1 = float(sayi1_str)
            sayi2 = float(sayi2_str)
            
            if operator == "+":
                sonuc = sayi1 + sayi2
            elif operator == "-":
                sonuc = sayi1 - sayi2
            elif operator == "*":
                sonuc = sayi1 * sayi2
            elif operator == "/":
                if sayi2 != 0:
                    sonuc = sayi1 / sayi2
                else:
                    print("Hata: Sıfıra bölme!")
                    continue
            else:
                print("Geçersiz işlem!")
                continue
            
            print(f"Sonuç: {sayi1} {operator} {sayi2} = {sonuc}")
            
        except ValueError:
            print("Hata: Geçerli sayı giriniz!")

hesap_makinesi_simulasyonu()

print("\n" + "="*50 + "\n")

print("3. MENÜ TABANlı PROGRAM:")
print("-" * 25)

def menu_programi_simulasyonu():
    """Menü tabanlı program simülasyonu"""
    print("=== ÖĞREN​Cİ YÖNETİM SİSTEMİ ===")
    
    ogrenciler = {
        "Ahmet": [85, 92, 78],
        "Ayşe": [96, 89, 94],
        "Mehmet": [72, 81, 69]
    }
    
    # Simüle edilmiş kullanıcı seçimleri
    secimler = ["1", "2", "3", "4"]
    
    for secim in secimler:
        print(f"\n=== ANA MENÜ ===")
        print("1. Öğrenci listesi")
        print("2. Not ortalaması hesapla")
        print("3. Yeni öğrenci ekle")
        print("4. Çıkış")
        print(f"\nSeçiminiz: {secim}")
        
        if secim == "1":
            print("\n--- ÖĞREN​Cİ LİSTESİ ---")
            for i, isim in enumerate(ogrenciler.keys(), 1):
                print(f"{i}. {isim}")
                
        elif secim == "2":
            print("\n--- NOT ORTALAMALARI ---")
            for isim, notlar in ogrenciler.items():
                ortalama = sum(notlar) / len(notlar)
                print(f"{isim}: {ortalama:.2f}")
                
        elif secim == "3":
            # Yeni öğrenci ekleme simülasyonu
            yeni_isim = "Fatma"
            yeni_notlar = [88, 91, 86]
            print(f"\nYeni öğrenci adı: {yeni_isim}")
            print(f"Notları: {yeni_notlar}")
            ogrenciler[yeni_isim] = yeni_notlar
            print(f"{yeni_isim} sisteme eklendi!")
            
        elif secim == "4":
            print("Program sonlandırılıyor...")
            break
        else:
            print("Geçersiz seçim!")

menu_programi_simulasyonu()

print("\n" + "="*50 + "\n")

print("4. VERİ DOĞRULAMA ÖRNEKLERİ:")
print("-" * 28)

def veri_dogrulama_ornekleri():
    """Veri doğrulama örnekleri"""
    print("=== VERİ DOĞRULAMA ÖRNEKLERİ ===")
    
    # E-posta doğrulama
    print("\n1. E-posta doğrulama:")
    test_emailler = ["ahmet@email.com", "geçersiz-email", "test@gmail.com"]
    
    for email in test_emailler:
        print(f"E-posta: {email}")
        if "@" in email and "." in email:
            print("✓ Geçerli e-posta formatı")
        else:
            print("✗ Geçersiz e-posta formatı")
    
    # Yaş doğrulama
    print("\n2. Yaş doğrulama:")
    test_yaslar = ["25", "150", "-5", "abc"]
    
    for yas_str in test_yaslar:
        print(f"Yaş girişi: '{yas_str}'")
        try:
            yas = int(yas_str)
            if 0 <= yas <= 120:
                print(f"✓ Geçerli yaş: {yas}")
            else:
                print("✗ Yaş 0-120 arasında olmalı")
        except ValueError:
            print("✗ Sayısal değer giriniz")
    
    # Telefon doğrulama
    print("\n3. Telefon doğrulama:")
    test_telefonlar = ["05321234567", "123", "05aa1234567"]
    
    for telefon in test_telefonlar:
        print(f"Telefon: {telefon}")
        if len(telefon) == 11 and telefon.startswith("0") and telefon[1:].isdigit():
            print("✓ Geçerli telefon formatı")
        else:
            print("✗ Geçersiz telefon formatı (0xxxxxxxxxx)")

veri_dogrulama_ornekleri()

print("\n" + "="*50 + "\n")

print("5. OYUN BENZERI ETKİLEŞİM:")
print("-" * 26)

def sayi_tahmin_oyunu():
    """Sayı tahmin oyunu simülasyonu"""
    print("=== SAYI TAHMİN OYUNU ===")
    
    import random
    gizli_sayi = random.randint(1, 100)
    tahminler = [45, 67, 89, gizli_sayi]  # Simüle edilmiş tahminler
    
    print("1 ile 100 arasında bir sayı tuttum!")
    print("Tahmin etmeye çalış!")
    
    for i, tahmin in enumerate(tahminler, 1):
        print(f"\n{i}. Tahmin: {tahmin}")
        
        if tahmin == gizli_sayi:
            print(f"🎉 Tebrikler! {i}. tahminde bildin!")
            print(f"Gizli sayı: {gizli_sayi}")
            break
        elif tahmin < gizli_sayi:
            print("📈 Daha büyük bir sayı dene!")
        else:
            print("📉 Daha küçük bir sayı dene!")
    
    print(f"\nOyun bitti. Gizli sayı: {gizli_sayi}")

sayi_tahmin_oyunu()

print("\n" + "="*50 + "\n")

print("6. KULLANICI DENEYİMİ İPUÇLARI:")
print("-" * 33)

print("✓ İyi Kullanıcı Deneyimi:")
print("  - Açık ve anlaşılır yönergeler")
print("  - Kullanıcı hatalarını yakala ve açıkla")
print("  - İlerleme durumunu göster")
print("  - Çıkış seçeneği sun")
print("  - Kısa ve öz mesajlar")

print("\n✗ Kötü Kullanıcı Deneyimi:")
print("  - Belirsiz hata mesajları")
print("  - Program çökmesi")
print("  - Çok uzun bekleme süreleri")
print("  - Karışık menüler")
print("  - Geri alma seçeneği yok")

print("\n=== ETKİLEŞİM PATTERN'LERİ ===")

print("\n1. Basit Soru-Cevap:")
print("   soru → cevap → işlem → sonuç")

print("\n2. Menü Tabanlı:")
print("   menü göster → seçim al → işlem → tekrar menü")

print("\n3. Döngülü Etkileşim:")
print("   başlat → işlem → devam et? → bitir/tekrar")

print("\n4. Adım Adım Kılavuz:")
print("   adım1 → adım2 → ... → tamamla")

print("\n=== GERÇEK PROGRAM ÖRNEĞİ ===")
print("""
# Gerçek input() kullanımı:

def gercek_hesap_makinesi():
    while True:
        print("\\n=== HESAP MAKİNESİ ===")
        
        try:
            sayi1 = float(input("Birinci sayı: "))
            operator = input("İşlem (+, -, *, /): ")
            sayi2 = float(input("İkinci sayı: "))
            
            if operator == "+":
                print(f"Sonuç: {sayi1 + sayi2}")
            elif operator == "-":
                print(f"Sonuç: {sayi1 - sayi2}")
            elif operator == "*":
                print(f"Sonuç: {sayi1 * sayi2}")
            elif operator == "/":
                if sayi2 != 0:
                    print(f"Sonuç: {sayi1 / sayi2}")
                else:
                    print("Hata: Sıfıra bölme!")
            else:
                print("Geçersiz işlem!")
                
        except ValueError:
            print("Hata: Geçerli sayı girin!")
        
        devam = input("Devam etmek istiyor musunuz? (e/h): ")
        if devam.lower() != 'e':
            break

# gercek_hesap_makinesi()  # Çalıştır
""")