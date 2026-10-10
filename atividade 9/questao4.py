import matplotlib.pyplot as plt
import seaborn as sns

db_mpg = sns.load_dataset('mpg')
print(db_mpg)

sns.regplot(data=db_mpg, x='horsepower', y='mpg')
plt.title('Potencia x Consumo')
plt.xlabel('Potencia')
plt.ylabel('Milhas por Galao')
plt.show()
