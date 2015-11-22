start:
	python blackadder/adder.py

example:
	curl -H "Content-Type: application/json" -X POST -d "{\"a\": 4, \"b\": 5}" http://localhost:8080/

test:
	py.test tests/
