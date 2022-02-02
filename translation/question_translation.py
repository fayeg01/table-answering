from transformers import pipeline
import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd
from tqdm import tqdm
import numpy as np

translator = pipeline('translation_en_to_fr', device = 0, model = 't5-small')

def translate_sub_df(df, line_begin, line_end):
  """
  Transates the questions of a sub data frame
  inputs:
    - df: the whole data frame to translate
    - line_begin: the first_line of the sub dataframe
    - line_end: the last line of the sub dataframme
  outputs:
    - translated_df: the translated sub data frame
  """
  sub_df = df.iloc[line_begin:line_end]
  sample = list(sub_df.question)
  translation = translator(sample)
  translation = list(map(lambda x:x['translation_text'], translation))
  sub_df.question = translation
  return sub_df

def translate_whole_df (df, path, batch_size = 100):
  """
  Translate the data frame batch by batch and save intermediate steps 
  in a checkpoint file
  inputs:
    - df: the whole dataframe to translate
    - path: the path of the checkpoint (same as the path of the final translated data_frame)
    - batch_size: the size of the batch to translate
  outputs:
    - None
  """
  n = df.shape[0]
  number_of_batches = n//batch_size

  for batch_number in tqdm(range(0,number_of_batches), position = 0):
    ### load previous checkpoint
    if batch_number != 0:
      previous_checkpoint = pd.read_csv(path)
    else:
      previous_checkpoint = pd.DataFrame(columns = df.columns)

    ### translate_sub_df
    line_begin = batch_number*batch_size
    if batch_number != number_of_batches-1:
      line_end =  (batch_number+1)*batch_size
    else:
      line_end =  None
    translated_sub_df = translate_sub_df(df, line_begin, line_end)

    # concat_df
    new_checkpoint = pd.concat([previous_checkpoint, translated_sub_df], axis = 0)
    
    # save_df
    new_checkpoint.to_csv(path, index = False)
  return


