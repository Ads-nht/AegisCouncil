import asyncio
import os
import sys

# Add src to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from council_orchestrator import CouncilOrchestrator

async def main():
    protocol_path = "/home/ads/Antigravity/Projeler/genel_hafiza.md"
    subagent_hafiza = "/home/ads/Antigravity/Projeler/Antigravity Sub Agent Mode/docs/hafiza.md"
    subagent_code = "/home/ads/Antigravity/Projeler/Antigravity Sub Agent Mode/src/subagent_manager.py"
    tools_code = "/home/ads/Antigravity/Projeler/Antigravity Sub Agent Mode/src/agent_tools.py"
    
    context = "# PRIMARY EVIDENCE FOR AUDIT (DOCS & CODE)\n\n"
    
    for path in [protocol_path, subagent_hafiza, subagent_code, tools_code]:
        if os.path.exists(path):
            with open(path, 'r') as f:
                context += f"## FILE: {os.path.basename(path)}\n"
                context += f.read() + "\n\n"
    
    topic = f"""PROJECT: Antigravity v2.1 Documentation & Handover Protocol
TASK: Audit the technical safety of the protocol and AI handover efficiency using the following primary evidence.

{context}
"""
    
    council = CouncilOrchestrator()
    report = await council.run_council(topic)
    
    log_path = "/home/ads/Antigravity/Projeler/LLM_Council/logs/final_v2.1_audit_report.md"
    with open(log_path, 'w') as f:
        f.write(report)
        
    print(f"✅ Final audit completed: {log_path}")

if __name__ == "__main__":
    asyncio.run(main())
