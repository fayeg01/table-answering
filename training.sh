pip install -r requirements.txt
pip install --upgrade gdown
gdown 1-ru15BYuPAF2ErhPnf6DTDV7hIdVtjwC
unzip bert-base-french-europeana-cased.zip -d ./tapas/TapasData/
rm -rf tapas/WikiSQLOutput/wikisql/
python3 run_task_main.py \
  --task="WIKISQL" \
  --input_dir="tapas/WikiSQLData" \
  --output_dir="tapas/WikiSQLOutput" \
  --bert_vocab_file="tapas/TapasData/bert-base-french-europeana-cased/vocab.txt" \
  --mode="create_data"
python3 run_task_main.py \
  --task="WIKISQL" \
  --output_dir="tapas/WikiSQLOutput" \
  --init_checkpoint="tapas/TapasData/bert-base-french-europeana-cased/model.ckpt" \
  --bert_config_file="tapas/TapasData/bert-base-french-europeana-cased/config.json" \
  --mode="train"