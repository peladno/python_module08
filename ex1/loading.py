import pandas as pd
import numpy as np

arr = np.random.randn(5, 3)
df = pd.DataFrame(arr, columns=["A", "B", "C"])
print(df)
print("pandas version:", pd.__version__)
