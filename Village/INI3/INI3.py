# @File     : INI1.py
# @Date     : 03-06-2021
# @Author   : MaiconGavino


def main():
    f = open('.\Village\INI3\input.txt', 'r')
    line_Str, line_Value = f.readlines()
    values = line_Value.split(" ")
    entA, entB, entC, entD = map(int, values)
    print(line_Str[entA:entB+1], line_Str[entC: entD+1])

if __name__ == '__main__':
   main()
