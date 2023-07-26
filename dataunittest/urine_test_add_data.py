import pandas as pd
import numpy as np

class UrineTestAddData():
    
    def __init__(self, path):
        self.df = pd.read_csv(path)
    
    def set_columns_name(self):
        self.cols_list = []   
        self.cols_list = self.df.columns.values.tolist()
    
    # this method returns the latest version of the self.df
    def get_df(self):
        return self.df
    
    
    def add_record(self, new_row):
    
        try:
            self.df.loc[len(self.df)] = new_row
            #TODO: Save the modified df in the file
            return True
        except Exception as e:
            #TODO: e Can be used later
            return False
        
            
    # TODO: this method saves the latest version of the self.df to the csv file
    def save_record(self):
        pass
