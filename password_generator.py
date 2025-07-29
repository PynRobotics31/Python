import random
sample = "1234567890"
length = int(input("Enter the length for password : "))
for i in range(10):
	num = "".join(random.sample(sample,length))
	print(num)