from astropy import units as u
import pandas as pd
import matplotlib.pyplot as plt
import pickle

with open('data/h_alpha.pickle', 'rb') as f:
    dc_wave, dc_flux, dc_model = pickle.load(f)
    
df = pd.read_csv('data/h_alpha.csv')

i = 1

fig, ax = plt.subplots()
ax.plot(dc_wave[i].value, dc_model[i].value)
ax.set_xlim(6500, 6630)
plt.show()
