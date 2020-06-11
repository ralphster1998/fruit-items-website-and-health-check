#!/usr/bin/env python3

import requests, os, json

def data_catalog(url,directory_description):
    """This function will return a list of dictionaries with all the details like name, weight, description, image_name.
    It will change the weight to integer format.
    """
    fruit_item={}
    for checked_fruit_item in os.listdir(directory_description):
      fruit_item.clear()
      file_name=os.path.join(directory_description,checked_fruit_item)
      with open(file_name) as f:
        line=f.readlines()
        text_description=""
        for i in range(2,len(line)):
          text_description=text_description+line[i].strip('\n').replace(u'\xa0',u'')
        fruit_item["description"]=text_description
        fruit_item["weight"]=int(line[1].strip('\n').strip('lbs'))
        fruit_item["name"]=line[0].strip('\n')
        fruit_item["image_name"]=(checked_fruit_item.strip('.txt'))+'.jpeg'
        print(fruit_item)
        if url!="":
          response=requests.post(url, json=fruit_item)
          print(response.status_code)
          print(response.request.url)
    return 0 #Meaning this should be good. 
        
if __name__=='__main__':
    user = os.getenv('USER')
    url = 'http://localhost/fruits/'
    description_directory = '/home/{}/supplier-data/descriptions/'.format(user)
    data_catalog(url,description_directory)