import pandas as pd

from statsmodels.formula.api import MNLogit
from statsmodels.tools.tools import add_constant

hie = pd.read_csv('/home/1-longitudinal-minimal-data-set-V2.csv', na_values='nd')
hie = add_constant(hie)

y = hie.outcome

x_copeptin = hie.loc[:,['const','copeptin_6h_pmol_l', 'copeptin_12h_pmol_l', 'copeptin_24h_pmol_l']]
model_copeptin = MNLogit(y, x_copeptin, missing='drop').fit()
print(model_copeptin.summary())

x_NSE = hie.loc[:,['const','NSE_6h_ng_ml', 'NSE_12h_ng_ml', 'NSE_24h_ng_ml']]
model_NSE = MNLogit(y, x_NSE, missing='drop').fit()
print(model_NSE.summary())