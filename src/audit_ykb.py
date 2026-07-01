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
    
    topic = f"""PROJECT: YouTube Knowledge Base (YKB) - v3.0.0 TOTAL MASTERY Final Audit
TASK: Review the final code (v3.0.0) below to audit the Persistence (Vault), Batch Processing, and Smart Polling
implementations. Verify whether the project is ready for 'Master Grade' certification and validate its security
compliance (XSS/SSRF/CWE).

SPECIFIC AUDIT QUESTIONS:
1. Is the SQLite Vault (Persistence) architecture secure and efficient?
2. Is the Smart Polling (Exponential Backoff) algorithm correctly designed?
3. Are there any remaining 'Technical Gaps' overlooked in the current 'Master' architecture?

{context}
"""
    
    council = CouncilOrchestrator()
    report = await council.run_council(topic)
    
    log_path = "/home/ads/Antigravity/Projeler/LLM_Council/logs/ykb_audit_v3.0_report.md"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, 'w') as f:
        f.write(report)
        
    print(f"✅ YKB Audit completed: {log_path}")

if __name__ == "__main__":
    asyncio.run(main())
