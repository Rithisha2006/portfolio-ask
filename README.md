# Portfolio Ask (RAG + LLM CLI)

## Overview
Portfolio Ask is a command-line tool that answers questions about a financial portfolio using Retrieval-Augmented Generation (RAG) and a local Large Language Model (LLM) via Ollama.

The system retrieves relevant portfolio and news data, feeds it into an LLM, and produces answers with strict citation validation.

---

## Features

- Retrieval-Augmented Generation (RAG)
- Local LLM using Ollama (llama3)
- CLI interface (`python -m portfolio_ask`)
- Structured output (sector exposure)
- Citation-based answers
- Strict validation for numeric claims (hallucination control)
- Evaluation system with PASS/FAIL results

---
## Design Highlights

- Combines LLM reasoning with deterministic validation to ensure factual correctness of numeric outputs  
- Built with a reproducibility-first approach: a reviewer can run the full system in under 10 minutes using `make setup`, `make run`, and `make eval`

---
## Hallucination Note

In this project, *hallucination* refers to the LLM generating information (especially numbers like prices or percentages) that is not present in the retrieved portfolio or news data.

To reduce this, a validation step is applied after the LLM generates an answer:
- All numeric values in the answer are extracted
- Each value must appear in the cited source chunks
- If any number is not supported by the sources, the answer is marked as **UNVERIFIED**

This approach reduces hallucination by enforcing evidence-based outputs. However, it does not eliminate it completely, since the LLM may still produce unsupported text or incorrect reasoning that is not fully captured by numeric validation.

## Setup

```bash
make setup