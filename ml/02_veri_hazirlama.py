
import pandas as pd
from pathlib import Path

PROJE_DIZINI = Path(__file__).resolve().parent
VERI_DOSYASI = PROJE_DIZINI / "data" / "raw" / "used_cars_kaggle.csv"
CIKTI_DIZINI = PROJE_DIZINI / "data" / "processed"

CIKTI_DIZINI.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(VERI_DOSYASI)

print("=" * 60)
print("VERİ HAZIRLAMA İŞLEMİ")
print("=" * 60)

print("\nBaşlangıç veri boyutu:", df.shape)

df["price"] = (
    df["price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["price"] = pd.to_numeric(df["price"], errors="coerce")

df["milage"] = (
    df["milage"]
    .astype(str)
    .str.replace(" mi.", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["milage"] = pd.to_numeric(df["milage"], errors="coerce")

df = df.dropna(subset=["price", "milage"])

df = df[df["price"] > 0]
df = df[df["model_year"].between(1980, 2026)]
df = df[df["milage"] >= 0]

kategorik_sutunlar = [
    "brand",
    "model",
    "fuel_type",
    "engine",
    "transmission",
    "ext_col",
    "int_col",
    "accident",
    "clean_title",
]

for sutun in kategorik_sutunlar:
    df[sutun] = df[sutun].fillna("Unknown")

cikti_dosyasi = CIKTI_DIZINI / "used_cars_clean.csv"
df.to_csv(cikti_dosyasi, index=False)

print("\nTemizleme sonrası veri boyutu:", df.shape)

print("\nFiyat sütununun veri tipi:", df["price"].dtype)
print("Kilometre sütununun veri tipi:", df["milage"].dtype)

print("\nFiyat istatistikleri:")
print(df["price"].describe())

print("\nKilometre istatistikleri:")
print(df["milage"].describe())

print("\nEksik değerler:")
print(df.isnull().sum())

print("\nTemizlenmiş veri seti kaydedildi:")
print(cikti_dosyasi)
