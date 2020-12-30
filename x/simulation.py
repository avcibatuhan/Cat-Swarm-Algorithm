import numpy as np
import pandas as pd
import sys

import cost_functions
import cso

#Alltaki değerleri cso.py da çağırıyoruz.
NUM_RUNS = 30
NUM_CATS = 50
MR = 2 #yüzdelik-iki davranış modu arasındaki
SMP = 5 #aranan hafıza havuzu /kopyaliyoruz
SRD = 20 #yüzdelik - seçilen boyutun aralığını aramak
c1 = 2 #sabit deger
num_dimensions = 2
v_max = 1

def run_experiment(function_name, num_iteration):
    #fonksiyonları aldığı kısım =>
	function = getattr(cost_functions, f"{function_name}_fn")
    #sonucları ve sonuc pozisyonlarını yazacagımız bos diziler =>
	results = []
	results_pos = []
    #ortalamayı yazacagımız degısken =>
	avg = 0
#cso.py daki run fonksiyonuna gönderiyoruz =>
	for _ in range(NUM_RUNS):
		best, best_pos = cso.CSO.run(
			num_iteration, 
			function, 
			num_cats=NUM_CATS, 
			MR=MR, 
			num_dimensions=num_dimensions, 
			v_max=v_max
		)
        #sonuç pozisyonu dizisine best positionu ekliyoruz
		results_pos.append(best_pos)
        #sonuc dizisine en iyi skoru ekliyoruz =>
		results.append(best)
	
	best_all = min(results)
	best_all_pos = results_pos[results.index(best_all)]

	return best_all, best_all_pos, (sum(results) / len(results))


def main():
    #Test Fonksiyonlarımız
	functions = [
		"beale",
        "ackley",
        "goldstein",
        "levi",
	]
    
    #İterasyon sayıları
	max_iterations = [50, 100, 500]

	all_results = []
    #Her bir fonksiyonu döndüren döngü
	for function in functions:
        #Her bir iterasyonu döndüren döngü
		for num_iteration in max_iterations:
			best, best_pos, avg = run_experiment(function, num_iteration)
			print(f"Function={function}, Iterations={num_iteration} | best={format(best, '.10f')}, best_pos={best_pos}, avg={format(avg, '.10f')}")
            #elde ettiğimiz tüm sonuçları başka diziye ekliyoruz
			all_results.append([
				function,
				num_iteration,
				best,
				best_pos,
				avg
			])
	#pandas ve numpy kütüphaneleri kullanarak yazdırma işlemleri =>
	data = np.array(all_results)
	dataset = pd.DataFrame({
		"function": data[:, 0],
		"iterations": data[:, 1],
		"best score": data[:, 2],
		"best position": data[:, 3],
		"avg": data[:, 4]
	})

	dataset.to_excel("results.xlsx")
	print(dataset)

if __name__ == "__main__":
	main()