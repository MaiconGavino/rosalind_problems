# @File     :Complementing_of_DNA.py
# @Date     :06-06-2021
# @Author   :MaiconGavino

def main():
    f = open('.\Stronghold\Cadeia_DNA\input.txt').readline()
    nucleotideo = 'ATCG'
    complemento = 'TAGC'
    transicao = str.maketrans(nucleotideo, complemento)
    dna_reverse = f.translate(transicao)[::-1].lstrip()
    print(dna_reverse)


if __name__ == '__main__':
    main()
