import os
import re
import requests
import glob

def getXml( file_path, output_filepath):
    url = "http://localhost:8070/api/processFulltextDocument"
    filename = file_path.split("/")[-1].split(".")[-2]
    params = dict(input=open(file_path , 'rb'))
    response = requests.post(url, files=params, timeout=300)
    fh = open(os.path.join(output_filepath ,filename + ".xml"), "w", encoding="utf-8")
    fh.write(response.text)
    fh.close()

def run(files_paths,files):
    
    for file_path in files_paths :
        
        getXml(file_path, files)


if __name__ ==  "__main__":
    files = "./data/grobid_data"
    files_path = [os.path.join(files, i)  for i in os.listdir(files)]
    run(files_path,files)