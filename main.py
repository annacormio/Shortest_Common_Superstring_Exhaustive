import random
import itertools

# INPUT
def getGenome(length=1000):
    genome = "".join(random.choice('ATCG') for i in range(length))
    return genome

def getSubstrings(seq, length=100):  # returns the list of subsequences of the genome of given length
    L = []
    for i in range(len(seq) - length + 1):
        L.append(seq[i:i + length])
    return L

def permutations(l): #create a list of lists of all possible permutations of the subsequences
    comb=[]
    for subset in itertools.permutations(l, len(l)):
        comb.append(list(subset))
    return comb
#OVERLAP
def overlap(s1, s2):
    over = ''
    for i in range(3,len(s1) + 1):  # at least the first 3 characters must be equal so there is not point in checking below that
        if s1[-i:] != s2[:i]:  # if the suffix of s2 is not the same as the prefix of s1
            pass  # go on looking
        else:  # when subsequence coincide --> overlapping sequence
            over = s2[:i]  # the i-th subsequence is assigned as an overlap
    return over








if __name__ == '__main__':
    DNA=getGenome(6)
    print(DNA)
    subseq=getSubstrings(DNA,3)
    print(subseq)
    p=permutations(subseq)
    print(p)
