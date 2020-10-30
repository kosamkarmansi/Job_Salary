#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 04:18:04 2020

@author: mansikosamkar
"""



import glassdoor_scraper as gs
import pandas as pd

path = "/Users/mansikosamkar/Desktop/projects/Job_Salary/chromedriver"

df = gs.get_jobs('data analyst', 800, False, path, 15)
df.to_csv('glassdoor_jobs.csv', index = False)
