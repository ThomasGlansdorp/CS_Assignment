import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("istherecorrelation.csv", delimter = ";")

plt.figure(dpi=300)
plt.plot(data["Year"], data["WO [x1000]"])
plt.xlabel('Year')
plt.ylabel('WO [x1000]')
plt.title('WO from 2006 to 2018')
plt.show()

plt.figure(dpi=300)
plt.plot(data["Year"], data["NL Beer consumption [x1000 hectoliter]"])
plt.xlabel('Year')
plt.ylabel('NL Beer consumption [x1000 hectoliter]')
plt.title('NL Beer consumption from 2006 to 2018')
plt.show()
