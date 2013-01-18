#!/bin/python
"""Categorize a book with barcode."""

__author__ = 'Royce Remer (royceremer@gmail.com)'
__date__ = '01/16/2013'

#TODO: use an encrypted yaml

import pyaml.yaml as yaml

CREDS_FILEPATH='/home/royceremer/source/fophl_book_sorter/credentials.yaml'
with open(CREDS_FILEPATH,'r') as creds_yaml:
	creds_dict = yaml.load(creds_yaml)

aws_api = amazonproduct.API(
	creds_dict.get('aws_access_key_id'),
	creds_dict.get('aws_secret_access_key'),
	'en') # 'en' is not a valid region...
#TODO: impliment node each time it's invoked so that variable terms get pulled
	
