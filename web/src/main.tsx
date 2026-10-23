import React from "react";
import { createRoot } from "react-dom/client";
import "./style.css";

function App() {
  return (
    <main className="page">
      <header className="hero">
        <p className="eyebrow">ARAÇ FORUM PLATFORMU</p>
        <h1>Araç sahipleri için ortak bilgi alanı.</h1>
        <p className="intro">
          Araç deneyimlerini paylaşmayı, bakım bilgilerini takip etmeyi ve
          ikinci el araç fiyatlarını incelemeyi tek platformda buluşturmayı hedefliyoruz.
        </p>
      </header>
      <section className="grid" aria-label="Planlanan modüller">
        <article><span>01</span><h2>Araç Forumu</h2><p>Arıza, bakım, kullanım deneyimi ve yedek parça konularında paylaşım.</p><small>Ana modül</small></article>
        <article><span>02</span><h2>Fiyat Tahmini</h2><p>Araç özelliklerinden tahmini ikinci el piyasa değeri üretmek için makine öğrenmesi.</p><small>İlk geliştirme önceliği</small></article>
        <article><span>03</span><h2>Bakım Takibi</h2><p>Kilometre ve bakım işlemlerini kayıt altına alma ve hatırlatma altyapısı.</p><small>Planlanan modül</small></article>
        <article><span>04</span><h2>Profesyonel Profiller</h2><p>Usta ve yedek parça satıcılarının hizmetlerini tanıtabileceği profiller.</p><small>Planlanan modül</small></article>
      </section>
      <footer>İlk geliştirme sürümü · Henüz gerçek kullanıcı verisi veya fiyat tahmini içermez.</footer>
    </main>
  );
}

createRoot(document.getElementById("root")!).render(
  <React.StrictMode><App /></React.StrictMode>
);
