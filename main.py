import random
import itertools

# INPUT
def getGenome(length=1000): #create random seq of nt. of given length
    genome = "".join(random.choice('ATCG') for i in range(length))
    return genome

def getSubstrings(seq, length=100):  # returns the list of subsequences of the genome of given length
    L = []
    for i in range(len(seq) - length + 1):
        L.append(seq[i:i + length])
    return L

def permutations(l): #create a list of lists of all possible permutations of the subsequences entered
    comb=[]
    for subset in itertools.permutations(l, len(l)):
        comb.append(list(subset))
    return comb


#OVERLAP
def overlap_or_merge(s1, s2): #if 2 seq overlap they are joined with the overlap otherwise they are simply merged
    over = ''
    for i in range(3,len(s1) + 1):  # at least the first 3 characters must be equal so there is not point in checking below that
        if s1[-i:] != s2[:i]:  # if the suffix of s2 is not the same as the prefix of s1
            pass  # go on looking
        else:  # when subsequence coincide --> overlapping sequence
            over = s2[:i]  # the i-th subsequence is assigned as an overlap
    if over!='':
        l=len(over)
        seq=s1[:-l]+over+s2[l:]
    else:
        seq=s1+s2
    return seq


#BUILD SEQ FROM PERMUTATION
def buildSeq(p): #given a permutation it reconstruct the sequence
    c=p.copy()
    if len(p)==1:
        return p[0]
    else:
        s=overlap_or_merge(p[0],p[1])
        c[0]=s
        c.remove(p[1])
        return buildSeq(c)


def SCS(permutations): #returns the shortest common superstring comparing all joined permutations length
    scs=buildSeq(permutations[0]) #initialize scs
    min_l=len(scs) #initializing the SCS min length
    for p in permutations:
        seq=buildSeq(p)
        if len(seq)<min_l:
            scs=p
            min_l=len(p)
    return scs

#MAIN
if __name__ == '__main__':
    DNA=getGenome(12)
    #print(DNA)
    subseq=getSubstrings(DNA,6)
    #print(subseq)
    p=permutations(subseq)
    #print(p)


    scs=SCS(p)
    print(scs)


