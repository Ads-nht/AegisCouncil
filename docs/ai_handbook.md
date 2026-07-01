# 🛠 AI Handbook: Antigravity LLM Council Integration

If you need to delegate a complex code audit or architectural decision, use the **LLM Council** as your primary **Autonomous Audit Tool**.

## 📞 How to Invoke
Run this terminal command:
```bash
python /home/ads/Antigravity/Projeler/LLM_Council/src/council_run.py "<Your Topic or Code>"
```

## 🧠 System Architecture
1. **Multi-Expert Analysis**: 3 specialized agents (Security, Technique, Vision) audit the topic in parallel.
2. **Deep Transparency**: Agents critique each other's *internal thought processes*, not just their final reports.
3. **Inner Dialogue**: Internal comms are optimized for machine readability (Technical English/JSON).
4. **Synthesis**: Results are decoded into a final Premium Turkish report.

## 📜 Communication Protocol (Rules for You)
- **Inputs**: Provide full context (Source code, specific concerns).
- **Internal Stages**: If you are part of the council, use technical English and JSON blocks in your `final_answer` to pass data efficiently to peer agents.
- **Thought Enforcement**: Always populate the `thought` field with deep logical reasoning.
- **Reporting**: Final output should be handled by the Chairperson for human-readable Turkish synthesis.

## 🎯 Use Cases
- **Security Audit**: Finding logical flaws (CWE) and vulnerabilities (OWASP).
- **Architecture Review**: Ensuring SOLID, Clean Architecture, and scalability.
- **Product Strategy**: Innovation mapping and growth analysis.

---
*For machine-readable spec, see: `docs/ai_usage_guide.json`*
