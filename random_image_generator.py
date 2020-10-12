import json
import numpy as np
import random
import requests
from PIL import Image


def create_image(n):
	RED_KEY = "5cb7ca05-e870-42f1-a480-290c1a2826e5"
	BLUE_KEY = "f231735e-3e03-42d5-afdd-0ec0160c6c0c"
	GREEN_KEY = "8145a4e6-45a5-4274-85a8-cbdd5c8d56b0"
	res = np.zeros((n,n), dtype=object)
	KEYS = [RED_KEY, BLUE_KEY, GREEN_KEY]
	colors = [request_values(key, n*n) for key in KEYS]
	for i in range(n):
		for j in range(n):
			res[i][j] = (colors[0][i+j], colors[1][i+j], colors[2][i+j])
		
	img = Image.fromarray(res, mode='RGB')
	img.save('random.png')


def request_values(api_key, n):
	url = 'https://api.random.org/json-rpc/2/invoke'
	text = {
		"jsonrpc": "2.0",
		"method": "generateIntegers",
		"params": {
			"apiKey": api_key,
			"n": n,
			"min": 0,
			"max": 255,
			"replacement": True
		},
		"id": 42
	}
	response = requests.post(url, json=text)
	text = json.loads(response.text)
	return text['result']['random']['data']
		

def main():
    create_image(120)
    #create_image(2)
    #create_image(4)
	
if __name__ == '__main__':
    main()
