from service.SocrataClient import SocrataClient
import pandas as pd

class CovidDataFrame:

    def __init__(self):
        sc = SocrataClient()
        self.dataframe = pd.DataFrame.from_records(sc.getDataset()).dropna(
            subset=["departamento", "departamento_nom", "edad", "sexo", "fecha_diagnostico", "fecha_recuperado",
                    "fecha_inicio_sintomas"])
        convert_dict = {'departamento': int,
                        'departamento_nom': str,
                        'edad': int,
                        'sexo': str
                        }
        self.dataframe = self.dataframe.astype(convert_dict)
        self.dataframe['fecha_diagnostico'] = pd.to_datetime(self.dataframe['fecha_diagnostico'])
        self.dataframe['fecha_recuperado'] = pd.to_datetime(self.dataframe['fecha_recuperado'])
        self.dataframe['fecha_inicio_sintomas'] = pd.to_datetime(self.dataframe['fecha_inicio_sintomas'])
        self.listaDepartamentos = self.dataframe['departamento_nom'].tolist()
        self.listaDepartamentos = list(dict.fromkeys(self.listaDepartamentos))
        self.listaPaises = self.dataframe['pais_viajo_1_nom'].tolist()
        self.listaPaises = list(dict.fromkeys(self.listaPaises))

    def getDataFrame(self):
        return self.dataframe

    # Crear aqui las consultas
    def getDatosPorEdad(self, e):
        return self.dataframe.query('edad == @e')

    def getDatosPorGenero(self, s):
        return self.dataframe.query('sexo == @s')

    def getDatosPorDepartamento(self, d):
        return self.dataframe.query('departamento_nom == @d')

    def getDatosPorDepartamentoyEdad(self,d,e):
        return self.dataframe[(self.dataframe['departamento_nom']==d)&(self.dataframe['edad']==e)]

    def getDatosPorPaisOrigen(self,p):
        return self.dataframe.query('pais_viajo_1_nom == @p')

    def getListaPaises(self):
        return self.listaPaises

    def getListaDepartamentos(self):
        return self.listaDepartamentos
