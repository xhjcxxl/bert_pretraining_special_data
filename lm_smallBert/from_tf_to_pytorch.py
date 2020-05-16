import tensorflow as tf
import torch
from transformers import convert_bert_original_tf_checkpoint_to_pytorch as ctp


BERT_BASE_DIR = "uncased_L-12_H-768_A-12/"
tf_checkpoint_path = BERT_BASE_DIR + "bert_model.ckpt"
bert_config_file = BERT_BASE_DIR + "bert_config.json"
pytorch_dump_path = BERT_BASE_DIR + "pytorch_model.bin"


ctp.convert_tf_checkpoint_to_pytorch(tf_checkpoint_path, bert_config_file, pytorch_dump_path)
