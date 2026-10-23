from fastapi import FastAPI

app = FastAPI(
    title="Araç Forum Platformu API",
    description=(
        "Araç forumu, ikinci el araç fiyat tahmini, bakım takibi "
        "ve otomotiv hizmet sağlayıcıları için ortak backend API'si."
    ),
    version="0.1.0",
)


@app.get("/", tags=["Genel"])
def root():
    """API'nin çalıştığını ve projenin başlangıç aşamasında olduğunu belirtir."""
    return {
        "project": "Araç Forum Platformu",
        "status": "initial_scaffold",
        "message": "Backend iskeleti hazır. Uygulama modülleri geliştirme planında.",
    }


@app.get("/health", tags=["Sistem"])
def health_check():
    """Yerel geliştirme ve test için basit sağlık kontrolü."""
    return {"status": "ok"}
