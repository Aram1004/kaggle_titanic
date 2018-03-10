# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 14:02:57 2018

@author: 김아람
"""

import pandas as pd

train = pd.read_cvs('input/train.cvs')
test = pd.read_csv('input/test.cvs')

train.head()
train.info()
