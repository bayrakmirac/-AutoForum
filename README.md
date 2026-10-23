# Araç Forum Platformu

**Proje sahibi:** Miraç Bayrak
**Öğrenci numarası:** 241230026

Araç Forum; araç sahiplerinin araçlarıyla ilgili sorunları paylaşabildiği, deneyim ve bilgi alışverişinde bulunabildiği, araçlarına özel içeriklere erişebildiği ve otomotiv sektöründeki hizmet sağlayıcıları bulabildiği bir dijital platformdur.

Projenin amacı; otomobil forumunu, araç bakım takibini ve makine öğrenmesi tabanlı ikinci el araç fiyat tahminini tek bir platformda bir araya getirmektir.

## Projenin Ana Modülleri

### 1. Araç Forumu

* Araç markası, modeli ve araç sayfalarına göre içeriklere erişim.
* Arıza, mekanik problem, bakım, kullanım deneyimi ve yedek parça konularında gönderiler.
* Gönderilere yorum yapma ve bilgi/deneyim paylaşma.
* Genel forum akışı ve araç bazlı konu alanları.
* Kullanıcı profilleri ve kullanıcı araçları.

### 2. İkinci El Araç Fiyat Tahmini

Makine öğrenmesi modülü, ikinci el araçların özelliklerinden yararlanarak tahmini piyasa fiyatını hesaplamayı amaçlar.

İlk geliştirme aşamasında bu modüle odaklanılacaktır.

Planlanan çalışmalar:

* Veri setinin bulunması ve incelenmesi.
* Eksik ve hatalı verilerin işlenmesi.
* Keşifsel veri analizi ve görselleştirme.
* Birden fazla regresyon modelinin eğitilmesi.
* Modellerin MAE, MSE, RMSE ve R² metrikleriyle karşılaştırılması.
* En uygun modelin seçilmesi ve uygulamaya entegrasyonu.

Tahmin sonuçları yaklaşık değerler sunacaktır; gerçek piyasa fiyatı araçların durumu ve güncel piyasa koşullarına göre değişebilir.

### 3. Araç Bakım Takibi

* Araç kilometresi ve bakım bilgilerinin kaydedilmesi.
* Yağ değişimi ve parça değişimi gibi bakım kayıtlarının tutulması.
* Gelecek bakımlar için hatırlatmalar oluşturulması.

### 4. Profesyonel Profiller

* Oto tamircileri ve servisler için profesyonel profiller.
* Yedek parça satıcılarının kendilerini tanıtabileceği profiller.
* Kullanıcıların otomotiv hizmet sağlayıcılarını bulabilmesi.

## Teknoloji Altyapısı

Başlangıç projesinde aşağıdaki teknolojiler kullanılmaktadır:

* **Backend:** Python, FastAPI
* **Web arayüzü:** React, TypeScript, Vite
* **Mobil uygulama:** React Native, Expo
* **Makine öğrenmesi:** Python, pandas, NumPy, scikit-learn
* **Planlanan veri tabanı:** PostgreSQL

Teknolojiler ve mimari, geliştirme sürecinde ihtiyaçlara göre güncellenebilir.

## Geliştirme Yol Haritası

1. Temel proje yapısının oluşturulması.
2. İkinci el araç fiyat tahmini için veri analizi ve model geliştirme.
3. Tahmin modelinin backend ile entegrasyonu.
4. Araç forumu ve kullanıcı özelliklerinin geliştirilmesi.
5. Araç bakım takibi modülünün geliştirilmesi.
6. Profesyonel profillerin oluşturulması.
7. Web ve mobil uygulamanın test edilmesi ve iyileştirilmesi.

## Proje Durumu

Bu depo, projenin başlangıç iskeletini içerir. Modüller aşamalı olarak geliştirilecektir. Henüz tamamlanmamış özellikler çalışır durumda kabul edilmemelidir.
