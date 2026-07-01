# 🏛️ Antigravity LLM Council (v1.5.0 Premium)

Antigravity LLM Council, karmaşık projeleri, siber güvenlik açıklarını ve mimari yapıları denetlemek için tasarlanmış **3 aşamalı otonom bir yapay zeka konsensüs sistemidir.**

## 🚀 Öne Çıkan Özellikler

- **Süper Uzman Kadrosu:** Siber Güvenlik (OWASP/CWE), Kıdemli Yazılım Mimarisi (SOLID/Clean Arch) ve Ürün Vizyonu alanlarında uzmanlaşmış 3 farklı ajan.
- **Deep Transparency (Derin Şeffaflık):** Uzmanlar birbirlerinin sadece sonuçlarını değil, iç düşünce süreçlerini (thoughts) de görerek karşılıklı denetim (peer-critique) yaparlar.
- **Inner Dialogue Protocol:** Konsey üyeleri kendi aralarında en verimli teknik dilde (İngilizce/JSON) iletişim kurar, Chairperson son sonucu kullanıcıya Türkçe olarak sentezler.
- **Bağımsız Denetim:** Farklı LLM modellerinin (Grok, Gemini, GPT-4o) zekasını birleştirerek "blind spot" riskini minimize eder.

## 🛠️ Kurulum ve Kullanım

### Gereksinimler
- Antigravity Sub Agent Mode (Dahili bağımlılık)
- Python 3.10+
- OpenRouter API Anahtarı

### Hızlı Çalıştırma
```bash
cd /home/ads/Antigravity/Projeler/LLM_Council
./.venv/bin/python src/council_run.py "Projenizi veya konunuzu buraya yazın"
```

## 🏗️ Mimari Yapı

1. **Aşama (Consultation):** Uzmanlar konuyu analiz eder (Teknik İngilizce/JSON).
2. **Aşama (Ranking & Critique):** Uzmanlar birbirlerinin düşünce süreçlerini kritik edip sıralama yapar.
3. **Aşama (Synthesis):** Chairperson tüm veriyi deşifre eder ve nihai Premium Türkçe raporu oluşturur.

## 📄 Dosya Yapısı
- `src/council_orchestrator.py`: Ana yönetim mantığı ve aşama kontrolü.
- `src/council_prompts.py`: Uzman sistem promptları.
- `src/council_run.py`: CLI giriş noktası.
- `docs/hafiza.md`: Sistem belleği ve protokol dökümantasyonu.
- `docs/ai_usage_guide.json`: Diğer AI ajanları için kullanım kılavuzu.

---
*Antigravity LLM Council - "The path to 10x engineering leads through collective intelligence."*
