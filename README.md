# Pretraining-Yourself-Bert-From-Scratch
从头训练MASK BERT

1.将需要训练的语料库转为训练集测试集

2.可以取这个地址下载[训练代码](https://github.com/huggingface/pytorch-pretrained-BERT)  
## How to start
- Preparing your dataset, train and dev, and place them into the data directionary

3.构建词表，需要包含[PAD] [UNK] [CLS] [SEP] [MASK]
- Building a vocab as bert_vocab.txt. Note that the vocab should include [PAD] [UNK] [CLS] [SEP] [MASK]

4.修改配置文件
- Change the bert_config.json. Alternatively, you can change the model size to fit your memory.  The current num_layer is set to 4, same as the [MASS](https://github.com/microsoft/MASS) model (k=1) by microsoft.  Besides, you also should change the vocab_size in the config file based on your vocab

5.执行函数即可
- python run_pretraining.py
