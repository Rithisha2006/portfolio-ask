setup:
	pip install -r requirements.txt
	ollama pull llama3

run:
	python -m portfolio_ask "What is my IT exposure?"

eval:
	python evals/run_eval.py