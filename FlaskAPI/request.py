#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 00:14:52 2020

@author: mansikosamkar
"""

from requests import get
from data_input import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = get(URL,headers=headers, json=data) 

print(r.json())