build:
	docker build --tag ${IMAGE_NAME} .

train:
	python ./src/train.py

eval:
	python ./src/eval.py

test:
	pytest -k "not slow"

test-full:
	pytest

mount:
	docker run -it -v `pwd`:/workspace/project ${IMAGE_NAME}
