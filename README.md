# Araç Forum Platformu

**Proje sahibi:** Miraç Bayrak  
**Öğrenci numarası:** 241230026

## 1. Projenin amacı

Araç Forum Platformu; araç sahiplerinin araçlarına ilişkin sorunları paylaşabildiği, deneyim ve bilgi alışverişinde bulunabildiği, araçlarına özel içeriklere erişebildiği ve otomotiv sektöründeki hizmet sağlayıcıları bulabildiği bir dijital platform olarak tasarlanmaktadır.

Platformun ana ürünü araç odaklı forumdur. Makine öğrenmesi tabanlı ikinci el araç fiyat tahmini, bu platformun içerisinde yer alacak modüllerden biridir. Akademik geliştirme sürecinde ilk olarak fiyat tahmini modülü ele alınacak; bu modülün ardından forumun ve diğer yardımcı özelliklerin geliştirilmesine devam edilecektir.

## 2. Planlanan ana modüller

### 2.1. Araç forumu — ana modül
- Araç markası, modeli ve araç sayfalarına göre içeriklere erişim
- Arıza, mekanik problem, bakım, kullanım deneyimi ve yedek parça konularında gönderiler
- Gönderilere yorum yapma ve bilgi/deneyim paylaşma
- Genel forum akışı ve araç bazlı konu alanları
- Kullanıcı profilleri ve kullanıcının araçları

### 2.2. İkinci el araç fiyat tahmini — makine öğrenmesi modülü
Kullanıcının girdiği araç özelliklerinden tahmini ikinci el piyasa fiyatı üretmesi hedeflenmektedir. Bu modül, ders kapsamında ilk geliştirilecek ve değerlendirilecek parçadır.

İncelenmesi planlanan özellikler:
- Marka ve model
- Model yılı
- Kilometre
- Yakıt türü
- Vites türü
- Motor ve diğer veri setinde bulunan araç özellikleri

Bu problem bir **regresyon problemi** olarak ele alınacaktır. Veri seti incelenip temizlendikten sonra keşifsel veri analizi ve özellik hazırlama yapılacak; en az üç makine öğrenmesi modeli eğitilip MAE, MSE, RMSE ve R² metrikleriyle karşılaştırılacaktır. Sonuçlar uygun olduğunda seçilen model API üzerinden web ve mobil arayüzlere sunulacaktır.

**Mevcut durum:** Bu ilk commit'te henüz veri analizi yapılmamış ve fiyat tahmin modeli eğitilmemiştir. Bunlar sonraki geliştirme aşamasının kapsamındadır.

### 2.3. Bakım takip sistemi
- Kullanıcının araç kilometresi ve bakım işlemlerini kaydetmesi
- Yağ değişimi, parça değişimi ve benzeri işlemlerin geçmişini tutma
- Bakım hatırlatmalarını destekleyecek temel veri yapısının hazırlanması

### 2.4. Usta ve yedek parça satıcısı profilleri
- Otomotiv hizmet sağlayıcıları için profesyonel profil
- Hizmet ve iletişim bilgilerinin listelenmesi
- Kullanıcıların ilgili hizmet sağlayıcıları bulabilmesi

### 2.5. Hesap ve araç yönetimi
- Kayıt ve giriş
- Kullanıcı profili
- Kullanıcının araçlarını ekleme ve yönetme
- İlerleyen aşamada araç sahipliğini doğrulamaya yönelik bir akışın değerlendirilmesi

## 3. Hedef platformlar ve teknoloji planı

Web sitesi ve mobil uygulamanın aynı backend ve veritabanı üzerinden çalışması hedeflenmektedir.

| Katman | Planlanan teknoloji | Sorumluluk |
|---|---|---|
| Web arayüzü | React + TypeScript + Vite | Tarayıcıdan kullanılan forum ve modül arayüzleri |
| Mobil uygulama | React Native + Expo + TypeScript | Android ve iOS uygulaması |
| Backend/API | Python + FastAPI | Web ve mobil istemcilere ortak API sağlama |
| Makine öğrenmesi | pandas, NumPy, scikit-learn | Veri hazırlama, model eğitimi ve değerlendirme |
| Veritabanı | PostgreSQL | Kullanıcı, araç, gönderi, yorum ve bakım kayıtları |
| ORM/veritabanı erişimi | SQLAlchemy (planlanan) | Python ile veritabanı işlemleri |
| Model saklama | joblib (planlanan) | Eğitilmiş modelin kaydedilmesi ve yüklenmesi |
| Test | pytest | Backend testleri |
| Sürüm kontrolü | Git + GitHub | Geliştirme geçmişi ve düzenli commit takibi |

Bu teknoloji seçimi başlangıç mimarisidir. İhtiyaçlara ve geliştirme sürecine göre README üzerinde güncellenecektir.

## 4. Genel mimari

```text
                  ARAÇ FORUM PLATFORMU
                           |
                +----------+----------+
                |                     |
                v                     v
           WEB İSTEMCİSİ         MOBİL İSTEMCİ
       React + TypeScript     React Native + Expo
                |                     |
                +----------+----------+
                           |
                           v
                    BACKEND API
                     Python/FastAPI
                           |
              +------------+------------+
              |            |            |
              v            v            v
          PostgreSQL   Fiyat Tahmini   Dosya/Medya
          (uygulama     ML modülü      (ileride)
           verileri)   (Python)
```

Web ve mobil istemcilerin ayrı arayüzleri olacak; kullanıcı, forum ve fiyat tahmini işlemleri için aynı backend API'yi kullanmaları hedeflenecektir.

## 5. İkinci el araç fiyat tahmini: planlanan çalışma

### Veri kaynakları
Proje önerisinde incelenmek üzere belirtilen kaynaklar:
1. [Used Car Price Prediction Dataset — Kaggle](https://www.kaggle.com/datasets/taeefnajib/used-car-price-prediction-dataset)
2. [Used-Car Price Prediction Dataset — Zenodo](https://zenodo.org/records/19394818)

Veri seti seçilmeden önce sütunlar, hedef fiyat değişkeni, eksik değerler, veri kalitesi, lisans ve kullanım koşulları kontrol edilecektir. Veri dosyaları bu ilk commit'e eklenmemiştir.

### Planlanan deney adımları
1. Veri setini edinme ve sütunlarını inceleme
2. Eksik/tekrarlı/aykırı değerleri analiz etme
3. Keşifsel veri analizi ve görselleştirme
4. Kategorik ve sayısal özellikleri hazırlama
5. Eğitim ve test kümelerini ayırma
6. En az üç regresyon modelini eğitme
7. MAE, MSE, RMSE ve R² ile sonuçları karşılaştırma
8. Uygun modeli kaydetme
9. Modeli FastAPI üzerinden tahmin endpoint'ine bağlama
10. Web ve mobil arayüzden tahmin isteği gönderme

Model türleri veri seti ve deney sonuçları değerlendirildikten sonra seçilecektir. Linear Regression, Random Forest ve Gradient Boosting gibi yöntemler aday olarak incelenebilir; başarıları deney yapılmadan varsayılmayacaktır.

## 6. Yol haritası ve geliştirme sırası

### Aşama 1 — Proje iskeleti (bu commit)
- Ana proje yapısını ve kapsamını belgeleme
- Backend, web ve mobil uygulama için başlangıç klasörlerini oluşturma
- FastAPI için temel sağlık kontrolü endpoint'i ekleme
- Web ve mobil için başlangıç ekranlarını hazırlama
- Bağımlılıkları ve Git ignore kurallarını tanımlama
- Backend için temel testi ekleme

### Aşama 2 — Fiyat tahmini modülü (ilk geliştirme önceliği)
- Veri setini seçme ve inceleme
- Veri ön işleme ve keşifsel veri analizi
- En az üç regresyon modelinin eğitilmesi ve karşılaştırılması
- Değerlendirme sonuçlarının raporlanması
- Tahmin modelinin backend API'ye bağlanması
- Basit bir fiyat tahmini arayüzünün hazırlanması ve sunulması

### Aşama 3 — Forumun temel özellikleri
- Veritabanı modelleri ve kullanıcı hesapları
- Araç sayfaları, gönderiler ve yorumlar
- Kullanıcı profilleri ve araç yönetimi

### Aşama 4 — Yardımcı modüller
- Bakım takip kayıtları ve hatırlatmalar
- Usta ve yedek parça satıcısı profilleri
- Arama, filtreleme ve kullanıcı deneyimi iyileştirmeleri

### Aşama 5 — Bütünleştirme ve teslim
- Web ve mobil istemcilerin ortak API ile çalışması
- Testler, hata düzeltmeleri ve güvenlik kontrolleri
- Kurulum dokümantasyonu ve proje sunumu

## 7. Yerel geliştirme

### Gereksinimler
- Python 3.11 veya uyumlu bir sürüm
- Node.js ve npm
- Git

### Backend'i çalıştırma
Windows PowerShell örneği:

```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend çalışınca:
- Sağlık kontrolü: `http://127.0.0.1:8000/health`
- Otomatik API dokümantasyonu: `http://127.0.0.1:8000/docs`

### Web başlangıç ekranını çalıştırma
```bash
cd web
npm install
npm run dev
```

### Mobil başlangıç ekranı
```bash
cd mobile
npm install
npx expo start
```

Web ve mobil istemcilerin backend ile tam işlevli entegrasyonu bu ilk commit'in kapsamı dışındadır.

## 8. İlk commit kapsamı

Bu commit, projenin tüm modüllerini ve hedef mimarisini görünür kılan başlangıç sürümüdür. Backend için çalışan bir FastAPI iskeleti, web ve mobil için başlangıç ekranları, temel test ve proje dokümantasyonu içerir.

Bu commit'te kullanıcı hesabı, forum gönderileri, veritabanı şeması veya eğitilmiş fiyat tahmin modeli henüz uygulanmış değildir. Bu özellikler yol haritasında belirtilen aşamalarda geliştirilecektir.
