from numpy import select

from service.SocrataClient import SocrataClient
import numpy as np
import pandas as pd

#Crear aqui las consultas

class CovidDataFrame:

    def __init__(self):
        sc = SocrataClient()
        self.dataframe = pd.DataFrame.from_records(sc.getDataset())

    def getDataFrame(self):
        return self.dataframe



