# 📜 Changelog - LLM Council

Tüm majör teknik gelişimlerin kronolojik kaydı.

## [1.7.1] - 2026-04-16
### Added
- Kök `requirements.txt` (Antigravity v5.2 proje dizin standardı).

## [1.6.0] - 2026-04-10
### Added
- **Powerful Model Lineup:** Konsey üyeleri `deepseek/deepseek-v3.2` ve `minimax/minimax-m2.7` modelleri ile güçlendirildi.
- **Performance Optimization:** Sentez (Stage 3) aşamasındaki gereksiz iterasyon döngüleri (23-adım bekletme sorunu) `max_iters=5` ve `One-Shot Synthesis` promptu ile giderildi.
- **Improved Resilience:** Sentez aşamasında JSON hatası durumunda `thought` alanından veri kurtarma (fallback) mekanizması eklenedi.

## [1.5.0] - 2026-04-10
### Added
- **Deep Transparency:** Uzmanların birbirlerinin düşünce süreçlerini (thoughts) görebilmesi sağlandı.
- **Translingual Synthesis:** İngilizce/JSON iç diyaloğunun detaylı Türkçe rapora dönüştürülmesi.
- **Initial Pro-level Audit:** YouTube Knowledge Base projesi üzerinde ilk başarılı denetim gerçekleştirildi.