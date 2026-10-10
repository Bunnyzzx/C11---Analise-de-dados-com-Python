import matplotlib.pyplot as plt
import seaborn as sns

db_titanic = sns.load_dataset('titanic')
print(db_titanic)

sns.boxplot(data=db_titanic, x='age',y='class', hue='sex')

plt.title('distribuicao de idade por classe e sexo')
plt.xlabel('classe')
plt.ylabel('idade')
plt.show()