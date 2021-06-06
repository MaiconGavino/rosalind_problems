# @file     :DNA_Counting.py
# @Date     :05-06-2021
# @Author   :MaiconGavino

def main():
    f = open('.\stronghold\DNA_Counting\input.txt', 'r')
    file = f.readline()
    file = sorted(file)
    dna = {}
    for value in file:
        if value in file:
            dna[value] = 1 + dna.get(value, 0)

    for value in dna:
        #print(value, dna[value])
        print(dna[value], sep=" ", end=" ")
    
if __name__ == '__main__':
    main()