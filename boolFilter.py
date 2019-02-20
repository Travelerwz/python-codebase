import mmh3
from bitarray import bitarray

class BloomFilter():
	def __init__(self):
		self.capacity = 1000
		self.bit_array = bitarray(capacity)
		self.bit_array.setall(0)
	
	def get_postions(self,element):
		postion_list = []
		for i in range(41,49):
			index = mmh3.hash(element,i) % self.capacity
			postion_list.append(index)
		return postion_list
		
	def add(self,elemnt):
		post_list = self.get_postions(element)
		
		for i in post_list:
			self.bit_array[i] = 1
			
	def contains(self,element):
		post_list = self.get_postions(element)
		
		result = True
		for i in post_list:
			result = self.bit_array[i] and result
			
		return result

if __name__=='__main__':
	bloom = BloomFilter()
	a = ['123','456','568']
	for i in a:
		bloom.add(i)
	b = ['123','756','963']
	for i in b:
		if bloom.contains(i):
			print("%s exist"%i)
		else: 
			print("%s not exist"%i)
