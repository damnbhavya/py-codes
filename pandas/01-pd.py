import numpy as np
import pandas as pd
s = [1,2,3,4,5]
i = ['a','b','c','d','e']
v = pd.Series(s,i)
print(v)
print(v['a'])


cars = {'Tesla': 10, 'BMW': 20, 'Toyota': 30}
v1 = pd.Series(cars)
print(v1)