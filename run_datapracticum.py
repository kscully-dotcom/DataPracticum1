# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:04:14 2024

@author: java
"""

import sys
import logging
import click

from model.run import runner

if __name__ == "__main__":
    
    root = logging.getLogger()
    
    root.setLevel(logging.DEBUG)
    
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s %(levelname) -8s %(module) -8s %(funcName) -12s %(message)s',
        datefmt='%H:%M:%S')
    ch.setFormatter(formatter)
    
    root.addHandler(ch)
    
    runner()