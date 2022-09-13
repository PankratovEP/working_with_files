import os


def reverse_sequence():
    with open('vvod.txt', encoding='utf-8') as inpt, open('vivod.txt', 'w', encoding='utf=8') as otpt:
        stroki = list(map(lambda x: (x + '\n') if not x.endswith('\n') else x, inpt.readlines()))[::-1]
        otpt.writelines(stroki)


def poisk_po_arhivu():
    with open('dirs.txt', 'w', encoding='utf-8') as outpt:
        lines = []
        for i in os.walk('main'):
            for j in i[2]:
                if j.endswith('py'):
                    lines.append(i[0])
                    break
        for i in lines:
            print(i, file=outpt)
