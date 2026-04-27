# AI_LOG.md

## Tools used

- ChatGPT (GPT-5.3) — used for system design, debugging, and prompt refinement
- Ollama (llama3) — used as the local LLM for inference
- VS Code — development environment

---

## Significant prompts

### Prompt 1: RAG pipeline design
- Prompt: "Design a CLI-based RAG system using local LLM and vector search"
- What AI produced:
  - Suggested retriever, embeddings, and LLM integration
- What I kept:
  - Modular structure (loader, retriever, embeddings, llm)
- What I rejected:
  - Overly complex architecture (kept it simple and testable)

---

### Prompt 2: Citation enforcement
- Prompt: "Ensure every numeric value in the answer is backed by a source"
- What AI produced:
  - Idea of adding citations like [1], [2]
- What I kept:
  - Numbered context and citation mapping
- What I rejected:
  - Blind trust in LLM citations → replaced with validator

---

### Prompt 3: Structured output
- Prompt: "Return sector allocation as structured JSON"
- What AI produced:
  - JSON-style output
- What I kept:
  - Deterministic function using Pydantic-style structure
- What I rejected:
  - LLM-generated structured output (not reliable)

---

## A bug your AI introduced

- Issue:
  The LLM generated numeric values (e.g., stock prices) that were not present in the retrieved context.

- How I caught it:
  Validation logic flagged numbers not found in source chunks.

- Fix:
  Implemented strict validation:
  - Extract numbers from answer
  - Verify against source chunks
  - Mark answer as UNVERIFIED if mismatch

---

## A design choice you made against AI suggestion

- AI suggestion:
  Use LLM for all responses, including structured outputs

- My decision:
  Used deterministic logic for structured outputs (sector exposure)

- Reason:
  - LLM outputs are not reliable for exact numeric computation
  - Deterministic code ensures correctness and reproducibility

---

## Time split

- Prompting & design: 30%
- Coding: 25%
- Debugging: 25%
- Testing & evaluation: 15%
- Documentation: 5%