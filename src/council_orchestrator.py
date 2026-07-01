import asyncio
import json
import os
import sys
import re

# Add Antigravity Sub Agent Mode to path
SUB_AGENT_PATH = "/home/ads/Antigravity/Projeler/Antigravity Sub Agent Mode/src"
if SUB_AGENT_PATH not in sys.path:
    sys.path.append(SUB_AGENT_PATH)

from subagent_manager import SubAgent, MultiAgentOrchestrator
from council_prompts import CouncilPrompts

class CouncilOrchestrator:
    def __init__(self, models=None):
        self.models = models or [
            "google/gemini-2.5-flash",
            "google/gemini-2.5-flash", 
            "google/gemini-2.5-flash"
        ]
        self.orchestrator = MultiAgentOrchestrator(strategy="A") # Parallel
        self.role_keys = ["teknik", "guvenlik", "vizyoner"]

    async def run_council(self, topic: str):
        print(f"🏛️ LLM Council Session Started: {topic}")
        
        # --- STAGE 1: CONSULTATION ---
        print("\n📢 Stage 1: Consulting Council Members (AI-to-AI Mode)...")
        stage1_prompts = [CouncilPrompts.get_prompt(rk) for rk in self.role_keys]
        
        stage1_tasks = [
            f"TASK: Analyze the following content from your area of expertise.\n\n"
            f"--- START CONTEXT ---\n{topic}\n--- END CONTEXT ---\n\n"
            f"Please provide a technically dense report containing English and JSON blocks, "
            f"in a way that fellow AI agents can fully comprehend."
        ] * 3

        # return_full=True: Collect thoughts (thought) of the agents.
        responses_raw = await self.orchestrator.start_parallel_tasks(
            stage1_tasks, 
            models=self.models[:3], 
            system_prompts=stage1_prompts,
            return_full=True
        )
        
        valid_responses = []
        for i, resp in enumerate(responses_raw):
            valid_responses.append({
                "model": self.models[i],
                "role": self.role_keys[i].capitalize(),
                "full_data": resp, # Entire JSON object
                "content": resp.get("final_answer", "No answer")
            })

        # --- STAGE 2: PEER RANKING ---
        print("\n⚖️ Stage 2: Cross-Evaluation and Ranking (Deep Transparency Mode)...")
        
        labels = ["A", "B", "C"]
        responses_text = ""
        for i, r in enumerate(valid_responses):
            responses_text += f"\n--- AGENT {labels[i]} ({r['role']}) INTERNAL DIALOGUE ---\n"
            # Peers can see each other's thoughts as well
            responses_text += f"THOUGHT PROCESS: {r['full_data'].get('thought')}\n"
            responses_text += f"FINAL REPORT: {r['full_data'].get('final_answer')}\n"

        ranking_task = f"""Review the INTERNAL reasoning and final reports of your peer specialists.
 
ORIGINAL TOPIC: {topic}
 
PEER INTERNAL DATA TO ANALYZE:
{responses_text}
 
YOUR TASK:
1. Examine the THOUGHT PROCESS and FINAL REPORT of each peer.
2. Identify logical fallacies, biases, or technical gaps in their reasoning.
3. Rank them based on architectural and security rigor.
4. Provide a dense technical critique (AI-to-AI format).
"""
        stage2_tasks = [ranking_task] * 3
        rankings_raw = await self.orchestrator.start_parallel_tasks(
            stage2_tasks, 
            models=self.models[:3], 
            system_prompts=stage1_prompts,
            return_full=True
        )

        # --- STAGE 3: SYNTHESIS ---
        print("\n✍️ Stage 3: Chairperson Synthesis (Decoding Complete Council State)...")
        
        stage1_summary = "\n\n".join([f"EXPERT: {r['role']}\nTHOUGHTS: {r['full_data'].get('thought')}\nREPORT: {r['full_data'].get('final_answer')}" for r in valid_responses])
        stage2_summary = "\n\n".join([f"CRITIC: {self.models[i]}\nCRITIQUE: {rankings_raw[i].get('final_answer')}" for i in range(len(rankings_raw))])

        synthesis_task = f"""Synthesize the council's COMPLETE internal dialogue into a final report.
 
ORIGINAL TOPIC: {topic}
 
--- STAGE 1: SPECIALIST REASONING & REPORTS ---
{stage1_summary}
 
--- STAGE 2: PEER CRITIQUES ---
{stage2_summary}
 
YOUR TASK:
1. Decode the complex internal dialogue and reasoning between the experts.
2. Resolve conflicts and define the most secure/innovative path.
3. CONVERT the final technical consensus into a DETAILED TURKISH REPORT for the USER.
"""
        chairperson_prompt = CouncilPrompts.get_prompt("chairperson")
        chairperson = SubAgent("Chairperson", model=self.models[1], system_prompt=chairperson_prompt)
        
        # Max iterations set to 5 to prevent loop delay
        final_answer_raw = await chairperson.run(synthesis_task, return_full=True, max_iters=5)
        
        if isinstance(final_answer_raw, dict):
            final_answer = final_answer_raw.get("final_answer")
            if not final_answer or final_answer == "Cevap verilmedi.":
                 final_answer = final_answer_raw.get("thought", "The synthesis report could not be fully generated.")
        else:
            final_answer = final_answer_raw

        return self.generate_report(topic, valid_responses, rankings_raw, final_answer)

    def generate_report(self, topic, stage1, stage2, final):
        report = [f"# 🏛️ AegisCouncil Report (Deep Transparency)\n"]
        report.append(f"> **Topic:** {topic}\n")
        
        report.append("## 🛡️ Synthesis Report (Final Report)")
        report.append(f"{final}\n")

        report.append("---")
        report.append("## 🔬 Council Inner Dialogue & Reasoning (Complete Traceability)")
        report.append("This section contains the analytical trace logs of council members viewing each other's thought processes.\n")
        
        for i, r in enumerate(stage1):
            report.append(f"### 👤 {r['role']} ({r['model']}) Internal Process")
            report.append(f"**Thought Process:**\n{r['full_data'].get('thought')}\n")
            report.append(f"**Technical Report (AI-to-AI):**\n```text\n{r['full_data'].get('final_answer')}\n```\n")
            
            # Add critiques received by this expert
            report.append(f"*Cross-critiques received by this expert:* \n{stage2[i].get('final_answer')}\n")

        return "\n".join(report)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python council_orchestrator.py \"Topic\"")
        sys.exit(1)
        
    orchestrator = CouncilOrchestrator()
    asyncio.run(orchestrator.run_council(sys.argv[1]))
