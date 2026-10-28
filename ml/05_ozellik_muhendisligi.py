
import pandas as pd
import re

from pathlib import Path



PROJE_DIZINI = Path(__file__).resolve().parent

GIRIS_DOSYASI = (
    PROJE_DIZINI
    / "data"
    / "processed"
    / "used_cars_clean.csv"
)

CIKTI_DOSYASI = (
    PROJE_DIZINI
    / "data"
    / "processed"
    / "used_cars_features.csv"
)



df = pd.read_csv(GIRIS_DOSYASI)

print("=" * 65)
print("ÖZELLİK MÜHENDİSLİĞİ")
print("=" * 65)

print("\nBaşlangıç veri boyutu:", df.shape)

REFERANS_YILI = 2026

df["vehicle_age"] = (
    REFERANS_YILI - df["model_year"]
)

# Gelecekteki model yılları için negatif yaş oluşmasını önle.
df["vehicle_age"] = df["vehicle_age"].clip(lower=0)


def motor_hacmi_bul(metin):
    """
    Motor açıklamasından litre cinsinden hacmi çıkarır.

    Örnek:
    '300.0HP 3.7L V6 Cylinder Engine' -> 3.7
    '2.0L I4 16V GDI DOHC Turbo' -> 2.0
    """

    if pd.isna(metin):
        return None

    metin = str(metin)

    eslesme = re.search(
        r"(\d+(?:\.\d+)?)\s*L\b",
        metin,
        flags=re.IGNORECASE
    )

    if eslesme:
        return float(eslesme.group(1))

    return None


df["engine_liters"] = df["engine"].apply(
    motor_hacmi_bul
)


def motor_gucu_bul(metin):
    """
    Motor açıklamasındaki HP değerini çıkarır.

    Örnek:
    '300.0HP 3.7L V6 Cylinder Engine' -> 300.0

    Açıklamada HP değeri yoksa None döndürür.
    """

    if pd.isna(metin):
        return None

    metin = str(metin)

    eslesme = re.search(
        r"(\d+(?:\.\d+)?)\s*HP\b",
        metin,
        flags=re.IGNORECASE
    )

    if eslesme:
        return float(eslesme.group(1))

    return None


df["engine_hp"] = df["engine"].apply(
    motor_gucu_bul
)


print("\nYeni özellikler oluşturuldu.")

print("\nYeni özelliklerdeki eksik değerler:")
print(
    df[
        ["vehicle_age", "engine_liters", "engine_hp"]
    ].isnull().sum()
)

print("\nYeni özelliklerin istatistikleri:")
print(
    df[
        ["vehicle_age", "engine_liters", "engine_hp"]
    ].describe()
)

print("\nÖrnek kayıtlar:")

print(
    df[
        [
            "brand",
            "model",
            "model_year",
            "vehicle_age",
            "engine",
            "engine_liters",
            "engine_hp",
            "price",
        ]
    ]
    .head(10)
    .to_string(index=False)
)

df.to_csv(
    CIKTI_DOSYASI,
    index=False
)

print("\n" + "=" * 65)
print("ÖZELLİK MÜHENDİSLİĞİ TAMAMLANDI")
print("=" * 65)

print("\nYeni veri seti:")
print(CIKTI_DOSYASI)

print("\nSon veri boyutu:", df.shape)

