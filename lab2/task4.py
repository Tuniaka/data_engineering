import json
import pickle

def load_data(path):
	result = {}
	with open(path, 'rb') as f:
		data = pickle.load(f)

	for item in data:
		result[item['name']] = item['price']

	with open('lab2/data/price_info_75.json', 'rb') as f:
		json_data = json.load(f)

	for item in json_data:
		if item['method'] == 'sum':
			result[item['name']] += item['param']
		elif item['method'] == 'sub':
			result[item['name']] -= item['param']
		elif item['method'] == 'percent+':
			val = result[item['name']]
			val += (val * item['param'] / 100)
			result[item['name']] = val
		elif item['method'] == 'percent-':
			val = result[item['name']]
			val -= (val * item['param'] / 100)
			result[item['name']] = val

	with open('lab2/result/task4/result.pkl', 'wb') as f:
		pickle.dump(result, f)


if __name__ == '__main__':
	load_data('lab2/data/products_75.pkl')