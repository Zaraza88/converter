import csv, yaml, json

type_to_convert = input('Введите тип конвертации (json или yaml): ')
file_csv = input('Введите полное название файла с указаним расширения: ')

open_file = open(file_csv, "r")

def filling_lists(titles, lines, new_list):
    item = dict(zip(titles, lines))
    new_list.append(item)

def start_script():
    reader_to_file = csv.reader(open_file)
    title_list = open_file.readline()[:-1].split(',')
    new_list = []
    if 'yaml' in type_to_convert:
        write_to_yaml = open('yaml_file.yaml', "w")
        for line in reader_to_file:
            filling_lists(title_list, line, new_list)
        write_to_yaml.write(yaml.dump(new_list, sort_keys=False))
        write_to_yaml.close()
    elif 'json' in type_to_convert:
        write_to_json = open('json_file.json', 'w')
        for line in reader_to_file:
            filling_lists(title_list, line, new_list)
        write_to_json.write(json.dumps(new_list, indent=4))
        write_to_json.close()
    open_file.close()


if __name__ == '__main__':
    start_script()
