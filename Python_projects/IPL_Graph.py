import pandas as pd
import matplotlib.pyplot as plt


teams = ['CSK', 'MI', 'DC', 'KKR', 'RR', 'PBKS', 'SRH', 'RCB']
points = [14, 12, 10, 8, 6, 4, 2, 0]


pf = pd.Series(teams, points)


print(pf)
c1 = ['y', 'b', 'c', 'k', 'm', 'r', 'g']
i = 0
for p in points:
    plt.annotate(p, xy=(i,p))
    i = i + 1
plt.bar(teams, points, color=c1)
plt.xlabel('teams')
plt.ylabel('points')
plt.title('IPL 2021 POINTS TABLE')
plt.legend()
plt.show()


