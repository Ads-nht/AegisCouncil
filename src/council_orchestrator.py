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
        print(f"🏛️ LLM Council Toplantısı Başladı: {topic}")
        
        # --- STAGE 1: CONSULTATION ---
        print("\n📢 Aşama 1: Konsey Üyelerine Danışılıyor (AI-to-AI Mode)...")
        stage1_prompts = [CouncilPrompts.get_prompt(rk) for rk in self.role_keys]
        
        stage1_tasks = [
            f"GÖREV: Aşağıdaki içeriği uzmanlık alanın açısından analiz et.\n\n"
            f"--- START CONTEXT ---\n{topic}\n--- END CONTEXT ---\n\n"
            f"Lütfen diğer AI ajanlarının anlayabileceği şekilde, teknik derinliği yüksek, "
            f"İngilizce ve JSON blokları içeren bir rapor sun."
        ] * 3

        # return_full=True: Ajanların düşüncelerini (thought) de topluyoruz.
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
                "full_data": resp, # Tüm JSON objesi
                "content": resp.get("final_answer", "No answer")
            })

        # --- STAGE 2: PEER RANKING ---
        print("\n⚖️ Aşama 2: Çapraz Değerlendirme ve Sıralama (Deep Transparency Mode)...")
        
        labels = ["A", "B", "C"]
        responses_text = ""
        for i, r in enumerate(valid_responses):
            responses_text += f"\n--- AGENT {labels[i]} ({r['role']}) INTERNAL DIALOGUE ---\n"
            # Peer'lar birbirlerinin thought süreçlerini de görüyor!
            responses_text += f"THOUGHT PROCESS: {r['full_data'].get('thought')}\n"
            responses_text += f"FINAL REPORT: {r['full_data'].get('final_answer')}\n"

        ranking_task = f"""Review the INTERNAL reasoning and final reports of your peer specialists.

ASIL KONU: {topic}

PEER INTERNAL DATA TO ANALYZE:
{responses_text}

GÖREVİN:
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
        print("\n✍️ Aşama 3: Chairperson Sentezi (Decoding Complete Council State)...")
        
        stage1_summary = "\n\n".join([f"UZMAN: {r['role']}\nTHOUGHTS: {r['full_data'].get('thought')}\nREPORT: {r['full_data'].get('final_answer')}" for r in valid_responses])
        stage2_summary = "\n\n".join([f"ELEŞTİRMEN: {self.models[i]}\nCRITIQUE: {rankings_raw[i].get('final_answer')}" for i in range(len(rankings_raw))])

        synthesis_task = f"""Synthesize the council's COMPLETE internal dialogue into a final report.

ASIL SORU: {topic}

--- STAGE 1: SPECIALIST REASONING & REPORTS ---
{stage1_summary}

--- STAGE 2: PEER CRITIQUES ---
{stage2_summary}

GÖREVİN:
1. Decode the complex internal dialogue and reasoning between the experts.
2. Resolve conflicts and define the most secure/innovative path.
3. CONVERT the final technical consensus into a PREMIUM TURKISH REPORT for the USER.
"""
        chairperson_prompt = CouncilPrompts.get_prompt("chairperson")
        # Elite Recovery Requirement: Opus 4.6 as President (self.models[1])
        chairperson = SubAgent("Chairperson", model=self.models[1], system_prompt=chairperson_prompt)
        
        # Sentez aşamasında 23-adım beklemeyi (loop) önlemek için max_iters=5 yapıldı.
        final_answer_raw = await chairperson.run(synthesis_task, return_full=True, max_iters=5)
        
        if isinstance(final_answer_raw, dict):
            # Model JSON formatında bitemediyse thought kısmını veya raw yanıtı kurtaralım
            final_answer = final_answer_raw.get("final_answer")
            if not final_answer or final_answer == "Cevap verilmedi.":
                 final_answer = final_answer_raw.get("thought", "Sentez raporu tam olarak oluşturulamadı.")
        else:
            final_answer = final_answer_raw

        return self.generate_report(topic, valid_responses, rankings_raw, final_answer)

    def generate_report(self, topic, stage1, stage2, final):
        report = [f"# 🏛️ Antigravity LLM Council Raporu (Deep Transparency)\n"]
        report.append(f"> **Konu:** {topic}\n")
        
        report.append("## 🛡️ Sentez Raporu (Final Report)")
        report.append(f"{final}\n")

        report.append("---")
        report.append("## 🔬 Konsey İç Diyaloğu ve Akıl Yürütme (Complete Traceability)")
        report.append("Bu bölüm, konsey üyelerinin birbirlerinin düşünce süreçlerini (thoughts) görerek yaptıkları analiz kayıtlarını içerir.\n")
        
        for i, r in enumerate(stage1):
            report.append(f"### 👤 {r['role']} ({r['model']}) İç Süreç")
            report.append(f"**Düşünce Süreci:**\n{r['full_data'].get('thought')}\n")
            report.append(f"**Teknik Rapor (AI-to-AI):**\n```text\n{r['full_data'].get('final_answer')}\n```\n")
            
            # Bu uzmana gelen eleştirileri de ekleyelim
            report.append(f"*Bu uzmana gelen çapraz eleştiriler:* \n{stage2[i].get('final_answer')}\n")

        return "\n".join(report)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python council_orchestrator.py \"Topic\"")
        sys.exit(1)
        
    orchestrator = CouncilOrchestrator()
    asyncio.run(orchestrator.run_council(sys.argv[1]))
