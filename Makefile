install:
	python -m pip install --upgrade pip
		pip install -r requirements.txt

format:	
	black *.py 

lint:
	ruff check *.py

#  container-lint:
#  	docker run --rm -i hadolint/hadolint < Dockerfile

test1:
	python test_script.py

test2:
	python test_lib.py

test3:
	 python -m pytest -vv --nbval -cov=myapp -cov=main *.ipynb

run:
	python script.py
		
all: install format lint test1  test2 test3 run
