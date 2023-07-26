
## Table of contents
* [Data Visualization](#data-visualization)
  * Task 1: The percentage of samples resistant (R) and sensitive (S) to each antibiotic.
  * Task 2: The presence of each resistance gene across the samples.
  * Task 3: The distribution of cell counts for each organism.
* [Unit Testing](#unit-test)
* [How to run the unit testing code](#how-to-run-the-unit-testing-code)
  
#### Data Visualization 
#### Task 1: The percentage of samples resistant (R) and sensitive (S) to each antibiotic.
To visualize the percentage of R and S a bar chart was used for each column separately. This way we can highlight both categories simultaneously. 
There are 17 types of antibiotics in the dataset, therefore 17 plots were created for each.

#### Task 2: The presence of each resistance gene across the samples.
To visualize the resistance gene across all samples bar chart was used. The presence of resistance is labeled as 1 in the dataset. So in each column, only the value of 1 was 
considered for the plot.
There are 5 genes presented in the dataset so the bar chart contains 5 bars for each. 

#### Task 3: The distribution of cell counts for each organism.
The question asks for a distribution plot. Initially, a boxplot chart was selected to visualize the organism's count. The boxplot can provide information such as distribution max, min, median, etc.
Since there are many zeros in the organism count (e.g. an organism was not observed for that assay), the box plot median skewed toward zero.
In the next attempt, distribution plots (kde) were created for each organism. The plot skewed to zero as I expected.
Finally, distribution plots were produced by filtering zeros. 
Along with this chart, the percentage plot of non-zero items vs zero items would be beneficial. 

#### Unit Test
To add a new record to the dataset a class ```urine_test_add_data.py``` were written. Method ```add_record(self, new_row)``` adds a new row to the dataset.
The data set can be presented to the class through the constructor when it is initialized.
To test the class ```test_cases.py``` was written. This class contains a method that throws an error if the number of elements for the new row is less than or more than rows in 
the dataframe.

* Note1:
  I searched for a better way to check unit test a dataframe. Pandas has built-in APIs ```from urine_test_add_data import UrineTestAddData``` that potentially can be used for this purpose.
  I specifically intended to use this API to check the datatype agreement of the new_row. Unfortunately, the API is not documented well and I could not use different flags provided b the API.
  I have to admit that I learn something new here!
* Note2:
  The type checking of the rows can be implemented easily.

#### How to run the unit testing code
* CD to the dataunittest directory
* On the command line type:<p>
  ```python  testcases.py```

Thanks for your consideration, please let me know if there is any question.



