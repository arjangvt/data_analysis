import unittest
from pandas.testing import assert_frame_equal
from urine_test_add_data import UrineTestAddData

class TestAddData(unittest.TestCase):
    
    #TODO: below is my my unsuccessful attempts to use "assert_frame_equal" panda's library to check the type of data that is inserted into 
    #      the dataframe!
    #      It appears the library is not widely used. There might be some alternative libraries that I may not know them!
    #      It is possible to write a code that compare the types of a given row to original dataframe.
    #      Unfortunately I ran out of time!
    
    #print(self.df.iloc[[0]])
    #df_new_row = pd.DataFrame([new_row], columns=self.cols_list)
    #print(df_new_row)
    #print(self.df.iloc[[0]])
    #print(np.array_equal(self.df.iloc[[0]].values, df_new_row.values))
    #assert_frame_equal(self.df.iloc[[0]], df_new_row, check_dtype=False, check_index_type=False, check_exact=False, check_column_type=False, check_frame_type=False, check_categorical=False)
    #df_new_row = pd.DataFrame([new_row], columns=self.cols_list)
    #pdt.assert_frame_equal(self.df, df_new_row, check_dtype=True, check_less_precise=True)    
        
    # This testcase tests if the input list contains less element as dataframe columns
    def test_add_less_item(self):
        path = "../data/urine_test_data.csv"
        ut = UrineTestAddData(path)
        ut.set_columns_name()
        # the correct data
        # ['Sample_1001',0, 565, 505, 319, 0, 0, 0, 0, 0, 0, 'R', 'R', 'R', 'S', 'S', 'S', 'R', 'R', 'R', 'S', 'R', 'R', 'S', 'S', 'R', 'S', 'R',	0, 0, 0, 0, 0]
        
        new_row = ['Sample_1001',0, 565, 505, 319, 0, 0, 0, 0, 0, 0, 'R', 'R', 'R', 'S', 'S', 'S', 'R', 'R', 'R', 'S', 'R', 'R', 'S', 'S', 'R', 'S', 'R',	0, 0, 0, 0]
        retVal = ut.add_record(new_row)
        
        self.assertEqual(retVal, True, 'The addrecord is wrong.')

    

if __name__ == '__main__':
    unittest.main()