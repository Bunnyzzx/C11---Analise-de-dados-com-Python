import matplotlib.pyplot as plt
import seaborn as sns

db_titanic = sns.load_dataset('titanic')
print(db_titanic)

sns.histplot(data=db_titanic, x='age', hue='sex', kde=True)

plt.title('distribuicao de idade por sexo')
plt.xlabel('idade')
plt.ylabel('quantidade')
plt.show()