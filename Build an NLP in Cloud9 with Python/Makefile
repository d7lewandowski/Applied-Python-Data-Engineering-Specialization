install:
		pip install	--upgrade pip && \
			pip install -r requirements.txt
		python -m textblob.download_corpora

test:
		python -m pytest -vv --cov=hello test_hello.py

format: 
		python -m black nlplogic 

lint: 
		pylint --disable=R,C hello.py

all: install lint test format
