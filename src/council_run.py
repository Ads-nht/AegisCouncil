import asyncio
import sys
import os

# Ensure we can import from src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from council_orchestrator import CouncilOrchestrator

def _expand_topic_arg(topic_arg: str) -> str:
    """
    Allow passing a local context file path as the "topic" argument.

    - If the argument is a readable file path (absolute or relative), read it and
      embed the contents into the topic so council agents receive full context.
    - Otherwise, return the argument unchanged.
    """
    candidate = topic_arg.strip()
    # Support common "Audit using context file: /abs/path" usage as well.
    if "context file:" in candidate:
        maybe_path = candidate.split("context file:", 1)[1].strip()
        if maybe_path:
            candidate = maybe_path

    if os.path.isfile(candidate):
        abs_path = os.path.abspath(candidate)
        try:
            with open(abs_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
        except Exception as e:
            return f"{topic_arg}\n\n[ERROR: Failed to read context file '{abs_path}': {e}]"

        return (
            "AUDIT INPUT SOURCE: local file\n"
            f"AUDIT INPUT PATH: {abs_path}\n\n"
            "--- START CONTEXT DOCUMENT ---\n"
            f"{content}\n"
            "--- END CONTEXT DOCUMENT ---\n"
        )

    return topic_arg

async def main():
    if len(sys.argv) < 2:
        print("Usage: python council_run.py \"Your complex question or topic\"")
        sys.exit(1)

    topic = _expand_topic_arg(sys.argv[1])
    
    # Optional: Models can be customized here
    models = [
        # Prefer a model that reliably returns STRICT JSON via OpenRouter.
        "google/gemini-2.5-flash",
        "google/gemini-2.5-flash",
        "google/gemini-2.5-flash"
    ]
    
    council = CouncilOrchestrator(models=models)
    report = await council.run_council(topic)
    
    # Save the report to logs
    log_path = f"/home/ads/Antigravity/Projeler/LLM_Council/logs/council_report_{int(asyncio.get_event_loop().time())}.md"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    with open(log_path, 'w') as f:
        f.write(report)
        
    print(f"\n✅ Konsey toplantısı bitti. Rapor oluşturuldu: {log_path}")
    print("\n--- RAPOR BAŞLANGICI ---\n")
    print(report)
    print("\n--- RAPOR SONU ---\n")

if __name__ == "__main__":
    asyncio.run(main())
