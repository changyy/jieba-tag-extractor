#encoding=utf-8
import sys
sys.path.append('../jieba')

import jieba
import jieba.analyse

data = sys.stdin.readlines()
tags = jieba.analyse.extract_tags("\n".join(data), topK=50)

print repr(tags).decode("unicode-escape")
