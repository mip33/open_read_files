from pprint import pprint
def dict_reciept():
    with open('reciepts.txt', 'r', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            name = line.strip()
            total = int(file.readline().strip())
            lines = []
            for item in range(total):
                data = file.readline().strip().split(' | ')
                lines.append({'ingredient_name': data[0],
                              'quantity': int(data[1]),
                              'measure': data[2]})
            cook_book[name] = lines
            file.readline()
        return cook_book



def get_shop_list_by_dishes(dishes, person_count):
    a = set(dishes)
    result = {}
    for keys,values in dict_reciept().items():
        if keys in a:
            for i in values:
                i['quantity'] = i['quantity'] * person_count
                result[i['ingredient_name']] = {'measure': i['measure'], 'quantity': i['quantity']}
    return result
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


def add_file(names):
    my_list = []
    for i in names:
        with open(i, encoding='utf8') as file:
            my_list.append((i,len(file.readlines())))
    my_list.sort(key=lambda x: x[1])
    with open('result.txt', 'w+') as write_file:
        for original_file, rows_count in my_list:
            with open(original_file) as read_file:
                write_file.writelines(read_file.readlines())


add_file(['1.txt','2.txt','3.txt'])
