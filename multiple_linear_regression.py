# Multiple Linear Regression, Coefficient of Determination, and Residual Variance

from numpy import array, linalg, dot

valores_x1 = [1.82, 1.80, 1.79, 1.87, 1.89, 1.94, 1.95, 1.93, 2.00]
valores_x2 = [74, 88, 94, 78, 84, 98, 76, 86, 96]
valores_y = [1.92, 2.11, 2.15, 2.02, 2.09, 2.31, 2.02, 2.16, 2.31]

x1x2 = []
x22 = []
x12 = []
x1y = []
x2y = []
y2 = []

for i in range(len(valores_x1)):
    x1x2.append(valores_x1[i] * valores_x2[i])
    x2y.append(valores_x2[i] * valores_y[i])
    x1y.append(valores_x1[i] * valores_y[i])
    x12.append(valores_x1[i] ** 2)
    x22.append(valores_x2[i] ** 2)
    y2.append(valores_y[i] ** 2)

A = linalg.inv(array([[len(valores_x2), sum(valores_x1), sum(valores_x2)], [sum(valores_x1), sum(x12), sum(x1x2)], [sum(valores_x2), sum(x1x2), sum(x22)]]))
Y = array([[sum(valores_y)], [sum(x1y)], [sum(x2y)]])

X = dot(A, Y)
Equacao = f'({str(X[2]).replace("[", "").replace("]", "")})w + ({str(X[1]).replace("[", "").replace("]", "")})h + ({str(X[0]).replace("[", "").replace("]", "")})'
print('Y(h, w) = ', Equacao)

U = []
for i in range(len(valores_x1)):
    U.append((valores_y[i] - eval(Equacao.replace('w', f'* {valores_x2[i]}').replace('h', f'* {valores_x1[i]}'))) ** 2)

print('Y(1.9, 82) = ', eval(Equacao.replace('w', '* 82').replace('h', '* 1.9')))
print('SIGMA^2 = ', sum(U)/(len(valores_y) - 3))
print('R^2 = ', 1 - (sum(U)/(sum(y2) - (sum(valores_y)**2)/len(valores_x1))))
