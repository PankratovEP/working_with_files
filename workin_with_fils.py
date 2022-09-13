with open('vvod.txt', encoding='utf-8') as inpt, open('vivod.txt', 'w', encoding='utf=8') as otpt:
    stroki = list(map(lambda x: (x +'\n') if not x.endswith('\n') else x, inpt.readlines()))[::-1]
    otpt.writelines(stroki)