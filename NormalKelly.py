y.sort()
y = np.array(y) / 100
# print(y)
plt.hist(y, bins= 20)
print('mean, var = ', np.mean(y), np.std(y))

def NormalPdf(x, mean, std):
    return 1 / (std * (2* np.pi)**0.5) * np.exp(-1/2 * ((x-mean)/ std) ** 2)
def DiscreteNormal(mean, std, radius , size):
    x = np.linspace(mean - radius, mean + radius, size)
    px = NormalPdf(x, mean, std)
    return x, px
mean, std = np.abs(np.mean(y)), np.std(y)
radius = 0.07 - np.abs(mean)
size = 100
x, px = DiscreteNormal(mean, std, radius , size)
# print(x)
# print(px)
print('mean, std', mean, std)

# print(x)
def logR(f, x, px):
    return np.sum(px* np.log(1+ f* x))
logR(10, x, px )


f = np.linspace(0.1, 12, 10)
returns = [logR(ele, x, px ) for ele in f]
plt.plot(f, returns)
plt.show()

print(f)
# print(logR(f, x, px ))
returns = [logR(ele, x, px ) for ele in f]
print(returns)
plt.plot(f, returns)


def BTK(f):
    return - logR(f , x, px )
res = minimize(BTK, [7], method='nelder-mead')
print(res.x)
