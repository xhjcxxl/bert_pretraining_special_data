import pandas as pd
import numpy as np


def split_text(infile, train_file, valid_file, seed=999, ratio=0.1):
    df = pd.read_csv(infile)  # 没有表头
    print(df.shape)
    idxs = np.arange(df.shape[0])  # df.shape 为数据的维度
    np.random.seed(seed)
    np.random.shuffle(idxs)
    val_size = int(len(idxs) * ratio)
    print(val_size)
    df.iloc[idxs[:val_size], :].to_csv(valid_file, index=False, header=None)  # 不保存表头，不保存索引
    df.iloc[idxs[val_size:], :].to_csv(train_file, index=False, header=None)


split_text(infile='corpus.txt', train_file='text_train.csv', valid_file='text_valid.csv')