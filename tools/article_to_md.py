# -*- coding: utf-8 -*-
# @Author : Jesse.T
# @Time   : 2019/10/18 10:21
import os
from logzero import logger
from article.models import ArticlePost
"""
将数据库中文章保存为md文件
"""
articles = {}
_ = [articles.update({i.id:i}) for i in ArticlePost.objects.all()]
logger.info(f'got {len(articles)} articles from database')

files = [int(i.strip('.md')) for i in os.listdir('md_articles')]
logger.info(f'got {len(files)} files from database')

tasks = [i for i in articles if i not in files]
logger.info(f'got {len(tasks)} tasks from database')

for id in tasks:
    article = articles[id]
    with open(f'md_articles/{id}.md','w+',encoding='utf-8') as f:
        f.write(article.title+'\n'+article.body)
logger.info('finished')
