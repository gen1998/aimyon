# coding: utf-8
import pickle
import numpy as np
import sys
sys.path.append('deep-learning/')
from common.time_layers import *
from common.base_model import BaseModel
from common.functions import softmax
from common.optimizer import SGD
from common.trainer import RnnlmTrainer
from ch06.rnnlm import Rnnlm
from common.util import preprocess, create_contexts_target, convert_one_hot

def display(txt_file_name=None,rnn_file_name=None):
    """
    txt_file_name : mecab実行後のtxtファイル
    rnn_file_name : pykle形式のの学習後データ
    """
    
    with open(rnn_file_name, 'rb') as f:
        params = pickle.load(f)

    layers = [
                TimeEmbedding(params[0]),
                TimeLSTM(params[1], params[2], params[3], stateful=True),
                TimeAffine(params[4], params[5])
            ]
    
    # 学習データの読み込み
    with open(txt_file_name) as f:
        mecab_data = f.read()

    corpus, word_to_id, id_to_word = preprocess(mecab_data)

    number=np.random.randint(0,len(word_to_id),(1,10))
    
    
    start_word = '私'
    start_id = word_to_id[start_word]
    word_ids = [start_id]
    xs=start_id
    while(len(word_ids)<100):
        xs = np.array(xs).reshape(1, 1)
        for layer in layers:
            xs = layer.forward(xs)
        p = softmax(xs.flatten())

        sampled = np.random.choice(len(p), size=1, p=p)
        xs=int(sampled)
        word_ids.append(int(xs))
        
    txt = ''.join([id_to_word[i] for i in word_ids])    
        
    return txt
