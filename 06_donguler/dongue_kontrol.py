# Döngü Kontrol İfadeleri
# break, continue ve pass kullanımı

print("=== DÖNGÜ KONTROL İFADELERİ ===\n")

print("1. BREAK İFADESİ:")
print("-" * 17)

# break ile döngüden çıkış
print("Sayı arama - break örneği:")
sayilar = [1, 3, 7, 9, 12, 15, 18, 21]
aranan = 12

for sayi in sayilar:
    print(f"Kontrol ediliyor: {sayi}")
    if sayi == aranan:
        print(f"✓ Aranan sayı {aranan} bulundu!")
        break
    print(f"  {sayi} ≠ {aranan}, devam ediliyor...")

print("Arama tamamlandı")

# while döngüsünde break
print(f"\nWhile döngüsünde break:")
sayac = 1
while True:  # Sonsuz döngü
    print(f"Sayaç: {sayac}")
    if sayac >= 5:
        print("Sayaç 5'e ulaştı, döngü sonlandırılıyor")
        break
    sayac += 1

print("\n2. CONTINUE İFADESİ:")
print("-" * 20)

# continue ile iterasyonu atlama
print("Tek sayıları atlama - continue örneği:")
for i in range(1, 11):
    if i % 2 != 0:  # Tek sayı ise
        continue  # Bu iterasyonu atla
    print(f"Çift sayı: {i}")

# String işlemede continue
print(f"\nSesli harfleri atlama:")
kelime = "Python Programlama"
sesli_harfler = "aeiouAEIOU"

for harf in kelime:
    if harf in sesli_harfler:
        continue  # Sesli harfi atla
    if harf != " ":  # Boşluk değilse
        print(harf, end="")
print()  # Yeni satır

# Liste işlemede continue
print(f"\nNegatif sayıları atlama:")
sayilar = [-3, 5, -1, 8, -9, 12, -4, 15]
pozitif_toplam = 0

for sayi in sayilar:
    if sayi < 0:
        print(f"Negatif sayı atlandı: {sayi}")
        continue
    print(f"Pozitif sayı eklendi: {sayi}")
    pozitif_toplam += sayi

print(f"Pozitif sayıların toplamı: {pozitif_toplam}")

print("\n3. PASS İFADESİ:")
print("-" * 16)

# pass ile placeholder
print("Pass ile placeholder kullanımı:")

for i in range(1, 6):
    if i == 3:
        pass  # Henüz implement edilmedi
        print("  (3 için özel işlem yapılacak)")
    else:
        print(f"Sayı işlendi: {i}")

# Fonksiyonlarda pass
def henuz_yazilmadi():
    pass  # Fonksiyon gövdesi boş olamaz

def debug_fonksiyonu(veri):
    # Debug kodları buraya gelecek
    pass

print("Pass ile boş yapılar oluşturuldu")

print("\n4. İÇ İÇE DÖNGÜLERDE BREAK:")
print("-" * 27)

# İç içe döngülerde break kullanımı
print("Matris içinde değer arama:")
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
aranan_deger = 5
bulundu = False

for satir_index, satir in enumerate(matris):
    for sutun_index, deger in enumerate(satir):
        print(f"Kontrol: matris[{satir_index}][{sutun_index}] = {deger}")
        if deger == aranan_deger:
            print(f"✓ Değer {aranan_deger} bulundu: [{satir_index}][{sutun_index}]")
            bulundu = True
            break
    if bulundu:  # Dış döngüyü de sonlandır
        break

# Çarpım tablosunda erken çıkış
print(f"\nÇarpım tablosu - 20'ye kadar:")
for i in range(1, 6):
    for j in range(1, 6):
        carpim = i * j
        print(f"{i}x{j}={carpim:2}", end="  ")
        if carpim >= 20:
            print("(20'ye ulaşıldı)")
            break
    print()

print("\n5. İÇ İÇE DÖNGÜLERDE CONTINUE:")
print("-" * 30)

# İç döngüde continue
print("Çarpım tablosu - çift sonuçlar:")
for i in range(1, 5):
    print(f"Satır {i}:", end=" ")
    for j in range(1, 5):
        carpim = i * j
        if carpim % 2 != 0:  # Tek sayı ise
            continue
        print(f"{carpim}", end=" ")
    print()

# Matris işlemede continue
print(f"\nMatris - sıfır olmayan elemanlar:")
matris = [
    [0, 2, 0],
    [4, 0, 6],
    [0, 8, 9]
]

for satir_index, satir in enumerate(matris):
    print(f"Satır {satir_index}:", end=" ")
    for deger in satir:
        if deger == 0:
            continue
        print(f"{deger}", end=" ")
    print()

print("\n6. KARMAŞIK KONTROL YAPILARI:")
print("-" * 29)

# Çoklu koşullu break ve continue
print("Sayı kategorileme:")
sayilar = [1, 8, 15, 22, 7, 30, 45, 3, 18, 50]

for sayi in sayilar:
    # 50'ye ulaşınca dur
    if sayi >= 50:
        print(f"✋ {sayi} - 50'ye ulaşıldı, döngü sonlandırılıyor")
        break
    
    # 5'in katlarını atla
    if sayi % 5 == 0:
        print(f"⏩ {sayi} - 5'in katı, atlandı")
        continue
    
    # Tek sayıları özel işle
    if sayi % 2 != 0:
        print(f"🔸 {sayi} - Tek sayı")
    else:
        print(f"🔹 {sayi} - Çift sayı")

print("\n7. MENÜ SİSTEMİ ÖRNEĞİ:")
print("-" * 22)

# Gelişmiş menü sistemi
print("Hesap Makinesi Menü Sistemi:")
islemler = [
    ("1", "toplama", 5, 3),
    ("2", "çıkarma", 10, 4),
    ("invalid", "geçersiz", 0, 0),
    ("3", "çarpma", 6, 7),
    ("4", "çıkış", 0, 0)
]

for secim, islem_adi, sayi1, sayi2 in islemler:
    print(f"\n=== HESAP MAKİNESİ ===")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Çıkış")
    print(f"Seçim: {secim}")
    
    if secim == "4":
        print("Program sonlandırılıyor...")
        break
    
    if secim not in ["1", "2", "3"]:
        print("❌ Geçersiz seçim!")
        continue
    
    print(f"Sayı 1: {sayi1}, Sayı 2: {sayi2}")
    
    if secim == "1":
        sonuc = sayi1 + sayi2
        print(f"Sonuç: {sayi1} + {sayi2} = {sonuc}")
    elif secim == "2":
        sonuc = sayi1 - sayi2
        print(f"Sonuç: {sayi1} - {sayi2} = {sonuc}")
    elif secim == "3":
        sonuc = sayi1 * sayi2
        print(f"Sonuç: {sayi1} × {sayi2} = {sonuc}")

print("\n8. HATA YÖNETİMİ İLE KONTROL:")
print("-" * 29)

# Güvenli veri işleme
print("Güvenli liste işleme:")
veri_listesi = ["123", "abc", "456", "789", "xyz", "0"]

for i, veri in enumerate(veri_listesi):
    try:
        sayi = int(veri)
        
        # Sıfıra bölme kontrolü
        if sayi == 0:
            print(f"Item {i}: {veri} - Sıfır değeri, atlandı")
            continue
            
        # Negatif sayı kontrolü (simüle edilmiş)
        if sayi < 0:
            print(f"Item {i}: {veri} - Negatif sayı, döngü sonlandırılıyor")
            break
            
        # Normal işlem
        sonuc = 100 / sayi
        print(f"Item {i}: {veri} → 100/{sayi} = {sonuc:.2f}")
        
    except ValueError:
        print(f"Item {i}: {veri} - Sayıya çevrilemez, atlandı")
        continue

print("\n9. PERFORMANS ÖPTİMİZASYONU:")
print("-" * 27)

# Erken çıkış ile optimizasyon
print("Büyük liste içinde arama (optimizasyon):")
buyuk_liste = list(range(1000, 2000))  # 1000 elemanlı liste
hedef_degerler = [1500, 1750]

for hedef in hedef_degerler:
    print(f"\n{hedef} aranıyor...")
    kontrol_sayisi = 0
    
    for deger in buyuk_liste:
        kontrol_sayisi += 1
        if deger == hedef:
            print(f"✓ {hedef} bulundu! {kontrol_sayisi} kontrol yapıldı")
            break
        if kontrol_sayisi % 100 == 0:
            print(f"  {kontrol_sayisi} eleman kontrol edildi...")

print("\n10. ELSE İLE DÖNGÜ KONTROLÜ:")
print("-" * 27)

# for-else ve while-else
print("For-else yapısı:")
asal_adaylar = [29, 31, 33, 37]

for sayi in asal_adaylar:
    print(f"\n{sayi} asal kontrolü:")
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            print(f"  {sayi} = {i} × {sayi//i} (asal değil)")
            break
    else:  # break çalışmadıysa
        print(f"  {sayi} asal sayıdır! ✓")

# while-else
print(f"\nWhile-else yapısı:")
sayilar = [2, 4, 6, 8, 9]  # Son eleman tek
i = 0

while i < len(sayilar):
    if sayilar[i] % 2 != 0:
        print(f"İlk tek sayı bulundu: {sayilar[i]}")
        break
    print(f"{sayilar[i]} çift")
    i += 1
else:
    print("Hiç tek sayı bulunamadı")

print("\n11. DEBUGGING İPUÇLARI:")
print("-" * 21)

# Debug için kontrol yapıları
print("Debug modlu döngü:")
DEBUG = True
sayilar = [1, 2, 3, 4, 5]

for i, sayi in enumerate(sayilar):
    if DEBUG:
        print(f"DEBUG: İterasyon {i}, değer {sayi}")
    
    if sayi == 3:
        if DEBUG:
            print("DEBUG: 3 değeri bulundu, continue çağrılıyor")
        continue
    
    if sayi > 4:
        if DEBUG:
            print("DEBUG: 4'ten büyük değer, break çağrılıyor")
        break
    
    print(f"İşlenen değer: {sayi}")

print("\n=== DÖNGÜ KONTROL ÖZETİ ===")
print("break:")
print("  • Döngüyü tamamen sonlandırır")
print("  • En yakın döngüyü etkiler")
print("  • for ve while'da kullanılır")
print()
print("continue:")
print("  • Mevcut iterasyonu atlar")
print("  • Döngünün başına döner")
print("  • Sonraki iterasyona geçer")
print()
print("pass:")
print("  • Hiçbir şey yapmaz")
print("  • Placeholder olarak kullanılır")
print("  • Söz dizimi hatası önler")
print()
print("else clause:")
print("  • Döngü normal biterse çalışır")
print("  • break ile çıkışta çalışmaz")
print("  • for/while her ikisinde de var")
print()
print("İpuçları:")
print("  • İç içe döngülerde label kullanımını araştır")
print("  • break/continue yerine fonksiyon return düşün")
print("  • Karmaşık kontroller için flag değişken kullan")