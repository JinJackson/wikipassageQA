import json
pairs = []


# with open('data/wikipassageQA/document_passages.json') as reader:
#     context = reader.read()
#     doc_dict = json.loads(context)
#     #Q:What is the role of conversionism in Evangelicalism? 672	Evangelicalism.html	4
#     #print(doc_dict['672']['4'])
#
# with open('data/wikipassageQA/train.tsv', 'r', encoding='utf-8') as reader:
#     lines =  reader.readlines()
#     info = lines[1].strip().split('\t')
#     #['3086', 'What is the role of conversionism in Evangelicalism?', '672', 'Evangelicalism.html', '4']
#
#     Q = info[1]
#     doc_index = info[2]
#     Answers = doc_dict[doc_index]
#     len_Answers = len(Answers)
#     Answer_index = [str(i) for i in range(len_Answers)]
#     pos_index = info[-1].split(',')
#     neg_index = sorted(list(set(Answer_index).difference(set(pos_index))), key= lambda x: int(x))
#     for index in pos_index:
#         pairs.append([Q, Answers[index], 1])
#
#     for index in neg_index:
#         pairs.append([Q, Answers[index], 0])

    #for index in pos_index:
import codecs
data_file = 'data/wikipassageQA/train.tsv'
doc_file = 'data/wikipassageQA/document_passages.json'

def getBertData(data_file, doc_file):

    pairs = []

    with codecs.open(doc_file, 'r', encoding='utf-8') as reader:
        context = reader.read()
        doc_dict = json.loads(context)

    with codecs.open(data_file, 'r', encoding='utf-8') as reader:
        lines = reader.readlines()
        for line in lines:
            info = line.strip().split('\t')
            # ['3086', 'What is the role of conversionism in Evangelicalism?', '672', 'Evangelicalism.html', '4']

            Q = info[1].strip()
            doc_index = info[2]
            Answers = doc_dict[doc_index]
            len_Answers = len(Answers)
            Answer_index = [str(i) for i in range(len_Answers)]
            pos_index = info[-1].split(',')
            neg_index = sorted(list(set(Answer_index).difference(set(pos_index))), key=lambda x: int(x))
            for index in pos_index:
                pairs.append([Q, Answers[index].strip(), 1])
            for index in neg_index:
                pairs.append([Q, Answers[index].strip(), 0])
    return pairs
result = getBertData(data_file, doc_file)
print(len(result))