import yaml
import json

yaml_path1 = r"/Users/robert/Desktop/DataProjects/PyJsonYaml/verify.yaml"
yaml_path2 = r"/Users/robert/Desktop/DataProjects/PyJsonYaml/xmas.yaml"

def json_converter(filepath):
    with open(filepath) as file:
        with open ("output.json", 'w') as new_file:
            yaml_data = yaml.safe_load(file.read())
            convert_json = json.dumps(yaml_data)

            new_file.write((convert_json))

# json_converter(yaml_path1)
json_converter(yaml_path2)