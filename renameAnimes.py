import os,re
from os.path import isdir
import shutil
import json

names = json.load(open('/media/amaury/DATOS/ANIMES/Utiles/animeList.json', 'r'))

dirname = '/media/amaury/DATOS/ANIMES'

file_list = os.listdir(dirname)

for video in filter(lambda x: re.match("([0-9]{4})([_]{1})+",x) and  names.get(x[:4],False) ,file_list):
    if names.get(video[:4],False):
        shutil.move(dirname + '/' + video, dirname + '/' + names.get(video[:4]) + video[4:])    
        print(video)
print('Done')
