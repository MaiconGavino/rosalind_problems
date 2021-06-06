# @File     :INI6.py
# @Date     :05-06-2021
# @author   :MaiconGavino


def main():
    file = [line.strip("\n") for line in open(".\Village\INI6\input.txt", "r")]
    value = file[0].split(" ")
    result = {}
    for i in value:
        if i in value:
            result[i] = 1 + result.get(i, 0)
    for i in result:
        print(i, result[i])



if __name__ == '__main__':
    main()