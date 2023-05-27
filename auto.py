import shutil
import time
import logging 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from selenium import webdriver
import os

source_dir = "/Users/user/Pictures/"
fact_dir = "/Users/user/Documents/A KINESIO/FACTURACION/"
for files in os.listdir(source_dir):

    name, extension = os.path.splitext(files)
    
    if extension in [".pdf", ".docx"]:
        file = name + extension

        splitted = name.split(" ")
        splitted = [s.strip() for s in splitted]
        new_name = []
        
        for split in splitted:
            new_name.append(split)
        
        months = ["1",'2','3','4','5','6','7','8','9','10','11','12'] 
        
        if new_name[1] in months:
            new_path = shutil.move(f"{source_dir}/{file}", fact_dir) 
            print(new_path)

for files in os.listdir(fact_dir):
    
    name, extension = os.path.splitext(files)

    if not extension in [".pdf", ".docx"]:
        continue
    
    splitted = name.split(" ")
    splitted = [s.strip() for s in splitted]
    new_name = []
    for split in splitted:
        new_name.append(split)
    
    months = ["1",'2','3','4','5','6','7','8','9','10','11','12'] 
    
    if len(new_name) >= 3:
        if not new_name[1] in months:
            continue
    else:
        continue
    print(new_name)
    
    file = name + extension

    nombre = []
    for name in range(2,len(new_name)):
        nombre.append(new_name[name])
    nombre = " ".join(nombre)
    print(nombre)
    
    """     print(os.listdir(f"{fact_dir}/{new_name[0]}"))  """
    if new_name[0] in os.listdir(fact_dir):
        print(files, new_name[0])
        path = shutil.move(f"{fact_dir}/{file}", f"{fact_dir}/{new_name[0]}")
        print(path)
    else: 
        continue
    new_name[2] = nombre
    print(new_name[2])
    pacient = new_name[2]
    if pacient in os.listdir(f"{fact_dir}/{new_name[0]}"):
        
        path = shutil.move(f"{fact_dir}/{new_name[0]}/{file}", f"{fact_dir}/{new_name[0]}/{pacient}")        
        print(path)
    else:
        os.mkdir(f'{fact_dir}/{new_name[0]}/{new_name[1]}', exist_ok=True)
    
    month = new_name[1]

    if month in os.listdir(f"{fact_dir}/{new_name[0]}/{pacient}"):
        path = shutil.move(f"{fact_dir}/{new_name[0]}/{pacient}/{file}", f"{fact_dir}/{new_name[0]}/{pacient}/{month}")
        print(path)
    else:
        os.mkdir(f'{fact_dir}/{new_name[0]}/{new_name[1]}/{pacient}/{month}', exist_ok=True)
