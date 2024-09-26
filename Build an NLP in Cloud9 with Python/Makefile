install:
		pip install	--upgrade pip && \
			pip install -r '/workspaces/Applied-Python-Data-Engineering-Specialization/Build an NLP in Cloud9 with Python/requirements.txt'
		python -m textblob.download_corpora

test:
		python -m pytest -vv --cov=wikiphrases --cov=nlplogic test_corenlp.py 

format: 
		python -m black nlplogic 

lint: 
		python -m pylint --recursive=y --disable=R,C wikiphrases.py test_corenlp.py

all: install lint test format
