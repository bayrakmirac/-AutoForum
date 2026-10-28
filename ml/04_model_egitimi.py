
import pandas as pd
import joblib

from pathlib import Path
from time import perf_counter

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, HistGradientBoostingRegressor

PROJE_DIZINI = Path(__file__).resolve().parent

VERI_DOSYASI = (
    PROJE_DIZINI
    / "data"
    / "processed"
    / "used_cars_clean.csv"
)

MODEL_DIZINI = PROJE_DIZINI / "models"
RAPOR_DIZINI = PROJE_DIZINI / "reports"

MODEL_DIZINI.mkdir(parents=True, exist_ok=True)
RAPOR_DIZINI.mkdir(parents=True, exist_ok=True)


df = pd.read_csv(VERI_DOSYASI)

print("=" * 65)
print("İKİNCİ EL ARAÇ FİYAT TAHMİNİ - MODEL EĞİTİMİ")
print("=" * 65)

print("\nVeri seti boyutu:", df.shape)

HEDEF = "price"

ozellikler = [
    "brand",
    "model",
    "model_year",
    "milage",
    "fuel_type",
    "engine",
    "transmission",
    "accident",
    "clean_title",
]

X = df[ozellikler].copy()
y = df[HEDEF].copy()

X["model_year"] = pd.to_numeric(
    X["model_year"], errors="coerce"
)

X["milage"] = pd.to_numeric(
    X["milage"], errors="coerce"
)

y = pd.to_numeric(y, errors="coerce")

gecerli = y.notna() & (y > 0)

X = X.loc[gecerli].copy()
y = y.loc[gecerli].copy()

X = X.replace([float("inf"), float("-inf")], float("nan"))


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Eğitim kayıt sayısı:", len(X_train))
print("Test kayıt sayısı:", len(X_test))

sayisal_sutunlar = [
    "model_year",
    "milage",
]

kategorik_sutunlar = [
    "brand",
    "model",
    "fuel_type",
    "engine",
    "transmission",
    "accident",
    "clean_title",
]

sayisal_islem = Pipeline(
    steps=[
        (
            "eksik_deger",
            SimpleImputer(strategy="median")
        )
    ]
)

kategorik_islem = Pipeline(
    steps=[
        (
            "eksik_deger",
            SimpleImputer(strategy="most_frequent")
        ),
        (
            "kodlama",
           OneHotEncoder(
    handle_unknown="ignore",
    sparse_output=False
)
        ),
    ]
)

on_isleme = ColumnTransformer(
    transformers=[
        (
            "sayisal",
            sayisal_islem,
            sayisal_sutunlar
        ),
        (
            "kategorik",
            kategorik_islem,
            kategorik_sutunlar
        ),
    ]
)

modeller = {
    "Baseline": DummyRegressor(
        strategy="median"
    ),

    "Linear Regression": LinearRegression(
        n_jobs=-1
    ),

    "Random Forest": RandomForestRegressor(
        n_estimators=200,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    ),

    "Gradient Boosting": HistGradientBoostingRegressor(
        max_iter=200,
        learning_rate=0.08,
        max_leaf_nodes=15,
        l2_regularization=1.0,
        random_state=42
    ),
}

sonuclar = []
egitilmis_modeller = {}

for model_adi, algoritma in modeller.items():

    print(f"\n{'-' * 65}")
    print(f"Model eğitiliyor: {model_adi}")

    model = Pipeline(
        steps=[
            ("on_isleme", on_isleme),
            ("algoritma", algoritma),
        ]
    )

    baslangic = perf_counter()

    model.fit(X_train, y_train)

    egitim_suresi = perf_counter() - baslangic

    tahminler = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        tahminler
    )

    rmse = mean_squared_error(
        y_test,
        tahminler
    ) ** 0.5

    r2 = r2_score(
        y_test,
        tahminler
    )

    sonuclar.append(
        {
            "Model": model_adi,
            "MAE": mae,
            "RMSE": rmse,
            "R2": r2,
            "Egitim_Suresi_Saniye": egitim_suresi,
        }
    )

    egitilmis_modeller[model_adi] = model

    print(f"MAE:  {mae:,.2f} $")
    print(f"RMSE: {rmse:,.2f} $")
    print(f"R²:   {r2:.4f}")
    print(f"Eğitim süresi: {egitim_suresi:.2f} saniye")

sonuc_df = pd.DataFrame(sonuclar)

sonuc_df = sonuc_df.sort_values(
    by="MAE",
    ascending=True
).reset_index(drop=True)

print("\n" + "=" * 65)
print("MODEL KARŞILAŞTIRMA SONUÇLARI")
print("=" * 65)

print(
    sonuc_df.to_string(
        index=False,
        formatters={
            "MAE": lambda x: f"{x:,.2f}",
            "RMSE": lambda x: f"{x:,.2f}",
            "R2": lambda x: f"{x:.4f}",
            "Egitim_Suresi_Saniye": lambda x: f"{x:.2f}",
        }
    )
)

en_iyi_model_adi = sonuc_df.iloc[0]["Model"]

en_iyi_model = egitilmis_modeller[
    en_iyi_model_adi
]

model_dosyasi = MODEL_DIZINI / "en_iyi_fiyat_modeli.joblib"

joblib.dump(
    en_iyi_model,
    model_dosyasi
)

sonuc_dosyasi = RAPOR_DIZINI / "model_karsilastirma.csv"

sonuc_df.to_csv(
    sonuc_dosyasi,
    index=False
)

print("\n" + "=" * 65)
print("EĞİTİM TAMAMLANDI")
print("=" * 65)

print("En iyi model:", en_iyi_model_adi)
print("Model dosyası:", model_dosyasi)
print("Karşılaştırma raporu:", sonuc_dosyasi)

ornek_arac = pd.DataFrame(
    [
        {
            "brand": "Ford",
            "model": "F-150 XLT",
            "model_year": 2021,
            "milage": 30000,
            "fuel_type": "Gasoline",
            "engine": "2.7L V6",
            "transmission": "Automatic",
            "accident": "None reported",
            "clean_title": "Yes",
        }
    ]
)

ornek_tahmin = en_iyi_model.predict(
    ornek_arac
)[0]

print("\nÖRNEK ARAÇ FİYAT TAHMİNİ")
print("Marka: Ford")
print("Model: F-150 XLT")
print("Model yılı: 2021")
print("Kilometre: 30.000 mil")
print(f"Tahmini fiyat: ${ornek_tahmin:,.2f}")

print(
    "\nNot: Bu tahmin, veri setindeki fiyat birimine ve "
    "pazarına bağlıdır. Türkiye piyasa fiyatı olarak "
    "yorumlanmamalıdır."
)
