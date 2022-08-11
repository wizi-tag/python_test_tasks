import pandas as pd
import os.path

"""
I would put the variables in the config
or pass the file name through sys.argv,
but the script is small and we can leave it here
"""
filename = 'data.csv'
target = 10

"""
What if we have not .csv file in data.tgz?
"""
if not os.path.exists(filename):
    print("[ERROR]\tFile not exists")
else:
    """
    Idk why pandas is used here
    if the data.csv format is the same as in example
    I would use split

    ```
        with open("filename","r") as file:
            str = file.readline()
            sum = sum(str.split(','))
    ```

    """
    # Change name of variable and add ".values" to get values initially
    csv_values = pd.read_csv(filename, sep=",", header=None).values

    """
    If there are strings in data.csv or something like that,
    then an exception will be thrown
    """
    try:
        print(csv_values.sum() == target)
    except TypeError as err:
        print("[ERROR]\tInvalid data in "+filename)
        exit()

"""
Also I think it would be better to pack this into a function
So that this code can be included as a module in other places
"""
