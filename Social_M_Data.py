import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import numpy as np
import random
import seaborn as sns
import matplotlib.pyplot as plt
#from IPython.display import display


categories = (['Food', 'Travel', 'Sports', 'Fitness', 'Art', 'Technology', 'Gaming'])
n = 10

data = { 
    'Date': pd.date_range('2024-01-01', periods=n),
    'Category': [random.choice(categories) for i in range(n)],
    'Like': np.random.randint(1, 10000, size=n)
}

df = pd.DataFrame(data)


category_likes = df.groupby('Category')['Like'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Like', data=category_likes)
plt.title('Total Likes by Category')
plt.xlabel('Category')
plt.ylabel('Total Likes')
plt.xticks(rotation=45)
plt.show()
print(df)
