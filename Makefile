install:
	python -m pip install --upgrade pip
		pip install -r requirements.txt

format:	
	black myapp/*.py 

lint:
	ruff check myapp/*.py

#  container-lint:
#  	docker run --rm -i hadolint/hadolint < Dockerfile

test1:
	python myapp/test_script.py

test2:
	py.test --nbval myapp/notebook.ipynb

test3:
	python myapp/test_lib

run:
	python myapp/main.py
		
all: install format lint test run
