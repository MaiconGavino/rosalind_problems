# @File     :INI4.py
# @Date     :03-06-2021
# @author   :MaiconGavino

def main():
    f = open('.\Village\INI4\input.txt', 'r')
    file = f.readline()
    values = file.split(" ")
    value_A, value_B = map(int, values)
    print(value_A)
    print(value_B)
    sum = 0
    for value_n in range(value_A, value_B+1, 1):
        if(value_n % 2 != 0):
            sum += value_n

    print(sum)


if __name__ == '__main__':
    main()
