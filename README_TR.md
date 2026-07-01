# 🏛️ AegisCouncil (v1.5.0)
### Kod İnceleme, Güvenlik Denetimleri ve Mimari Analizler İçin Otonom 3 Ajanlı LLM Konsensüs Sistemi

[English](README.md) | [Türkçe](README_TR.md)

AegisCouncil; karmaşık kod tabanlarını, yazılım mimarilerini ve siber güvenlik açıklarını analiz etmek, denetlemek ve eleştirmek için tasarlanmış 3 aşamalı otonom bir yapay zeka konsensüs sistemidir. Sistem, farklı uzmanlık alanlarına sahip yapay zeka ajanlarının zekasını birleştirerek bireysel modellerin "kör noktalarını" (blind spots) ortadan kaldırır ve son derece disiplinli, objektif teknik raporlar sunar.

---

## 🚀 Öne Çıkan Özellikler

- **Özelleştirilmiş Yapay Zeka Uzmanları:** Konsey, 3 farklı uzman ajanı koordine eder:
  - **Teknik Uzman (Senior Software Architect):** Kod kalitesi, tasarım desenleri (SOLID), ölçeklenebilirlik ve performansa odaklanır.
  - **Güvenlik Denetçisi (Senior Cybersecurity Engineer):** Siber güvenlik açıklarını (OWASP, CWE) ve mantıksal hataları tarayarak nesnel bir Güvenlik Skorlama Puanı üretir.
  - **Vizyoner (Product Visionary & AI Architect):** Modern teknolojik inovasyonları ve uzun vadeli ürün büyüme stratejilerini belirler.
- **Derin Şeffaflık Protokolü (Deep Transparency):** Uzman ajanlar birbirlerinin sadece nihai raporlarını değil, iç düşünce süreçlerini de (`thought` alanları) inceleyerek mantıksal boşlukları ve çelişkileri yakalar.
- **İç İletişim Protokolü:** Konsey üyeleri kendi aralarında en verimli teknik dilde (İngilizce/JSON) haberleşir; Chairperson tüm bu ham iç diyaloğu analiz ederek kullanıcıya detaylı Türkçe bir rapor sentezler.
- **Çoklu Model Konsensüsü:** Grok, Gemini, GPT-4o gibi farklı LLM modellerini OpenRouter üzerinden koordine ederek tarafsız ve çok perspektifli sonuçlar sağlar.

---

## 🏗️ Konsensüs Mimarisi

```mermaid
graph TD
    User([Kullanıcı Denetim İsteği]) -->|Konu veya Kod Gönderimi| Orch[CouncilOrchestrator]
    Orch -->|Danışma Aşaması| Stage1[1. Aşama: Uzmanlar İçeriği Analiz Eder]
    Stage1 -->|Düşünce ve raporların paylaşımı| Stage2[2. Aşama: Çapraz Değerlendirme ve Sıralama]
    Stage2 -->|Karşılıklı eleştiri ve tartışma| Stage3[3. Aşama: Chairperson Sentezleme & Deşifre]
    Stage3 -->|Nihai Konsensüs Raporu| Output([Markdown Konsensüs Raporu])
```

---

## 🛠️ Sistem Gereksinimleri ve Kurulum

### Gereksinimler
- Python 3.10+
- Yapay zeka modellerini tetiklemek için OpenRouter API Anahtarı.

### Kurulum
1. Depoyu bilgisayarınıza kopyalayın:
   ```bash
   git clone git@github.com:Ads-nht/AegisCouncil.git
   cd AegisCouncil
   ```
2. Sanal ortam (venv) oluşturun ve aktif edin:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
4. API anahtarınızı tanımlayın:
   ```bash
   export OPENROUTER_API_KEY="openrouter_api_anahtariniz_buraya"
   ```

### Kullanım
Bir denetim başlatmak için konuyu veya yerel bir bağlam dosyası yolunu argüman olarak geçin:
```bash
python src/council_run.py "Denetlemek istediğiniz konu, soru veya dosya yolu"
```

Denetim raporları otomatik olarak konsola yazdırılır ve `logs/` dizini altına markdown dosyası olarak kaydedilir (Örn: `logs/council_report_*.md`).

---

## 📄 Dosya Yapısı

- `src/council_orchestrator.py`: 3 aşamalı konsensüs hattını koordine eden ana yönetim mantığı.
- `src/council_prompts.py`: Her uzman ajan için optimize edilmiş sistem promptlarının bulunduğu katalog.
- `src/council_run.py`: Yerel dosya okuma desteğine sahip komut satırı arayüzü (CLI).
- `docs/hafiza.md`: Sistem belleği ve protokol dökümantasyonunun tutulduğu teknik defter.
- `docs/ai_usage_guide.json`: Diğer yapay zeka ajanlarının bu konseyi otonom çalıştırabilmesi için yapılandırılmış kılavuz.

---

## 📄 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.
