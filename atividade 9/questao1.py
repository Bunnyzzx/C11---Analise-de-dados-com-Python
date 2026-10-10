import matplotlib.pyplot as plt
import seaborn as sns

db_iris = sns.load_dataset('iris')

setosa = db_iris[db_iris['species'] == 'setosa']

correlacao = setosa.select_dtypes(include='number').corr()

sns.heatmap(correlacao, annot=True, cmap='coolwarm')

plt.title('Correlacao - Iris Setosa')
plt.show()