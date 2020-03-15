import os
import tempfile
import argparse
import json

def work(key=None, value=None):

	storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
	
	if os.path.exists(storage_path):
		with open(storage_path, "r") as f:
			json_data = json.load(f)
	else:
		with open(storage_path, "w") as f:
			json_data = {"keys":[], "values":{}}
			json.dump(json_data, f)

	if value is None:
		values = json_data['values'].get(key, [])
		print("{}". format(", ".join([str(val) for val in values])))
		return

	if key in json_data['keys']:
		values_list = json_data['values'][key]
		values_list.append(value)
		json_data['values'][key] = values_list
	else:
		keys_list = json_data['keys']
		keys_list.append(key)
		json_data['keys'] = keys_list
		json_data['values'].update({key:[value]})
	
	with open(storage_path, "w") as f:
		json.dump(json_data, f)


def main():
	
	parser = argparse.ArgumentParser()
	parser.add_argument("--key", type = str, help ="parameters - key, type - str")
	parser.add_argument("--value", type = str, help ="parameters - value, type - str")
	
	args= parser.parse_args()
	if args.key is None:
		print("Sorry, key is not found")
		return
	_key = str(args.key)
	_value = args.value
	work(_key, _value)


if __name__ == '__main__':
	main()