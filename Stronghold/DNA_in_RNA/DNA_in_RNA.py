# @File     :DNA_in_RNA
# @Date     :06-06-2021
# @Author   :MaiconGavino

def main():
    f = open('.\Stronghold\DNA_in_RNA\input.txt', 'r')
    file = f.readline()
    file = file.replace('T', 'U')
    print(file)

if __name__ == '__main__':
    main()