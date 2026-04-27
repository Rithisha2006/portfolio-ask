import ollama


def ask_llm(context, question):
    prompt = f"""
You are a strict financial assistant.

RULES:
1. Answer ONLY using the context.
2. Use ONLY the numbered context [1], [2], etc.
3. EVERY number MUST have a citation immediately after it.
4. DO NOT use numbering like 1., 2.
5. DO NOT output index numbers.
6. DO NOT write numbers like (1450) without citation.
7. ALWAYS follow this format EXACTLY:

FORMAT:
- TCS - 3500 [1]
- INFY - 1450 [2]

Context:
{context}

Question:
{question}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']