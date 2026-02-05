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
import matplotlib.pyplot as plt

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
    arr_average = np.mean(arr,axis=1)
    
    # Criando uma figura
    fig, ax = plt.subplots(2)
    
    # Plotando a média e dados brutos
    ax[0].plot(arr_average)
    ax[1].plot(arr)
    
    fig.savefig(r"C:\minicurso_LABHIDRO\figuras"+"/timeSeriesPlot.png", dpi = 300)
    
    return fig, arr_average

