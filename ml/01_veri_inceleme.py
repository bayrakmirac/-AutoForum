from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
RAW_DIR = PROJECT_DIR / "data" / "raw"

csv_files = list(RAW_DIR.glob("*.csv"))

if not csv_files:
    print("CSV dosyası bulunamadı.")
else:
    for file_path in csv_files:
        print("\n" + "=" * 60)
        print("VERİ SETİ:", file_path.name)
        print("=" * 60)

        df = pd.read_csv(file_path)

        print("\nSatır ve sütun sayısı:", df.shape)
        print("\nSütunlar:")
        print(df.columns.tolist())

        print("\nİlk 5 kayıt:")
        print(df.head().to_string())

        print("\nVeri türleri:")
        print(df.dtypes.to_string())

        print("\nEksik değerler:")
        print(df.isnull().sum().to_string())

        print("\nTekrarlanan satır sayısı:")
        print(df.duplicated().sum())
        