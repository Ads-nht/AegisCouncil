import asyncio
import os
import sys

# Add src to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from council_orchestrator import CouncilOrchestrator

async def main():
    # SKO Project Files
    project_root = "/home/ads/Antigravity/Projeler/Site_Knowledge_Oracle"
    files_to_audit = [
        os.path.join(project_root, "bundled_sko_tool.py"),
        os.path.join(project_root, "src/crawler_engine.py"),
        os.path.join(project_root, "src/vault_manager.py"),
        os.path.join(project_root, "docs/hafiza.md"),
        os.path.join(project_root, "docs/architecture.md"),
        os.path.join(project_root, "README.md")
    ]
    
    context = "# PRIMARY EVIDENCE FOR SITE KNOWLEDGE ORACLE (SKO) AUDIT (v0.3.1-ARCHIVIST)\n\n"
    
    for path in files_to_audit:
        if os.path.exists(path):
            with open(path, 'r') as f:
                context += f"## FILE: {os.path.basename(path)} ({path})\n"
                context += f"```"
                context += "python\n" if path.endswith(".py") else "markdown\n"
                context += f.read() + "\n```\n\n"
    
    topic = f"""PROJE: Site Knowledge Oracle (SKO) - v0.3.1 ELITE MASTER GRADE Sertifikasyonu
GÖREV: Aşağıdaki nihai kodları ve dökümantasyonu inceleyerek; SSRF Shield (DNS Safe Resolve), XSS Sanitization (Bleach) 
ve Archivist (Autonomous Append) mantığını denetle. Projenin Antigravity v5.0+ standartlarına uygunluğunu doğrula.

DENETİM KRİTERLERİ:
1. SSRF Shield: DNS çözümleme mantığı TOCTOU açıklarına karşı dirençli mi? (socket.getaddrinfo kullanımı)
2. Archivist Mantığı: Knowledge Base dosya güncelleme API çağrıları tutarlı ve güvenli mi?
3. Vault Manager: SQLite WAL ve mutlak yol kullanımı doğru kurgulanmış mı?
4. Dökümantasyon: 'AI-Ready' seviyesine ulaşılmış mı?

{context}
"""
    
    print("🚀 SKO Elite Master Grade Audit Council Başlatılıyor...")
    council = CouncilOrchestrator()
    report = await council.run_council(topic)
    
    log_path = "/home/ads/Antigravity/Projeler/LLM_Council/logs/sko_v0.3.1_elite_report.md"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, 'w') as f:
        f.write(report)
        
    print(f"\n✅ SKO Denetimi tamamlandı: {log_path}")

if __name__ == "__main__":
    asyncio.run(main())
