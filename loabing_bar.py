from tqdm import tqdm
import time
print("new software installing ")
print("please wait... ")
for i in tqdm(range(100)):
	time.sleep(0.1)
print("loading successful")