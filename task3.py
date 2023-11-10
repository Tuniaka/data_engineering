import json
import msgpack

def aggregate_information(path):
	with open(path) as file:
			data = json.load(file)

	product = {}

	for item in data:
		if item['name'] in product:
			product[item['name']].append(item['price'])
		else:
			product[item['name']] = []
			product[item['name']].append(item['price'])
		
	result = {}

	for name, price in product.items():
		res = {
			"average": sum(price) / len(price),
			"maxinum": max(price),
			"mininmim": min(price)
		}
		result[name] = res

	with open("result/task3/result.json", "w") as f:
		f.write(json.dumps(result))

	with open("result/task3/result.msgpack", "wb") as f:
		f.write(msgpack.dumps(result))


if __name__ == "__main__":
	aggregate_information("data/products_75.json")
	