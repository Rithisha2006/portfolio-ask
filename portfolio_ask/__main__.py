import sys
from portfolio_ask.retriever import retrieve
from portfolio_ask.llm import ask_llm
from portfolio_ask.structured import calculate_sector_exposure
from portfolio_ask.validator import validate_answer


def run():
    question = sys.argv[1]

    # ✅ Structured output
    if question.lower().strip() == "sector exposure":
        result = calculate_sector_exposure()
        print("\nStructured Output:\n")
        print(result)
        return

    # ✅ Default RAG flow
    results, sources = retrieve(question)

    # Numbered context (important for citations)
    context_list = [
        f"[{i+1}] {text}"
        for i, text in enumerate(results)
    ]
    context = "\n".join(context_list)

    # LLM
    answer = ask_llm(context, question)

    # Validation
    validation = validate_answer(answer, sources)

    print("\nAnswer:\n")
    print(answer)

    print("\nSources:\n")
    for key, value in sources.items():
        print(f"{value[:80]}... {key}")

    print("\nValidation:\n")
    print(validation)


if __name__ == "__main__":
    run()