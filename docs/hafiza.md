# 🧠 AegisCouncil - Hafıza (Knowledge Base)

Bu döküman, AegisCouncil'ın tasarımı, protokolleri ve evrimi hakkında kritik bilgileri içerir. Otonom ajanlar için "Context" (bağlam) sağlar.

## 🪐 Genel Bakış (v1.5.0)
AegisCouncil, tek bir yapay zekanın "bias" (yanlılık) ve "blind spot" (kör nokta) sorunlarını aşmak için tasarlanmış 3 aşamalı bir otonom denetim sistemidir. **Bu sistem, Antigravity ekosistemindeki zorunlu 'Post-Project Audit' protokolünün (Bkz: [/Projeler/genel_hafiza.md](file:///home/ads/Antigravity/Projeler/genel_hafiza.md) Bölüm 5.2) ana yürütücü aracıdır.**

## 🛡️ Protokoller (Protocols)

### 1. Inner Dialogue Protocol (AI-to-AI)
Uzmanlar (Teknik, Güvenlik, Vizyoner) iç iletişimlerinde (Consultation & Ranking) **AI Verimliliği** odaklı davranırlar (Dense Technical English / JSON).

### 2. Deep Transparency Protocol
Konsey üyeleri birbirlerinin sadece final raporlarını değil, **thought (akıl yürütme)** süreçlerini de görebilirler. `return_full=True` ile tüm State aktarılır.

### 3. Translingual Synthesis
İç İngilizce/JSON diyaloğu, Chairperson tarafından çözümlenir ve kullanıcıya **detaylı Türkçe** rapor olarak sunulur.

## 🏗️ Mimari (Architecture)
- **Orchestration:** `council_orchestrator.py`
- **Hızlı Başlatma (CLI):** `python src/council_run.py "Topic"`
- **Prompts:** `council_prompts.py` (Expert Catalog)
- **Sub-Agent Logic:** `subagent_manager.py` (Sub Agent Mode base)

## 📊 Karar Alma Aşamaları
1. **Danışma (Consultation):** Uzmanlar konuyu analiz eder.
2. **Sıralama (Ranking):** Peer-review ve mantık hatası eleştirisi.
3. **Sentez (Synthesis):** Nihai stratejik yol ve Türkçe rapor.

## 📍 Mevcut Durum (Current State)
- **Versiyon:** v1.6.0 Performance Upgrade
- **Modeller:** Grok-4.1-fast, DeepSeek-V3.2, MiniMax-M2.7.
- **Optimizasyon:** Sentez aşaması `max_iters=5` ve "One-Shot" promptu ile hızlandırıldı. "23-adım" döngü hatası giderildi.

## 🏁 Sıradaki Adımlar (Next Steps)
1. **Dynamic Model Selection:** Modellerin otomatik maliyet/performans optimizasyonu.
2. **Context Compression:** Uzun dökümanlarda token tasarrufu.
3. **Multi-Model synthesis:** Farklı modellerin chairperson olarak performansını karşılaştırmak.

---
*Son Güncelleme: 11 Nisan 2026 - Antigravity Core Protocol v2.1 & Council v1.6.0 Uyumlu*