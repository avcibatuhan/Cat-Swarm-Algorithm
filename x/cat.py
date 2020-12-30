import random
import numpy as np
from enum import Enum

import simulation

#İzleme veya Takip Etme Class
class Behavior(Enum):
    #İzleme
	SEEKING = 1
    #Takip Etme
	TRACING = 2

#Kedi Classı
class Cat:
    #Temel özellikler(davranış,pozisyon,hız,)
	def __init__(self, behavior, position, velocities, vmax):
		self.behavior = behavior
		self._position = position
		self._velocities = velocities
		self._vmax = vmax
		self._dimension_size = len(self._position)

	def evaluate(self, function):
		return function(self._position), self._position

    #İzleme veya Hareket Etme durumuna göre olay fonksiyonu
	def move(self, function, best_pos):
        #Eğer Davranış İzlemeye Eşit İse =>
		if self.behavior == Behavior.SEEKING:
		#------IZLEME------
        #boş bir hareket array i oluşturuyoruz. =>
			candidate_moves = []
            #Hafıza havuzundaki aranan her hedef için
			for j in range(simulation.SMP):
                #Boş array imize arama havuzuna göre ekleme yapıyoruz.
				candidate_moves.append(
					[
						random.uniform(
							self._position[idx_dim] - (self._position[idx_dim] * simulation.SRD) / 100, 
							self._position[idx_dim] + (self._position[idx_dim] * simulation.SRD) / 100
						)
						for idx_dim in range(self._dimension_size)
					]
				)
			
			fitness_values = [function(candidate) for candidate in candidate_moves]

			fit_min = min(fitness_values)
			fit_max = max(fitness_values)

			probabilities = [abs(value - fit_max) / (fit_max - fit_min) for value in fitness_values]
			prob_sum = sum(probabilities)
			probabilities = list(map(lambda prob: (float)(prob / prob_sum), probabilities))

			next_position_idx = np.random.choice(simulation.SMP, 1, p=probabilities)[0]
			self._position = candidate_moves[next_position_idx]
        #Eğer davranış Takip Etmeye Eşit ise
		elif self.behavior == Behavior.TRACING:
			#------TAKIP ETME------
			r1 = random.random()

			for idx_dim in range(self._dimension_size):
				#Hızı hesaplama =>
				self._velocities[idx_dim] = self._velocities[idx_dim] + r1 * simulation.c1 * (best_pos[idx_dim] - self._position[idx_dim])
				#Sınırları Uygulama =>		
				self._velocities[idx_dim] = min(self._velocities[idx_dim], self._vmax)
				self._velocities[idx_dim] = max(self._velocities[idx_dim], -self._vmax)
				#Hesaplanan hız ile hareket etme
				self._position[idx_dim] = self._position[idx_dim] + self._velocities[idx_dim]

			#İZLEME Veya Takip Etme Modunda değilse
		else:
			raise Exception("Unreachable")