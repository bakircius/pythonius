"""
Veri Görselleştirme ve Analiz Projesi
Gerçek bir veri seti ile kapsamlı analiz örneği
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# 1. VERİ SETİ OLUŞTURMA (Gerçek veri simülasyonu)
# =============================================================================

print("=== Satış Veri Seti Analizi ===\n")

# Örnek e-ticaret satış verisi oluşturma
np.random.seed(42)

# Tarih aralığı
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Ürün kategorileri
kategoriler = ['Elektronik', 'Giyim', 'Kitap', 'Ev & Yaşam', 'Spor']
sehirler = ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya', 'Adana']

# Veri seti oluşturma
n_records = 5000
data = {
    'Tarih': np.random.choice(date_range, n_records),
    'Kategori': np.random.choice(kategoriler, n_records),
    'Şehir': np.random.choice(sehirler, n_records),
    'Satış_Miktarı': np.random.randint(1, 20, n_records),
    'Birim_Fiyat': np.random.uniform(10, 500, n_records).round(2),
    'Müşteri_Yaşı': np.random.randint(18, 65, n_records),
    'İndirim_Oranı': np.random.choice([0, 0.1, 0.15, 0.2, 0.25], n_records)
}

df = pd.DataFrame(data)

# Toplam satış tutarı hesaplama
df['Toplam_Tutar'] = df['Satış_Miktarı'] * df['Birim_Fiyat'] * (1 - df['İndirim_Oranı'])

print("Veri seti oluşturuldu:")
print(f"Toplam kayıt sayısı: {len(df)}")
print(f"Tarih aralığı: {df['Tarih'].min()} - {df['Tarih'].max()}")
print("\nİlk 5 kayıt:")
print(df.head())

# =============================================================================
# 2. VERİ KEŞİF ANALİZİ (EDA)
# =============================================================================

print("\n=== Veri Keşif Analizi ===\n")

# Temel istatistikler
print("Sayısal değişkenler için özet istatistikler:")
print(df.describe())

print(f"\nKategorik değişkenlerin dağılımı:")
print(f"Kategori dağılımı:\n{df['Kategori'].value_counts()}")
print(f"\nŞehir dağılımı:\n{df['Şehir'].value_counts()}")

# Eksik değer kontrolü
print(f"\nEksik değer analizi:")
print(df.isnull().sum())

# =============================================================================
# 3. VERİ TEMİZLEME VE DÖNÜŞTürme
# =============================================================================

print("\n=== Veri Temizleme ===\n")

# Tarih sütununu datetime'a çevirme
df['Tarih'] = pd.to_datetime(df['Tarih'])

# Yeni zaman özellikli sütunlar ekleme
df['Yıl'] = df['Tarih'].dt.year
df['Ay'] = df['Tarih'].dt.month
df['Gün'] = df['Tarih'].dt.day
df['Haftanın_Günü'] = df['Tarih'].dt.day_name()
df['Çeyrek'] = df['Tarih'].dt.quarter

# Yaş grupları oluşturma
def yas_grubu(yas):
    if yas < 25:
        return 'Genç (18-24)'
    elif yas < 35:
        return 'Genç Yetişkin (25-34)'
    elif yas < 45:
        return 'Orta Yaş (35-44)'
    elif yas < 55:
        return 'Olgun (45-54)'
    else:
        return 'Yaşlı (55+)'

df['Yaş_Grubu'] = df['Müşteri_Yaşı'].apply(yas_grubu)

# Fiyat kategorileri
def fiyat_kategorisi(fiyat):
    if fiyat < 50:
        return 'Düşük'
    elif fiyat < 200:
        return 'Orta'
    else:
        return 'Yüksek'

df['Fiyat_Kategorisi'] = df['Birim_Fiyat'].apply(fiyat_kategorisi)

print("Yeni özellikler eklendi:")
print(df[['Tarih', 'Ay', 'Yaş_Grubu', 'Fiyat_Kategorisi']].head())

# =============================================================================
# 4. DETAYLI ANALİZ VE GÖRSELLEŞTİRME
# =============================================================================

print("\n=== Detaylı Analiz ===\n")

# Aylık satış trendi
monthly_sales = df.groupby('Ay').agg({
    'Toplam_Tutar': 'sum',
    'Satış_Miktarı': 'sum'
}).reset_index()

print("Aylık satış özeti:")
print(monthly_sales)

# Kategori bazlı analiz
category_analysis = df.groupby('Kategori').agg({
    'Toplam_Tutar': ['sum', 'mean'],
    'Satış_Miktarı': 'sum',
    'Müşteri_Yaşı': 'mean'
}).round(2)

print("\nKategori bazlı analiz:")
print(category_analysis)

# Şehir bazlı performans
city_performance = df.groupby('Şehir')['Toplam_Tutar'].agg(['sum', 'mean', 'count']).round(2)
print("\nŞehir bazlı performans:")
print(city_performance.sort_values('sum', ascending=False))

# =============================================================================
# 5. GÖRSELLEŞTİRME PANELİ
# =============================================================================

print("\n=== Görselleştirme Paneli Oluşturuluyor ===\n")

# Ana görselleştirme paneli
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('E-Ticaret Satış Analizi Dashboard', fontsize=16, fontweight='bold')

# 1. Aylık satış trendi
axes[0, 0].plot(monthly_sales['Ay'], monthly_sales['Toplam_Tutar'], marker='o', linewidth=2)
axes[0, 0].set_title('Aylık Satış Trendi')
axes[0, 0].set_xlabel('Ay')
axes[0, 0].set_ylabel('Toplam Tutar (TL)')
axes[0, 0].grid(True, alpha=0.3)

# 2. Kategori bazlı satış dağılımı
category_sales = df.groupby('Kategori')['Toplam_Tutar'].sum().sort_values(ascending=True)
axes[0, 1].barh(category_sales.index, category_sales.values)
axes[0, 1].set_title('Kategorilere Göre Toplam Satış')
axes[0, 1].set_xlabel('Toplam Tutar (TL)')

# 3. Şehir bazlı satış haritası (bar chart)
city_sales = df.groupby('Şehir')['Toplam_Tutar'].sum().sort_values(ascending=False)
axes[0, 2].bar(city_sales.index, city_sales.values, color='lightcoral')
axes[0, 2].set_title('Şehirlere Göre Satış')
axes[0, 2].set_xlabel('Şehir')
axes[0, 2].set_ylabel('Toplam Tutar (TL)')
axes[0, 2].tick_params(axis='x', rotation=45)

# 4. Yaş grubu dağılımı
age_dist = df['Yaş_Grubu'].value_counts()
axes[1, 0].pie(age_dist.values, labels=age_dist.index, autopct='%1.1f%%', startangle=90)
axes[1, 0].set_title('Müşteri Yaş Grubu Dağılımı')

# 5. Fiyat vs Satış Miktarı ilişkisi
scatter = axes[1, 1].scatter(df['Birim_Fiyat'], df['Satış_Miktarı'], 
                           c=df['Toplam_Tutar'], cmap='viridis', alpha=0.6)
axes[1, 1].set_title('Fiyat vs Satış Miktarı')
axes[1, 1].set_xlabel('Birim Fiyat (TL)')
axes[1, 1].set_ylabel('Satış Miktarı')
plt.colorbar(scatter, ax=axes[1, 1], label='Toplam Tutar')

# 6. İndirim oranına göre satış performansı
discount_sales = df.groupby('İndirim_Oranı')['Toplam_Tutar'].mean()
axes[1, 2].bar(discount_sales.index, discount_sales.values, color='lightgreen')
axes[1, 2].set_title('İndirim Oranına Göre Ortalama Satış')
axes[1, 2].set_xlabel('İndirim Oranı')
axes[1, 2].set_ylabel('Ortalama Toplam Tutar (TL)')

plt.tight_layout()
plt.show()

# =============================================================================
# 6. İLERİ İSTATİSTİKSEL ANALİZ
# =============================================================================

print("\n=== İleri İstatistiksel Analiz ===\n")

# Korelasyon analizi
numeric_columns = ['Satış_Miktarı', 'Birim_Fiyat', 'Müşteri_Yaşı', 'İndirim_Oranı', 'Toplam_Tutar']
correlation_matrix = df[numeric_columns].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, square=True)
plt.title('Değişkenler Arası Korelasyon Matrisi')
plt.tight_layout()
plt.show()

print("Korelasyon matrisi:")
print(correlation_matrix)

# Kategorik değişkenler arası ilişki
plt.figure(figsize=(14, 10))

# Kategori ve şehir bazlı heatmap
pivot_table = df.pivot_table(values='Toplam_Tutar', index='Kategori', columns='Şehir', aggfunc='sum')
sns.heatmap(pivot_table, annot=True, fmt='.0f', cmap='YlOrRd')
plt.title('Kategori ve Şehir Bazlı Satış Haritası')
plt.tight_layout()
plt.show()

# =============================================================================
# 7. ÖNGÖRÜSEL ANALİZ VE RAPOR
# =============================================================================

print("\n=== Öngörüsel Analiz ve İş Zekası ===\n")

# En başarılı kombinasyonlar
top_combinations = df.groupby(['Kategori', 'Şehir', 'Yaş_Grubu']).agg({
    'Toplam_Tutar': 'sum',
    'Satış_Miktarı': 'count'
}).reset_index().sort_values('Toplam_Tutar', ascending=False)

print("En karlı kategori-şehir-yaş grubu kombinasyonları:")
print(top_combinations.head(10))

# Performans metrikleri
total_revenue = df['Toplam_Tutar'].sum()
total_orders = len(df)
avg_order_value = df['Toplam_Tutar'].mean()
top_category = df.groupby('Kategori')['Toplam_Tutar'].sum().idxmax()
top_city = df.groupby('Şehir')['Toplam_Tutar'].sum().idxmax()

print(f"\n📊 KPI Dashboard:")
print(f"{'='*40}")
print(f"Toplam Gelir: {total_revenue:,.2f} TL")
print(f"Toplam Sipariş: {total_orders:,}")
print(f"Ortalama Sipariş Değeri: {avg_order_value:.2f} TL")
print(f"En Başarılı Kategori: {top_category}")
print(f"En Başarılı Şehir: {top_city}")

# Trend analizi
monthly_growth = monthly_sales['Toplam_Tutar'].pct_change().fillna(0) * 100
print(f"\nAylık Büyüme Oranları (%):")
for i, growth in enumerate(monthly_growth[1:], 1):
    print(f"Ay {i+1}: %{growth:.1f}")

# Sezonallik analizi
seasonal_analysis = df.groupby('Çeyrek')['Toplam_Tutar'].sum()
print(f"\nÇeyreklik Satış Performansı:")
for quarter, sales in seasonal_analysis.items():
    print(f"Q{quarter}: {sales:,.2f} TL")

print(f"\n🎯 Öneriler:")
print("1. En karlı kategorilere odaklanın")
print("2. Düşük performanslı şehirlerde pazarlama artırın")
print("3. İndirim stratejisini optimize edin")
print("4. Mevsimsel trendleri takip edin")
print("5. Müşteri yaş gruplarına özel kampanyalar düzenleyin")

print("\n🎉 Kapsamlı veri analizi tamamlandı!")