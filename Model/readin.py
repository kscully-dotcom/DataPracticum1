# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:29:27 2024

@author: java
"""

import params

mergedFile = params.fileCPI.merge(params.fileRecession, how='left', on='Date')