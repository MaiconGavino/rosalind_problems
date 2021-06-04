# @File     :INI5.py
# @Date     :03-06-2021
# @Author   :MaiconGavino

def numbered_line(file):
    return [line for (i, line) in enumerate(file) if i % 2 == 1]

def main():
    f = open('.\Village\INI5\input.txt', 'r')
    file = f.readlines()
    count = numbered_line(file)
    print(count)
    with open('result.out', 'w') as g:
        for n in count:
            g.write(n)

if __name__ == '__main__':
    main()