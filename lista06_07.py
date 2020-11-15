'''7) Crie um vetor x com 60 pontos linearmente espaçados entre
-2π e 2π e construa o gráfico a baixo. Utilize as bibliotecas
numpy e matplotlib'''

import numpy as np 
import matplotlib.pyplot as plt

plt.subplot(2,2,1)
plt.title('função seno(x)')
x = np.linspace(-2*np.pi, 2*np.pi, 60)
y = np.sin(x)

plt.xlim((-7,7))
plt.ylim((-1,1))
plt.plot(x, y, color="red", linewidth=1)

plt.subplot(2,2,2).fill_betweenx(y, 0, x)
plt.title('função cos(x)')
x = np.linspace(-2*np.pi, 2*np.pi, 60)
y = np.cos(x)

plt.subplot(2,2,3)

plt.title('função tg(x)')
plt.xlabel('valor de x')
plt.ylabel('valot de tg(x)')
x = np.linspace(-2*np.pi, 2*np.pi, 60)
y = np.tan(x)

plt.xlim((-7,7))
plt.ylim((-40,40))
plt.scatter(x,y,linewidth=1)

plt.show()