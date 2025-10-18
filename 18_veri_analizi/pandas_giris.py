"""
Pandas Giriş - DataFrame Kullanımı
Pandas kütüphanesinin temel özelliklerini ve DataFrame işlemlerini öğreniyoruz.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

print("=== Pandas DataFrame Kullanımı ===\n")

# =============================================================================
# 1. DATAFRAME OLUŞTURMA
# =============================================================================

print("1. DataFrame Oluşturma")
print("-" * 30)

# Sözlükten DataFrame
data_dict = {
    'Isim': ['Ahmet', 'Ayşe', 'Mehmet', 'Fatma', 'Ali', 'Zeynep'],
    'Yas': [25, 30, 35, 28, 32, 27],
    'Sehir': ['Istanbul', 'Ankara', 'Izmir', 'Bursa', 'Antalya', 'Adana'],
    'Maas': [5000, 6500, 7500, 5500, 6000, 5800],
    'Departman': ['IT', 'Pazarlama', 'Muhasebe', 'IT', 'Pazarlama', 'Muhasebe']
}

df = pd.DataFrame(data_dict)
print("Sözlükten oluşturulan DataFrame:")
print(df)
print(f"\nDataFrame şekli: {df.shape}")

# Listelerden DataFrame
columns = ['A', 'B', 'C']
data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df_list = pd.DataFrame(data_list, columns=columns)
print(f"\nListelerden DataFrame:\n{df_list}")

# NumPy array'den DataFrame
np.random.seed(42)
arr = np.random.randn(4, 3)
df_numpy = pd.DataFrame(arr, 
                       columns=['X', 'Y', 'Z'],
                       index=['Satır1', 'Satır2', 'Satır3', 'Satır4'])
print(f"\nNumPy array'den DataFrame:\n{df_numpy}")

# =============================================================================
# 2. DATAFRAME BİLGİLERİ
# =============================================================================

print(f"\n2. DataFrame Bilgileri")
print("-" * 30)

print("DataFrame.info():")
df.info()

print("\nDataFrame.describe():")
print(df.describe())

print(f"\nSütun isimleri: {list(df.columns)}")
print(f"İndeks: {list(df.index)}")
print(f"Veri tipleri:\n{df.dtypes}")

# Null değer kontrolü
print(f"\nNull değerler:\n{df.isnull().sum()}")

# =============================================================================
# 3. VERİ SEÇME VE FİLTRELEME
# =============================================================================

print(f"\n3. Veri Seçme ve Filtreleme")
print("-" * 30)

# Tek sütun seçme
print("İsimler:")
print(df['Isim'])

# Birden fazla sütun seçme
print(f"\nİsim ve Maaş:")
print(df[['Isim', 'Maas']])

# İlk/son satırlar
print(f"\nİlk 3 satır:")
print(df.head(3))

print(f"\nSon 2 satır:")
print(df.tail(2))

# Koşullu filtreleme
yuksek_maas = df[df['Maas'] > 6000]
print(f"\nMaaşı 6000'den fazla olanlar:")
print(yuksek_maas)

# Birden fazla koşul
it_ve_yuksek_maas = df[(df['Departman'] == 'IT') & (df['Maas'] > 5000)]
print(f"\nIT departmanında maaşı 5000'den fazla olanlar:")
print(it_ve_yuksek_maas)

# İçerme kontrolü
istanbul_ankara = df[df['Sehir'].isin(['Istanbul', 'Ankara'])]
print(f"\nİstanbul veya Ankara'da yaşayanlar:")
print(istanbul_ankara)

# =============================================================================
# 4. VERİ SIRALAMA VE GRUPLAMAa
# =============================================================================

print(f"\n4. Veri Sıralama ve Gruplama")
print("-" * 30)

# Sıralama
maas_sirali = df.sort_values('Maas', ascending=False)
print("Maaşa göre azalan sırada:")
print(maas_sirali)

# Birden fazla sütuna göre sıralama
coklu_sirali = df.sort_values(['Departman', 'Maas'], ascending=[True, False])
print(f"\nDepartman ve maaşa göre sıralı:")
print(coklu_sirali)

# Gruplama
dept_group = df.groupby('Departman')
print(f"\nDepartmanlara göre ortalama maaş:")
print(dept_group['Maas'].mean())

print(f"\nDepartmanlara göre istatistikler:")
print(dept_group.agg({
    'Maas': ['mean', 'min', 'max'],
    'Yas': 'mean'
}))

# =============================================================================
# 5. YENİ SÜTUN EKLEME VE VERİ DÖNÜŞTÜRME
# =============================================================================

print(f"\n5. Yeni Sütun Ekleme ve Veri Dönüştürme")
print("-" * 30)

# Yeni sütun ekleme
df['Yillik_Maas'] = df['Maas'] * 12
df['Yas_Grubu'] = df['Yas'].apply(lambda x: 'Genç' if x < 30 else 'Orta Yaş' if x < 35 else 'Yaşlı')

print("Yeni sütunlar eklendi:")
print(df[['Isim', 'Maas', 'Yillik_Maas', 'Yas_Grubu']])

# Koşullu değer atama
df['Performans'] = np.where(df['Maas'] > 6000, 'Yüksek', 'Normal')

# Kategorik veri dönüştürme
df['Sehir_Kodu'] = df['Sehir'].map({
    'Istanbul': 'IST',
    'Ankara': 'ANK', 
    'Izmir': 'IZM',
    'Bursa': 'BUR',
    'Antalya': 'ANT',
    'Adana': 'ADA'
})

print(f"\nDönüştürülmüş veriler:")
print(df[['Sehir', 'Sehir_Kodu', 'Performans']])

# =============================================================================
# 6. EKSİK VERİ YÖNETİMİ
# =============================================================================

print(f"\n6. Eksik Veri Yönetimi")
print("-" * 30)

# Eksik veri ekleme (test için)
df_eksik = df.copy()
df_eksik.loc[1, 'Maas'] = np.nan
df_eksik.loc[3, 'Yas'] = np.nan
df_eksik.loc[5, 'Departman'] = np.nan

print("Eksik veriler:")
print(df_eksik.isnull().sum())

# Eksik verileri doldurma
df_doldurulmus = df_eksik.copy()

# Sayısal verileri ortalama ile doldur
df_doldurulmus['Maas'].fillna(df_doldurulmus['Maas'].mean(), inplace=True)
df_doldurulmus['Yas'].fillna(df_doldurulmus['Yas'].median(), inplace=True)

# Kategorik verileri mod ile doldur
df_doldurulmus['Departman'].fillna(df_doldurulmus['Departman'].mode()[0], inplace=True)

print(f"\nDoldurma sonrası eksik veriler:")
print(df_doldurulmus.isnull().sum())

# Eksik satırları silme
df_silindi = df_eksik.dropna()
print(f"\nEksik satırlar silindi - yeni boyut: {df_silindi.shape}")

# =============================================================================
# 7. ZAMAN SERİSİ VERİLERİ
# =============================================================================

print(f"\n7. Zaman Serisi Verileri")
print("-" * 30)

# Tarih aralığı oluşturma
tarih_araligi = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')

# Zaman serisi DataFrame'i
np.random.seed(42)
zaman_serisi = pd.DataFrame({
    'Tarih': tarih_araligi,
    'Satış': np.random.randint(100, 1000, len(tarih_araligi)),
    'Maliyet': np.random.randint(50, 500, len(tarih_araligi))
})

# Tarih sütununu indeks yapma
zaman_serisi.set_index('Tarih', inplace=True)

print("Zaman serisi verisi:")
print(zaman_serisi.head())

# Kar hesaplama
zaman_serisi['Kar'] = zaman_serisi['Satış'] - zaman_serisi['Maliyet']

# Aylık toplam
aylik_toplam = zaman_serisi.resample('M').sum()
print(f"\nAylık toplam (ilk 5 ay):")
print(aylik_toplam.head())

# Hareketli ortalama
zaman_serisi['Satış_MA7'] = zaman_serisi['Satış'].rolling(window=7).mean()

print(f"\n7 günlük hareketli ortalama:")
print(zaman_serisi[['Satış', 'Satış_MA7']].head(10))

# =============================================================================
# 8. VERİ BİRLEŞTİRME
# =============================================================================

print(f"\n8. Veri Birleştirme")
print("-" * 30)

# İkinci DataFrame oluşturma
df_proje = pd.DataFrame({
    'Isim': ['Ahmet', 'Ayşe', 'Mehmet', 'Can'],
    'Proje_Sayisi': [3, 5, 2, 4],
    'Son_Proje_Tarihi': ['2024-01-15', '2024-02-20', '2024-01-30', '2024-03-10']
})

print("Proje DataFrame:")
print(df_proje)

# Inner join
inner_join = pd.merge(df, df_proje, on='Isim', how='inner')
print(f"\nInner join:")
print(inner_join[['Isim', 'Departman', 'Maas', 'Proje_Sayisi']])

# Left join
left_join = pd.merge(df, df_proje, on='Isim', how='left')
print(f"\nLeft join (eksik projeler NaN):")
print(left_join[['Isim', 'Proje_Sayisi']].fillna('Proje Yok'))

# =============================================================================
# 9. VERİ DIŞA AKTARMA VE İÇE AKTARMA
# =============================================================================

print(f"\n9. Veri Dışa/İçe Aktarma")
print("-" * 30)

# CSV'ye kaydetme
df.to_csv('calisan_verileri.csv', index=False, encoding='utf-8')
print("Veri CSV dosyasına kaydedildi: calisan_verileri.csv")

# CSV'den okuma (simüle)
try:
    df_okunan = pd.read_csv('calisan_verileri.csv', encoding='utf-8')
    print(f"CSV'den okunan veri boyutu: {df_okunan.shape}")
except FileNotFoundError:
    print("CSV dosyası henüz oluşturulmadı")

# JSON'a kaydetme
df.to_json('calisan_verileri.json', orient='records', indent=2)
print("Veri JSON dosyasına kaydedildi: calisan_verileri.json")

# =============================================================================
# 10. VERİ ANALİZİ ÖRNEKLERİ
# =============================================================================

print(f"\n10. Veri Analizi Örnekleri")
print("-" * 30)

# Korelasyon analizi
sayisal_df = df.select_dtypes(include=[np.number])
korelasyon = sayisal_df.corr()
print("Korelasyon matrisi:")
print(korelasyon)

# Pivot tablo
pivot_tablo = df.pivot_table(
    values='Maas',
    index='Departman',
    columns='Yas_Grubu',
    aggfunc='mean',
    fill_value=0
)
print(f"\nPivot tablo (Departman x Yaş Grubu ortalaması):")
print(pivot_tablo)

# Değer sayımları
print(f"\nDepartman dağılımı:")
print(df['Departman'].value_counts())

print(f"\nŞehir dağılımı yüzdeleri:")
print(df['Sehir'].value_counts(normalize=True) * 100)

# İstatistiksel özetler
print(f"\nMaaş istatistikleri:")
print(f"Ortalama: {df['Maas'].mean():.2f}")
print(f"Medyan: {df['Maas'].median():.2f}")
print(f"Standart sapma: {df['Maas'].std():.2f}")
print(f"Min: {df['Maas'].min()}")
print(f"Max: {df['Maas'].max()}")

# =============================================================================
# 11. VİZUALİZASYON
# =============================================================================

print(f"\n11. Temel Görselleştirme")
print("-" * 30)

# Matplotlib ile görselleştirme
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Histogram
axes[0, 0].hist(df['Maas'], bins=8, alpha=0.7, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Maaş Dağılımı')
axes[0, 0].set_xlabel('Maaş')
axes[0, 0].set_ylabel('Frekans')

# Bar plot
dept_counts = df['Departman'].value_counts()
axes[0, 1].bar(dept_counts.index, dept_counts.values, color=['red', 'green', 'blue'])
axes[0, 1].set_title('Departman Dağılımı')
axes[0, 1].set_ylabel('Kişi Sayısı')

# Scatter plot
axes[1, 0].scatter(df['Yas'], df['Maas'], alpha=0.7, s=100)
axes[1, 0].set_title('Yaş vs Maaş')
axes[1, 0].set_xlabel('Yaş')
axes[1, 0].set_ylabel('Maaş')

# Box plot
dept_maas = [df[df['Departman'] == dept]['Maas'].values for dept in df['Departman'].unique()]
axes[1, 1].boxplot(dept_maas, labels=df['Departman'].unique())
axes[1, 1].set_title('Departmanlara Göre Maaş Dağılımı')
axes[1, 1].set_ylabel('Maaş')

plt.tight_layout()
plt.show()

# Pandas plotting
df.groupby('Departman')['Maas'].mean().plot(kind='bar', 
                                           title='Departmanlara Göre Ortalama Maaş',
                                           color='lightcoral')
plt.ylabel('Ortalama Maaş')
plt.xticks(rotation=45)
plt.show()

print("\n🎯 Pandas DataFrame Özeti:")
print("✅ DataFrame oluşturma ve temel bilgiler")
print("✅ Veri seçme, filtreleme ve sıralama")
print("✅ Gruplama ve toplama işlemleri")
print("✅ Yeni sütun ekleme ve dönüştürme")
print("✅ Eksik veri yönetimi")
print("✅ Zaman serisi işlemleri")
print("✅ Veri birleştirme (join/merge)")
print("✅ Dosya I/O işlemleri")
print("✅ İstatistiksel analiz")
print("✅ Temel görselleştirme")