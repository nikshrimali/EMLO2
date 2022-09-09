# Testing of CIFAR Integration
## For testing of my code changes, following commands were executed in the Google Colab

  - !git clone https://github.com/atulgupta01/EMLO
  - !mv ./EMLO/Assignment02/lightning-hydra-template-main ./
  - !mv lightning-hydra-template-main lightning-hydra-template
  - !rm -rf EMLO
  - !pip install -r ./lightning-hydra-template/requirements.txt
  - !python ./lightning-hydra-template/src/train.py
  - !python ./lightning-hydra-template/src/eval.py ckpt_path="<Path from the training>"
 
### EMLO_Assignment02.ipynb is uploaded in this repository
### To Create Docker run - <b>make setup</b>
### for training - <b>make train</b>
### for eval - <b>make eval</b>
