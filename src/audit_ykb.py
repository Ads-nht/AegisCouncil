import asyncio
import os
import sys

# Add src to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from council_orchestrator import CouncilOrchestrator

async def main():
    # YKB Project Files
    project_root = "/home/ads/Antigravity/Projeler/YouTube_Knowledge_Base"
    files_to_audit = [
        os.path.join(project_root, "src/youtube_kb_tool.py"),
        os.path.join(project_root, "src/vault_manager.py"),
        os.path.join(project_root, "docs/hafiza.md"),
        os.path.join(project_root, "docs/changelog.md"),
        os.path.join(project_root, "docs/roadmap.md"),
        os.path.join(project_root, "README.md"),
        "/home/ads/Antigravity/Projeler/genel_hafiza.md" # Core Protocol for reference
    ]
    
    context = "# PRIMARY EVIDENCE FOR YKB AUDIT (v1.7.0/v5.0 Enterprise Edition)\n\n"
    
    for path in files_to_audit:
        if os.path.exists(path):
            with open(path, 'r') as f:
                context += f"## FILE: {os.path.basename(path)} ({path})\n"
                context += f.read() + "\n\n"
    
    topic = f"""PROJE: YouTube Knowledge Base (YKB) - v3.0.0 TOTAL MASTERY Final Denetimi
GÖREV: Aşağıdaki nihai kodları (v3.0.0) inceleyerek; Persistence (Vault), Batch Processing ve Smart Polling 
uygulamalarını denetle. Projenin 'Master Grade' sertifikasyonuna hazır olup olmadığını ve siber güvenlik 
açısından (XSS/SSRF/CWE) kusursuzluğunu doğrula.

ÖZELLİKLE SORULAN SORULAR:
1. SQLite Vault (Persistence) yapısı güvenli ve verimli mi?
2. Smart Polling (Exponential Backoff) algoritması doğru kurgulanmış mı?
3. Mevcut 'Master' mimarisinde hala gözden kaçan bir 'Technical Gap' var mı?

{context}
"""
    
    council = CouncilOrchestrator()
    report = await council.run_council(topic)
    
    log_path = "/home/ads/Antigravity/Projeler/LLM_Council/logs/ykb_audit_v3.0_report.md"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, 'w') as f:
        f.write(report)
        
    print(f"✅ YKB Denetimi tamamlandı: {log_path}")

if __name__ == "__main__":
    asyncio.run(main())
