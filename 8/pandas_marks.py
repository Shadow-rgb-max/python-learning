import pandas as pd
import numpy as np
weights = np.array([0.3, 0.3, 0.4])
data = {
    'names': ['juri', 'mraks', 'evans', 'casper', 'juli'],
    'math': [98, 78, 56, 90, 70],
    'physics': [59, 90, 78, 78, 80],
    'chem': [88, 99, 90, 56, 90],
}
df = pd.DataFrame(data)
df['final_marks'] = (df[['math', 'physics', 'chem']] * weights).sum(axis=1)
sorted_df = df.sort_values(by='final_marks', ascending=False)
sorted_df.reset_index(inplace=True, drop=True)
top_students = sorted_df[sorted_df['final_marks'] > 75]
top_students.reset_index(drop=True, inplace=True)
for i, row in top_students.iterrows():
    print(f'{i+1}. {row["names"]}: {row["final_marks"]:.1f}')