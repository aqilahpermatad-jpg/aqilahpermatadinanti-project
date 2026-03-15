
#contoh penerapan library python
import requests 

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.text)

#library math 
import math

print(math.sqrt(20))
print(math.pi)






