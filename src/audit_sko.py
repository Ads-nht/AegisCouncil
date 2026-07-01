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
    
    topic = f"""PROJECT: Site Knowledge Oracle (SKO) - v0.3.1 ELITE MASTER GRADE Certification
TASK: Review the final code and documentation below to audit the SSRF Shield (DNS Safe Resolve), XSS Sanitization (Bleach),
and Archivist (Autonomous Append) logic. Verify the project's compliance with Antigravity v5.0+ standards.

AUDIT CRITERIA:
1. SSRF Shield: Is the DNS resolution logic resilient to TOCTOU attacks? (socket.getaddrinfo usage)
2. Archivist Logic: Are the Knowledge Base file update API calls consistent and secure?
3. Vault Manager: Is the SQLite WAL and absolute path usage correctly designed?
4. Documentation: Has it achieved 'AI-Ready' status?

{context}
"""
    
    print("🚀 Starting SKO Elite Master Grade Audit Council...")
    council = CouncilOrchestrator()
    report = await council.run_council(topic)
    
    log_path = "/home/ads/Antigravity/Projeler/LLM_Council/logs/sko_v0.3.1_elite_report.md"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, 'w') as f:
        f.write(report)
        
    print(f"\n✅ SKO Audit completed: {log_path}")

if __name__ == "__main__":
    asyncio.run(main())
