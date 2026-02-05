# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 15:26:28 2026

@author: brito
"""

# Importando pacotes
import firstScript
import numpy as np

# Array de valores aleatórios
arr = np.random.rand(100,100)

# Executando função timeSeriesPlot em firstScript
firstScript.timeSeriesPlot(arr)