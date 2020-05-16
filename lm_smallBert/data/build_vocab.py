import gensim
import codecs


def build_vocab(vocab_file):
    with codecs.open(vocab_file, "w", "utf-8") as f:
        for i in range(51200):
            f.write(str(i) + '\r\n')
        f.write(str("[PAD]") + '\r\n')
        f.write(str("[UNK]") + '\r\n')
        f.write(str("[CLS]") + '\r\n')
        f.write(str("[SEP]") + '\r\n')
        f.write(str("[MASK]") + '\r\n')


build_vocab('bert_vocab.txt')