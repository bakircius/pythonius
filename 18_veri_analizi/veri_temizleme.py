"""
Veri Temizleme Teknikleri
Bu dosyada gerçek dünyadaki kirli verilerle nasıl başa çıkılacağını öğreniyoruz.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import re

print("=== Veri Temizleme Teknikleri ===\n")

# =============================================================================
# 1. KİRLİ VERİ SETİ OLUŞTURMA
# =============================================================================

print("1. Kirli Veri Seti Oluşturma")
print("-" * 30)

# Gerçekçi kirli veri oluşturma
np.random.seed(42)

kirli_data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'isim': ['Ahmet Yılmaz', 'ayşe demir', 'MEHMET KAYA', 'Fatma  Şahin', 
             'ali özkan', '', 'Zeynep Güler', 'Hasan Çelik', None, 'elif yıldız',
             'Murat  Aydın', 'Seda   Polat'],
    'yas': [25, 30, -5, 999, 28, 35, None, 22, 45, np.nan, 0, 33],
    'email': ['ahmet@email.com', 'AYSE@EMAIL.COM', 'mehmet@', 
              'fatma.sahin@company.co.uk', '', 'invalid-email',
              'zeynep@email.com', 'hasan@email', np.nan, 'elif@email.com',
              'murat@@email.com', 'seda@email.com'],
    'telefon': ['0532-123-4567', '05321234567', '532 123 45 67', '(532) 123-45-67',
                '+90 532 123 45 67', '', '532.123.45.67', None,
                '0532 123 45 67', '532-123-45-67', '123', '0532-123-4567'],
    'maas': [5000, 6500, None, 7500, -1000, 150000, 5500, np.nan, 6000, 5800, 0, 7200],
    'baslangic_tarihi': ['2020-01-15', '2021/03/20', '15.06.2019', '2022-12-01',
                        '', '2021-13-45', '2020-02-28', None,
                        '01/01/2023', '2021-02-30', 'invalid', '2022-06-15'],
    'departman': ['IT', 'it', 'PAZARLAMA', 'Muhasebe', 'pazarlama',
                 '', 'IT', 'muhasebe', None, 'Pazarlama', 'IT', 'İK']
}

df_kirli = pd.DataFrame(kirli_data)
print("Orijinal kirli veri:")
print(df_kirli)

print(f"\nVeri şekli: {df_kirli.shape}")
print(f"Veri tipleri:\n{df_kirli.dtypes}")

# =============================================================================
# 2. EKSİK VERİ ANALİZİ
# =============================================================================

print(f"\n2. Eksik Veri Analizi")
print("-" * 30)

# Eksik veri sayısı
eksik_sayisi = df_kirli.isnull().sum()
print("Sütun başına eksik veri sayısı:")
print(eksik_sayisi)

# Eksik veri yüzdesi
eksik_yuzde = (df_kirli.isnull().sum() / len(df_kirli)) * 100
print(f"\nEksik veri yüzdeleri:")
for col, yuzde in eksik_yuzde.items():
    print(f"{col}: %{yuzde:.1f}")

# Eksik veri görselleştirmesi
plt.figure(figsize=(10, 6))
sns.heatmap(df_kirli.isnull(), cbar=True, yticklabels=False, cmap='viridis')
plt.title('Eksik Veri Haritası (Sarı: Eksik, Mor: Mevcut)')
plt.show()

# =============================================================================
# 3. İSİM TEMİZLEME
# =============================================================================

print(f"\n3. İsim Temizleme")
print("-" * 30)

df_temiz = df_kirli.copy()

# İsim temizleme fonksiyonu
def isim_temizle(isim):
    if pd.isna(isim) or isim == '':
        return np.nan
    
    # Fazla boşlukları kaldır
    isim = re.sub(r'\s+', ' ', str(isim).strip())
    
    # İlk harfleri büyük yap (Title Case)
    isim = isim.title()
    
    return isim

# İsimleri temizle
df_temiz['isim_temiz'] = df_temiz['isim'].apply(isim_temizle)

print("İsim temizleme sonuçları:")
karsilastirma = pd.DataFrame({
    'Orijinal': df_kirli['isim'],
    'Temizlenmiş': df_temiz['isim_temiz']
})
print(karsilastirma)

# =============================================================================
# 4. YAŞ VERİSİ TEMİZLEME
# =============================================================================

print(f"\n4. Yaş Verisi Temizleme")
print("-" * 30)

def yas_temizle(yas):
    if pd.isna(yas):
        return np.nan
    
    # Mantıksız değerleri kontrol et
    if yas < 0 or yas > 100:
        return np.nan
    
    return int(yas)

df_temiz['yas_temiz'] = df_temiz['yas'].apply(yas_temizle)

print("Yaş temizleme sonuçları:")
yas_karsilastirma = pd.DataFrame({
    'Orijinal': df_kirli['yas'],
    'Temizlenmiş': df_temiz['yas_temiz']
})
print(yas_karsilastirma)

# Eksik yaşları ortalama ile doldur
ortalama_yas = df_temiz['yas_temiz'].mean()
df_temiz['yas_doldurulmus'] = df_temiz['yas_temiz'].fillna(ortalama_yas)

print(f"\nOrtalama yaş ile dolduruldu: {ortalama_yas:.1f}")

# =============================================================================
# 5. EMAİL TEMİZLEME VE DOĞRULAMA
# =============================================================================

print(f"\n5. Email Temizleme ve Doğrulama")
print("-" * 30)

def email_temizle(email):
    if pd.isna(email) or email == '':
        return np.nan
    
    # Küçük harfe çevir
    email = str(email).lower().strip()
    
    # Basit email regex pattern
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(email_pattern, email):
        return email
    else:
        return np.nan

df_temiz['email_temiz'] = df_temiz['email'].apply(email_temizle)

print("Email temizleme sonuçları:")
email_karsilastirma = pd.DataFrame({
    'Orijinal': df_kirli['email'],
    'Temizlenmiş': df_temiz['email_temiz']
})
print(email_karsilastirma)

# =============================================================================
# 6. TELEFON NUMARASI TEMİZLEME
# =============================================================================

print(f"\n6. Telefon Numarası Temizleme")
print("-" * 30)

def telefon_temizle(telefon):
    if pd.isna(telefon) or telefon == '':
        return np.nan
    
    # Sadece rakamları al
    rakamlar = re.sub(r'[^\d]', '', str(telefon))
    
    # Türkiye telefon formatını kontrol et
    if len(rakamlar) == 11 and rakamlar.startswith('0'):
        # 0XXX XXX XX XX formatına çevir
        return f"0{rakamlar[1:4]} {rakamlar[4:7]} {rakamlar[7:9]} {rakamlar[9:11]}"
    elif len(rakamlar) == 10 and not rakamlar.startswith('0'):
        # Başına 0 ekle
        return f"0{rakamlar[:3]} {rakamlar[3:6]} {rakamlar[6:8]} {rakamlar[8:10]}"
    elif len(rakamlar) == 13 and rakamlar.startswith('90'):
        # +90 kodu varsa kaldır
        rakamlar = rakamlar[2:]
        return f"0{rakamlar[1:4]} {rakamlar[4:7]} {rakamlar[7:9]} {rakamlar[9:11]}"
    else:
        return np.nan

df_temiz['telefon_temiz'] = df_temiz['telefon'].apply(telefon_temizle)

print("Telefon temizleme sonuçları:")
telefon_karsilastirma = pd.DataFrame({
    'Orijinal': df_kirli['telefon'],
    'Temizlenmiş': df_temiz['telefon_temiz']
})
print(telefon_karsilastirma)

# =============================================================================
# 7. MAAŞ VERİSİ TEMİZLEME
# =============================================================================

print(f"\n7. Maaş Verisi Temizleme")
print("-" * 30)

def maas_temizle(maas):
    if pd.isna(maas):
        return np.nan
    
    # Mantıksız değerleri kontrol et (negatif veya çok yüksek)
    if maas <= 0 or maas > 100000:
        return np.nan
    
    return maas

df_temiz['maas_temiz'] = df_temiz['maas'].apply(maas_temizle)

# Aykırı değer tespiti (IQR yöntemi)
Q1 = df_temiz['maas_temiz'].quantile(0.25)
Q3 = df_temiz['maas_temiz'].quantile(0.75)
IQR = Q3 - Q1
alt_sinir = Q1 - 1.5 * IQR
ust_sinir = Q3 + 1.5 * IQR

print(f"Maaş istatistikleri:")
print(f"Q1: {Q1:.2f}")
print(f"Q3: {Q3:.2f}")
print(f"IQR: {IQR:.2f}")
print(f"Alt sınır: {alt_sinir:.2f}")
print(f"Üst sınır: {ust_sinir:.2f}")

# Aykırı değerleri işaretle
df_temiz['maas_aykiri'] = ~df_temiz['maas_temiz'].between(alt_sinir, ust_sinir)

print(f"\nAykırı değerler:")
aykiri_masalar = df_temiz[df_temiz['maas_aykiri'] == True]['maas_temiz']
print(aykiri_masalar)

# =============================================================================
# 8. TARİH VERİSİ TEMİZLEME
# =============================================================================

print(f"\n8. Tarih Verisi Temizleme")
print("-" * 30)

def tarih_temizle(tarih):
    if pd.isna(tarih) or tarih == '' or tarih == 'invalid':
        return np.nan
    
    # Farklı tarih formatlarını dene
    tarih_formatlari = ['%Y-%m-%d', '%Y/%m/%d', '%d.%m.%Y', '%d/%m/%Y']
    
    for format_str in tarih_formatlari:
        try:
            tarih_obj = datetime.strptime(str(tarih), format_str)
            # Mantıklı tarih aralığını kontrol et
            if datetime(1950, 1, 1) <= tarih_obj <= datetime.now():
                return tarih_obj.strftime('%Y-%m-%d')
        except ValueError:
            continue
    
    return np.nan

df_temiz['tarih_temiz'] = df_temiz['baslangic_tarihi'].apply(tarih_temizle)

print("Tarih temizleme sonuçları:")
tarih_karsilastirma = pd.DataFrame({
    'Orijinal': df_kirli['baslangic_tarihi'],
    'Temizlenmiş': df_temiz['tarih_temiz']
})
print(tarih_karsilastirma)

# =============================================================================
# 9. DEPARTMAN VERİSİ STANDARTLAŞTİRMA
# =============================================================================

print(f"\n9. Departman Verisi Standartlaştırma")
print("-" * 30)

def departman_temizle(departman):
    if pd.isna(departman) or departman == '':
        return np.nan
    
    # Küçük harfe çevir ve boşlukları kaldır
    departman = str(departman).lower().strip()
    
    # Departman eşleştirmesi
    departman_mapping = {
        'it': 'IT',
        'pazarlama': 'Pazarlama',
        'muhasebe': 'Muhasebe',
        'ik': 'İK'
    }
    
    return departman_mapping.get(departman, departman.title())

df_temiz['departman_temiz'] = df_temiz['departman'].apply(departman_temizle)

print("Departman temizleme sonuçları:")
departman_karsilastirma = pd.DataFrame({
    'Orijinal': df_kirli['departman'],
    'Temizlenmiş': df_temiz['departman_temiz']
})
print(departman_karsilastirma)

# =============================================================================
# 10. DUBLICATE (TEKRAR EDEN) VERİLER
# =============================================================================

print(f"\n10. Tekrar Eden Veriler")
print("-" * 30)

# Tekrar eden satırları bul
duplicate_rows = df_temiz.duplicated()
print(f"Tekrar eden satır sayısı: {duplicate_rows.sum()}")

# Belirli sütunlara göre tekrar kontrol
isim_duplicate = df_temiz.duplicated(subset=['isim_temiz'], keep=False)
print(f"Aynı isimde olanlar: {isim_duplicate.sum()}")

if isim_duplicate.sum() > 0:
    print("Aynı isimli kayıtlar:")
    print(df_temiz[isim_duplicate][['isim_temiz', 'email_temiz']])

# =============================================================================
# 11. VERİ TİPİ DÖNÜŞTÜRMELERİ
# =============================================================================

print(f"\n11. Veri Tipi Dönüştürmeleri")
print("-" * 30)

# Temizlenmiş verileri doğru tiplere çevir
df_final = df_temiz.copy()

# Tarihi datetime'a çevir
df_final['tarih_temiz'] = pd.to_datetime(df_final['tarih_temiz'], errors='coerce')

# Yaşı integer'a çevir
df_final['yas_doldurulmus'] = df_final['yas_doldurulmus'].astype('int64')

# Departmanı kategori yap
df_final['departman_temiz'] = df_final['departman_temiz'].astype('category')

print("Final veri tipleri:")
print(df_final[['isim_temiz', 'yas_doldurulmus', 'email_temiz', 
               'telefon_temiz', 'maas_temiz', 'tarih_temiz', 'departman_temiz']].dtypes)

# =============================================================================
# 12. TEMİZLEME ÖZETİ VE KARŞILAŞTIRMA
# =============================================================================

print(f"\n12. Temizleme Özeti")
print("-" * 30)

# Temizleme öncesi ve sonrası karşılaştırma
print("Temizleme öncesi eksik veri:")
print(df_kirli.isnull().sum())

print(f"\nTemizleme sonrası eksik veri:")
temiz_sutunlar = ['isim_temiz', 'yas_doldurulmus', 'email_temiz', 
                 'telefon_temiz', 'maas_temiz', 'tarih_temiz', 'departman_temiz']
print(df_final[temiz_sutunlar].isnull().sum())

# Veri kalitesi raporu
def veri_kalitesi_raporu(df_once, df_sonra):
    rapor = {}
    
    for col in df_once.columns:
        if col in ['isim', 'yas', 'email', 'telefon', 'maas', 'baslangic_tarihi', 'departman']:
            temiz_col = col + '_temiz' if col != 'yas' else 'yas_doldurulmus'
            if col == 'baslangic_tarihi':
                temiz_col = 'tarih_temiz'
            
            once_eksik = df_once[col].isnull().sum()
            sonra_eksik = df_sonra[temiz_col].isnull().sum() if temiz_col in df_sonra.columns else len(df_sonra)
            
            rapor[col] = {
                'önceki_eksik': once_eksik,
                'sonraki_eksik': sonra_eksik,
                'iyileştirme': once_eksik - sonra_eksik
            }
    
    return rapor

kalite_raporu = veri_kalitesi_raporu(df_kirli, df_final)

print(f"\nVeri Kalitesi Raporu:")
for sutun, metrics in kalite_raporu.items():
    print(f"{sutun}:")
    print(f"  Önceki eksik: {metrics['önceki_eksik']}")
    print(f"  Sonraki eksik: {metrics['sonraki_eksik']}")
    print(f"  İyileştirme: {metrics['iyileştirme']}")

# =============================================================================
# 13. TEMİZ VERİYİ GÖRSELLEŞTIRME
# =============================================================================

print(f"\n13. Temiz Veri Görselleştirme")
print("-" * 30)

fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 1. Yaş dağılımı
axes[0, 0].hist(df_final['yas_doldurulmus'], bins=10, alpha=0.7, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Yaş Dağılımı (Temizlenmiş)')
axes[0, 0].set_xlabel('Yaş')
axes[0, 0].set_ylabel('Frekans')

# 2. Departman dağılımı
dept_counts = df_final['departman_temiz'].value_counts()
axes[0, 1].pie(dept_counts.values, labels=dept_counts.index, autopct='%1.1f%%')
axes[0, 1].set_title('Departman Dağılımı')

# 3. Maaş kutu grafiği
df_final.boxplot(column='maas_temiz', by='departman_temiz', ax=axes[1, 0])
axes[1, 0].set_title('Departmanlara Göre Maaş Dağılımı')
axes[1, 0].set_ylabel('Maaş')

# 4. Yaş vs Maaş
scatter = axes[1, 1].scatter(df_final['yas_doldurulmus'], df_final['maas_temiz'], 
                           c=pd.Categorical(df_final['departman_temiz']).codes, 
                           cmap='viridis', alpha=0.7, s=100)
axes[1, 1].set_title('Yaş vs Maaş (Departmana Göre Renkli)')
axes[1, 1].set_xlabel('Yaş')
axes[1, 1].set_ylabel('Maaş')

plt.tight_layout()
plt.show()

# =============================================================================
# 14. TEMİZ VERİYİ KAYDETME
# =============================================================================

print(f"\n14. Temiz Veriyi Kaydetme")
print("-" * 30)

# Sadece temizlenmiş sütunları al
final_df = df_final[['id'] + temiz_sutunlar].copy()

# Sütun isimlerini düzenle
final_df.columns = ['id', 'isim', 'yas', 'email', 'telefon', 'maas', 'baslangic_tarihi', 'departman']

print("Final temizlenmiş veri:")
print(final_df)

# CSV'ye kaydet
final_df.to_csv('temizlenmis_veri.csv', index=False, encoding='utf-8')
print(f"\nTemizlenmiş veri 'temizlenmis_veri.csv' dosyasına kaydedildi.")

print("\n🎯 Veri Temizleme Özeti:")
print("✅ Eksik veri analizi ve görselleştirme")
print("✅ İsim standardizasyonu")
print("✅ Yaş verisi doğrulama ve doldurma")
print("✅ Email formatı doğrulama")
print("✅ Telefon numarası standardizasyonu")
print("✅ Maaş verisi temizleme ve aykırı değer tespiti")
print("✅ Tarih formatı standardizasyonu")
print("✅ Kategori verisi eşleştirme")
print("✅ Tekrar eden veri kontrolü")
print("✅ Veri tipi dönüştürmeleri")
print("✅ Kalite raporu ve görselleştirme")