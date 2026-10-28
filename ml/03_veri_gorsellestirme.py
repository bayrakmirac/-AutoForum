
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


PROJE_DIZINI = Path(__file__).resolve().parent
VERI_DOSYASI = (
    PROJE_DIZINI
    / "data"
    / "processed"
    / "used_cars_clean.csv"
)

CIKTI_DIZINI = PROJE_DIZINI / "reports" / "figures"
CIKTI_DIZINI.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(VERI_DOSYASI)

df["vehicle_age"] = 2026 - df["model_year"]

plt.figure(figsize=(10, 6))
plt.hist(df["price"], bins=50)
plt.title("İkinci El Araç Fiyatlarının Dağılımı")
plt.xlabel("Fiyat ($)")
plt.ylabel("Araç Sayısı")
plt.tight_layout()

plt.savefig(
    CIKTI_DIZINI / "01_fiyat_dagilimi.png",
    dpi=300
)
plt.show()


plt.figure(figsize=(10, 5))
plt.boxplot(df["price"], vert=False)
plt.title("Araç Fiyatları - Aykırı Değer İncelemesi")
plt.xlabel("Fiyat ($)")
plt.tight_layout()

plt.savefig(
    CIKTI_DIZINI / "02_fiyat_boxplot.png",
    dpi=300
)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(
    df["milage"],
    df["price"],
    alpha=0.5
)
plt.title("Kilometre ve Araç Fiyatı İlişkisi")
plt.xlabel("Kilometre (mil)")
plt.ylabel("Fiyat ($)")
plt.tight_layout()

plt.savefig(
    CIKTI_DIZINI / "03_kilometre_fiyat.png",
    dpi=300
)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(
    df["vehicle_age"],
    df["price"],
    alpha=0.5
)
plt.title("Araç Yaşı ve Araç Fiyatı İlişkisi")
plt.xlabel("Araç Yaşı (yıl)")
plt.ylabel("Fiyat ($)")
plt.tight_layout()

plt.savefig(
    CIKTI_DIZINI / "04_yas_fiyat.png",
    dpi=300
)
plt.show()

print("=" * 60)
print("GÖRSELLEŞTİRME VE VERİ ANALİZİ")
print("=" * 60)

print("\nFiyat yüzdelikleri:")
print(df["price"].quantile([0.25, 0.50, 0.75, 0.90, 0.95, 0.99]))

print("\nEn pahalı 10 araç:")
print(
    df[
        ["brand", "model", "model_year", "milage", "price"]
    ]
    .sort_values("price", ascending=False)
    .head(10)
    .to_string(index=False)
)

print("\nFiyat ve kilometre korelasyonu:")
print(df["price"].corr(df["milage"]))

print("\nGrafikler kaydedildi:")
print(CIKTI_DIZINI)
