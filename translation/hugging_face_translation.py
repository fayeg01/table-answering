from transformers import pipeline
import torch
from torch.utils.data import Dataset
import pandas as pd
import os
import numpy as np
from tqdm import tqdm
import deepl 

import yaml

with open("config.yaml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

def get_translator(model='t5-small', device=-1):
    return pipeline('translation_en_to_fr', device = device, model = model)

device = 0 if torch.cuda.is_available() else -1
translator = get_translator(device= device)

class MyDataset(Dataset):
    def __init__(self,to_tranlate):
        self.samples = to_tranlate
        super().__init__()
    def __getitem__(self,index):
        return self.samples[index]
    def __len__(self):
        return len(self.samples)

def translate_header(row):
    """Translates the header of the table with transformers"""
    for auth_key in cfg['deepl']["AUTH_KEY"]:
        try:
            translator = deepl.Translator(auth_key) 

            header = row['header']
            to_translate = ''
            for word in header:
                to_translate += str(word) + '+'
            return translator.translate_text(to_translate, target_lang='fr').text.split('+')[:-1]
        except:
            continue
        
    print("ALL DEEPL ACCOUNTS ARE EMPTY")
            

def translate_key(row,key):
    """Transates a key of the dataframe which is not header nor rows"""
    cell = str(row[key])
    return translator(cell)[0]["translation_text"]


def translate_rows(row):
    """Translates the rows of the table with transformers"""
    r = row['rows']
    to_translat = []
    indices_not_to_translate = []
    not_to_translate = []
    indice = [0,0]

    for l in r:
        for v in l:
            if str(v).isnumeric() or (''.join(e for e in v if e.isalnum())).isnumeric():
                not_to_translate.append(str(v))  #If the value is a number we don't run an inference on it
                indices_not_to_translate.append(indice.copy())
            else:
                to_translat.append(str(v))
            indice[1] += 1
        to_translat.append('?????')
        indice[0] += 1
        indice[1] = 0

    dataset = MyDataset(to_translat)
    translation = list(translator(dataset))
    out = [[]]
    indice = [0,0]
    for i in range(len(translation)):
        while len(indices_not_to_translate)>0 and indice == indices_not_to_translate[0]:
            out[-1].append(not_to_translate[0])
            _ = indices_not_to_translate.pop(0)
            _ = not_to_translate.pop(0)
            indice[1] += 1
        if translation[i]['translation_text'] == '?????':
            out.append([])
            indice[0] += 1
            indice[1] = 0
        else:
            out[-1].append(translation[i]['translation_text'])
            indice[1]+=1

    return out[:-1]

keys_to_translate = ['page_title', 'section_title', 'caption', 'name']

def translate_dataframe(df):
    values = {k:[] for k in keys_to_translate}
    values['rows'] = []



    for k in df.keys():
        if not (k in keys_to_translate or k=='rows'):
            values[k] = list(df[k])
    for i in tqdm(range(df.shape[0])):
        for k in keys_to_translate:
            values[k].append(translate_key(df.iloc[i],k))
        values['rows'].append(translate_rows(df.iloc[i]))

    df_transl = pd.DataFrame.from_dict(values)
    return df_transl