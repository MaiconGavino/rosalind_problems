# @File     : INI1.py
# @Date     : 03-06-2021
# @Author   : MaiconGavino

def main():
    f = open('.\INI2\rosalind_ini2.txt','r')
    file = f.readline()
    ent1, ent2 = file.split(" ")
    print(pow(int(ent1),2) + pow(int(ent2),2))

if __name__ == '__main__':
   main()
