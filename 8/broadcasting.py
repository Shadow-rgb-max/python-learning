import numpy as np

marks = np.array([[98, 59, 88],
                  [78, 90, 99],
                  [56, 78, 90],
                  [90, 78, 56],
                  [70, 80, 90]])
students = {'juri': 0, 'mraks': 1, 'evans': 2, 'casper': 3, 'juli': 4}
inverse_students = {k: v for v, k in students.items()}
weights = np.array([0.3, 0.3, 0.4])
weighted_marks = marks * weights
final_marks = np.sum(weighted_marks, axis=1)
best_mark = np.argmax(final_marks)
sorted_marks = np.argsort(final_marks, 
                         kind='stable')[::-1]
print(f'лучший студент: {inverse_students[best_mark]}')
print('топ студентов:')
for number, index in enumerate(sorted_marks):
    print(f'{number + 1}. {inverse_students[index]}')