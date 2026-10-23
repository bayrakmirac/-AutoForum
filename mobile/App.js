import React from "react";
import { SafeAreaView, ScrollView, StatusBar, StyleSheet, Text, View } from "react-native";

const modules = [
  { number: "01", title: "Araç Forumu", detail: "Araç sorunları, bakım deneyimleri ve kullanıcı paylaşımları." },
  { number: "02", title: "Fiyat Tahmini", detail: "Makine öğrenmesiyle ikinci el araç fiyatı tahmini. İlk geliştirme önceliği." },
  { number: "03", title: "Bakım Takibi", detail: "Kilometre ve bakım geçmişi kayıtları." },
  { number: "04", title: "Profesyonel Profiller", detail: "Usta ve yedek parça satıcıları için profiller." },
];

export default function App() {
  return (
    <SafeAreaView style={styles.safe}>
      <StatusBar barStyle="light-content" />
      <ScrollView contentContainerStyle={styles.container}>
        <View style={styles.hero}>
          <Text style={styles.eyebrow}>ARAÇ FORUM PLATFORMU</Text>
          <Text style={styles.title}>Araç sahipleri için ortak bilgi alanı.</Text>
          <Text style={styles.intro}>Forum, bakım takibi ve ikinci el araç fiyat tahmini tek platformda buluşacak.</Text>
        </View>
        {modules.map((item) => (
          <View key={item.number} style={styles.card}>
            <Text style={styles.number}>{item.number}</Text>
            <Text style={styles.cardTitle}>{item.title}</Text>
            <Text style={styles.detail}>{item.detail}</Text>
          </View>
        ))}
        <Text style={styles.footer}>Başlangıç sürümü · Modüller geliştirme aşamasındadır.</Text>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: "#f4f6fa" },
  container: { padding: 18, paddingBottom: 32 },
  hero: { backgroundColor: "#14243a", borderRadius: 22, padding: 26, marginBottom: 18 },
  eyebrow: { color: "#9ed5ff", fontSize: 11, fontWeight: "800", letterSpacing: 2 },
  title: { color: "#ffffff", fontSize: 31, fontWeight: "800", lineHeight: 37, marginTop: 18 },
  intro: { color: "#d5deeb", fontSize: 15, lineHeight: 23, marginTop: 14 },
  card: { backgroundColor: "#ffffff", borderRadius: 16, borderWidth: 1, borderColor: "#e4e9f1", padding: 22, marginBottom: 12 },
  number: { color: "#3478b8", fontWeight: "800" },
  cardTitle: { color: "#172033", fontSize: 19, fontWeight: "700", marginTop: 10 },
  detail: { color: "#58657a", fontSize: 14, lineHeight: 21, marginTop: 8 },
  footer: { color: "#6d7788", fontSize: 12, lineHeight: 18, marginTop: 8 },
});
