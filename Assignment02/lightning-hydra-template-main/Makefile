setup:
  docker build --tag assignment02:latest .
  docker run assignment02:latest

train:
  docker run assignment01:latest python ./src/train.py experiment=example.yaml

eval:
  docker run assignment01:latest python ./src/eval.py ckpt_path=""
