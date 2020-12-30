import math

#Beale Test Fonksiyonu
def beale_fn(x):
	return (1.5 - x[0] + x[0]*x[1])**2 + (2.25 - x[0] + x[0]*x[1]**2)**2 + (2.625 - x[0] + x[0]*x[1]**3)**2

#Ackley Test Fonkisyonu
def ackley_fn(x):
    return -math.exp(-math.sqrt(0.5 * sum([i ** 2 for i in x]))) - math.exp(0.5 * sum([math.cos(i) for i in x])) + 1 + math.exp(1)

#Goldstein Test Fonksiyonu
def goldstein_fn(x):
    return ((1 + (x[0] + x[1] + 1) ** 2 * (19 - 14 * x[0] + 3 * (x[0] ** 2) - 14 * x[1] + 6 * x[0] * x[1] + 3 * (x[1] ** 2))) * (30 + (2 * x[0] - 3 * x[1]) ** 2 * (18 - 32 * x[0] + 12 * (x[0] ** 2) + 48 * x[1] - 36 * x[0] * x[1] + 27 * (x[1] ** 2))))

#Levi Test Fonksiyonu
def levi_fn(x):
    return (math.sin(3*x[0]*math.pi))**2 + ((x[0] - 1)**2)*(1 + math.sin(3*x[1]*math.pi)**2) + ((x[1] - 1)**2)*(1 + math.sin(2*x[1]*math.pi)**2)