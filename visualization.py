import pandas as pd
import numpy
import matplotlib.pyplot as plt

salarios = pd.read_csv('tabela_salarios.csv')

remLiq_df = pd.DataFrame({"remLiq":salarios["remLiq"], "id":salarios["id"]})
rl = remLiq_df.groupby("id").aggregate(numpy.mean)
print(rl)
rl = rl.sort_values("remLiq", ascending = False)

plt.bar(range(rl.shape[0]), rl["remLiq"])
plt.show()