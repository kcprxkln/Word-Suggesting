import pandas as pd 

class CsvConverter():        
    def convert_to_dict(self, file):
        self.file = file
        dictionary = pd.read_csv(self.file, header = None, dtype = {0:str}).set_index(0).squeeze().to_dict()
        return dictionary