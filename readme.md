+ 训练环境：torch==1.6.0, transformers==2.11.0，apex fp16
+ 训练数据：wikipassageQA
+ 训练模型：BERT+Linear打分，打分大于0则为正类
+ 训练参数：!python3 run.py --do_train --bert_model  "bert-base-uncased" --model_type "MatchModel" --train_file "data/wikipassageQA/train.tsv" --dev_file "data/wikipassageQA/dev.tsv" --test_file "data/wikipassageQA/test.tsv" --do_lower_case --learning_rate 2e-6 --gpu 0 --epochs 10 --batch_size 16 --s1_length 100 --s2_length 400 --seed 1024 --save_dir "result/model" --fp16 --fptype O2
