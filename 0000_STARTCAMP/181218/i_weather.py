from darksky import forecast 

multicampus = forecast('44671c4f0f3b09f0d9e7d43025d8341a', 37.501588, 127.039713)

print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])