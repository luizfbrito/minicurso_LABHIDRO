# -*- coding: utf-8 -*-
"""

------------------------------------first_script.py------------------------------------------------------------------

Este script é utilizado para...
Created on Thu Feb 5
@author: luizfbrito

---------------------------------------------------------------------------------------------------------------------

"""

# Importação de pacotes para usar este script
import numpy as np
import matplotlib as pl

def timeSeriesPlot(arr):
    """
    
    Parameters
    ----------
    arr : np.array
        array com a matriz de dados.

    Returns
    -------
    fig : TYPE
        DESCRIPTION.
        
    arr_average: numpy array

    Exemplos de uso:
        fig, arr_average = timeSeriesPlot(arr)
        
    """
    
    # Média no eixo 1
    