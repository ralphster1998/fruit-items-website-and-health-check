#!/usr/bin/env python3

import os
import datetime

from reports import generate_report
from run import data_catalog
from emails import send_email, generate_email

def pdf_body(input_for,desc_dir):
    """Generating a summary with two lists, which gives the output name and weight"""
    weight_output = []
    name_output = []
    for fruit_item in os.listdir(desc_dir):
      name_file=os.path.join(desc_dir,fruit_item)
      with open(name_file) as f:
        line=f.readlines()
        name=line[0].strip('\n')
        weight=line[1].strip('\n')
        name_output.append('name: ' +name)
        weight_output.append('weight: ' +weight)
        print(name,weight)
        print(name_output)
        print(weight_output)
    object_new = ""  # initializing the object
    # Calling values from two lists one by one.
    for i in range(len(name_output)):
        if name_output[i] and input_for == 'pdf':
            object_new += name_output[i] + '<br />' + weight_output[i] + '<br />' + '<br />'
    return object_new

if __name__ == "__main__":
    username = os.getenv('USER')
    description_directory = '/home/{}/supplier-data/descriptions/'.format(username) 
    current_date = datetime.date.today().strftime("%B %d, %Y") 
    title = 'Processed Update on ' + str(current_date) 
    generate_report('/tmp/processed.pdf', title, pdf_body('pdf',description_directory))  
    subject_email = 'Upload Completed - Online Fruit Store'  
    body_email = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.' 
    msg = generate_email("automation@example.com", "{}@example.com".format(username),
                         subject_email, body_email, "/tmp/processed.pdf")  
    send_email(msg)