from utils.tokenizer import train_subword_tokenizer
from preprocess import data_preparation
from argparse import ArgumentParser
import os

# argument
parser = ArgumentParser()
parser.add_argument('--train_500hr_corpus_dir', default='../ASR_char/data/LibriSpeech-500/LibriSpeech/train-other-500', type=str)
parser.add_argument('--train_360hr_corpus_dir', default='data/LibriSpeech-100/LibriSpeech/train-other-100', type=str)
parser.add_argument('--train_100hr_corpus_dir', default='data/LibriSpeech-360/LibriSpeech/train-other-360', type=str)
parser.add_argument('--save_dir', default='subword/', type=str)
parser.add_argument('--size', default=500, type=int)

args = parser.parse_args()

save_dir = args.save_dir

def main():
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    texts_all = []
    for path in [args.train_100hr_corpus_dir, args.train_360hr_corpus_dir, args.train_500hr_corpus_dir]:
        texts, audio_path = data_preparation(path)
        texts_all += texts

    # save to subword/
    with open(save_dir+"/corpus_all.txt", 'w') as fout:
        fout.write("\n".join(texts_all))
    
    special_tokens = ['<PAD>', '<SOS>', '<EOS>', '<SPACE>']
    train_subword_tokenizer(args.size, special_tokens, save_dir)



if __name__ == '__main__':
    main()
