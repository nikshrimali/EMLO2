!git clone https://github.com/atulgupta01/EMLO
!mv ./EMLO/Assignment02/lightning-hydra-template-main ./
!mv lightning-hydra-template-main lightning-hydra-template
!rm -rf EMLO
!pip install -r ./lightning-hydra-template/requirements.txt
!python ./lightning-hydra-template/src/train.py
!python ./lightning-hydra-template/src/eval.py ckpt_path="<path taken from the train.py log>"
