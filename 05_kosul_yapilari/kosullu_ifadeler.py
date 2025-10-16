# Koşullu İfadeler (Ternary Operator)
# Tek satırda koşul yazma teknikleri

print("=== KOŞULLU İFADELER (TERNARY OPERATOR) ===\n")

print("1. TEMEL TERNARY OPERATÖR:")
print("-" * 27)

# Klasik if-else yapısı
yas = 20
print(f"Yaş: {yas}")

if yas >= 18:
    durum = "Reşit"
else:
    durum = "Reşit değil"
print(f"Klasik yöntem: {durum}")

# Ternary operator ile aynı işlem
durum = "Reşit" if yas >= 18 else "Reşit değil"
print(f"Ternary ile: {durum}")

print("\n2. FARKLI VERİ TİPLERİYLE:")
print("-" * 26)

# Sayısal değerler
sayi = -5
print(f"Sayı: {sayi}")
mutlak_deger = sayi if sayi >= 0 else -sayi
print(f"Mutlak değer: {mutlak_deger}")

# String değerler
isim = ""
print(f"İsim: '{isim}'")
gosterilecek_isim = isim if isim else "İsimsiz"
print(f"Gösterilecek: '{gosterilecek_isim}'")

# Boolean değerler
aktif = True
print(f"Aktif: {aktif}")
durum_mesaji = "Çevrimiçi" if aktif else "Çevrimdışı"
print(f"Durum: {durum_mesaji}")

print("\n3. MATEMATİKSEL İŞLEMLER:")
print("-" * 26)

# Maksimum bulma
a, b = 15, 23
print(f"a = {a}, b = {b}")
maksimum = a if a > b else b
print(f"Maksimum: {maksimum}")

# Minimum bulma
minimum = a if a < b else b
print(f"Minimum: {minimum}")

# Çift/tek kontrolü
sayi = 17
print(f"\nSayı: {sayi}")
tip = "çift" if sayi % 2 == 0 else "tek"
print(f"Sayı tipi: {tip}")

# İşaret kontrolü
sayi = -8
print(f"\nSayı: {sayi}")
isaret = "pozitif" if sayi > 0 else ("sıfır" if sayi == 0 else "negatif")
print(f"İşaret: {isaret}")

print("\n4. LİSTE İŞLEMLERİ:")
print("-" * 18)

# Liste boş kontrolü
liste = [1, 2, 3]
print(f"Liste: {liste}")
mesaj = "Liste dolu" if liste else "Liste boş"
print(f"Durum: {mesaj}")

# Liste eleman sayısı
eleman_sayisi = len(liste) if liste else 0
print(f"Eleman sayısı: {eleman_sayisi}")

# Liste ilk elemanı
ilk_eleman = liste[0] if liste else None
print(f"İlk eleman: {ilk_eleman}")

print("\n5. STRING İŞLEMLERİ:")
print("-" * 19)

# String formatlama
kullanici_adi = "admin"
print(f"Kullanıcı adı: '{kullanici_adi}'")
hosgeldin = f"Hoşgeldin {kullanici_adi}" if kullanici_adi else "Hoşgeldin misafir"
print(f"Mesaj: {hosgeldin}")

# String uzunluk kontrolü
sifre = "123456"
print(f"\nŞifre: '{sifre}'")
sifre_durumu = "Güvenli" if len(sifre) >= 8 else "Güvensiz"
print(f"Şifre durumu: {sifre_durumu}")

# E-mail kontrolü
email = "user@example.com"
print(f"\nE-mail: '{email}'")
email_gecerli = "Geçerli" if "@" in email and "." in email else "Geçersiz"
print(f"E-mail durumu: {email_gecerli}")

print("\n6. FUNKSİYONLARLA KULLANIM:")
print("-" * 27)

# Fonksiyonlarda ternary
def mutlak_deger(x):
    return x if x >= 0 else -x

def max_iki_sayi(a, b):
    return a if a > b else b

def not_harfi(puan):
    return "A" if puan >= 90 else ("B" if puan >= 80 else ("C" if puan >= 70 else "F"))

# Test
print(f"mutlak_deger(-10): {mutlak_deger(-10)}")
print(f"max_iki_sayi(5, 8): {max_iki_sayi(5, 8)}")
print(f"not_harfi(85): {not_harfi(85)}")

print("\n7. KARMAŞIK KOŞULLAR:")
print("-" * 21)

# Çoklu koşul
yas = 25
gelir = 3000
print(f"Yaş: {yas}, Gelir: {gelir}")

kredi_durumu = "Uygun" if yas >= 18 and gelir >= 2000 else "Uygun değil"
print(f"Kredi durumu: {kredi_durumu}")

# İç içe ternary (dikkatli kullanın!)
sayi = 0
print(f"\nSayı: {sayi}")
durum = "pozitif" if sayi > 0 else ("sıfır" if sayi == 0 else "negatif")
print(f"Durum: {durum}")

print("\n8. LİST COMPREHENSION İLE:")
print("-" * 26)

# Liste elemanlarını koşula göre değiştirme
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Sayılar: {sayilar}")

# Çift sayıları karele, tek sayıları iki katına çıkar
sonuc = [x**2 if x % 2 == 0 else x*2 for x in sayilar]
print(f"Sonuç: {sonuc}")

# Pozitif sayıları koru, negatiflerini sıfır yap
sayilar2 = [-3, 5, -1, 8, -9, 2]
print(f"\nSayılar2: {sayilar2}")
temizlenmis = [x if x >= 0 else 0 for x in sayilar2]
print(f"Temizlenmiş: {temizlenmis}")

print("\n9. SÖZLÜK İŞLEMLERİ:")
print("-" * 19)

# Sözlük değer kontrolü
kisi = {"isim": "Ahmet", "yas": 30}
print(f"Kişi: {kisi}")

# Güvenli değer alma
yas = kisi.get("yas", 0)
isim = kisi.get("isim", "Bilinmiyor")
sehir = kisi.get("sehir", "Belirtilmemiş")

print(f"Yaş: {yas}")
print(f"İsim: {isim}")
print(f"Şehir: {sehir}")

# Ternary ile güvenli erişim
telefon = kisi["telefon"] if "telefon" in kisi else "Numara yok"
print(f"Telefon: {telefon}")

print("\n10. PERFORMANS VE ÇIKTI FORMATlAMA:")
print("-" * 35)

# Çıktı formatlaması
puan = 92
print(f"Puan: {puan}")

# Emoji ile durumu gösterme
emoji = "🎉" if puan >= 90 else ("😊" if puan >= 80 else ("😐" if puan >= 70 else "😢"))
mesaj = f"{emoji} Puanınız: {puan}"
print(f"Mesaj: {mesaj}")

# Renk kodu belirleme (varsayımsal)
renk = "yeşil" if puan >= 80 else ("sarı" if puan >= 60 else "kırmızı")
print(f"Renk kodu: {renk}")

# Hızlı kategorizasyon
kategori = "A" if puan >= 90 else ("B" if puan >= 75 else ("C" if puan >= 60 else "D"))
print(f"Kategori: {kategori}")

print("\n11. GERÇEK DÜNYA ÖRNEKLERİ:")
print("-" * 27)

# E-ticaret indirim sistemi
uye_tipi = "premium"
sepet_tutari = 150
print(f"Üye tipi: {uye_tipi}, Sepet: {sepet_tutari}₺")

indirim_orani = 0.20 if uye_tipi == "premium" else (0.10 if uye_tipi == "gold" else 0.05)
indirimli_fiyat = sepet_tutari * (1 - indirim_orani)
print(f"İndirim oranı: %{indirim_orani*100:.0f}")
print(f"İndirimli fiyat: {indirimli_fiyat:.2f}₺")

# Kargo ücreti hesaplama
kargo = 0 if sepet_tutari >= 100 else 15
toplam = indirimli_fiyat + kargo
print(f"Kargo: {kargo}₺")
print(f"Toplam: {toplam:.2f}₺")

# Hava durumu önerisi
sicaklik = 22
print(f"\nSıcaklık: {sicaklik}°C")
oneri = "Dışarı çıkabilirsiniz" if 15 <= sicaklik <= 30 else "İçeride kalın"
print(f"Öneri: {oneri}")

print("\n=== TERNARY OPERATOR ÖZETİ ===")
print("Söz dizimi:")
print("deger = ifade1 if koşul else ifade2")
print()
print("Örnekler:")
print("durum = 'pozitif' if x > 0 else 'negatif'")
print("maksimum = a if a > b else b")
print("mesaj = 'dolu' if liste else 'boş'")
print()
print("Avantajlar:")
print("✓ Kısa ve öz kod")
print("✓ Okunabilir (basit koşullarda)")
print("✓ Fonksiyonel programlama stili")
print()
print("Dezavantajlar:")
print("✗ Karmaşık koşullarda okunması zor")
print("✗ Çoklu koşullarda hantal")
print("✗ Debug etmesi zor")
print()
print("Ne zaman kullanılır:")
print("• Basit koşullar için")
print("• Değişken atama sırasında")
print("• List comprehension içinde")
print("• Kısa fonksiyonlarda")