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
    for p in itertools.permutations(l, len(l)):
        comb.append(list(p)) #append the permutation to a list in list format
    return comb


#OVERLAP
def overlap_or_merge(s1, s2): #if 2 seq overlap they are joined with the overlap otherwise they are simply merged
    over = ''
    for i in range(min(len(s1),len(s2)) + 1):
        if s1[-i:] != s2[:i]:  # if the suffix of s2 is not the same as the prefix of s1
            pass  # go on looking
        else:  # when subsequence coincide --> overlapping sequence
            over = s2[:i]  # the i-th subsequence is assigned as an overlap
    if over!='': #overlap sequence exist
        l=len(over)
        seq=s1[:-l]+over+s2[l:] #joimed overlapped sequence
    else: #if no overlap exist
        seq=s1+s2 #just merge the 2 sequences
    return seq


#BUILD SEQ FROM PERMUTATION
def buildSeq(p): #given a permutation it reconstruct the sequence
    c=p.copy()
    if len(p)==1: #base case: only one seq left in the list --> seq obtained from that permutation joinings
        return p[0]
    else:
        s=overlap_or_merge(p[0],p[1]) #overlap or merge the first 2 sequences in the list
        c[0]=s #the obtaied seq is replaced in first position
        c.remove(p[1]) #second seq is removed
        return buildSeq(c) #recursive call


def SCS(permutations): #returns the shortest common superstring comparing all joined permutations length
    scs=buildSeq(permutations[0]) #initialize scs
    min_l=len(scs) #initializing the SCS min length
    for p in permutations: #for each permutation of superstring
        seq=buildSeq(p) #assemble the subseq in the permutation by overlap or merge
        if len(seq)<min_l: #if its len is less than the shortes common superstring length
            scs=seq #it becomes the shortes common superstirng
            min_l=len(seq)
    return scs

#MAIN
if __name__ == '__main__':
    DNA=getGenome(11)
    print(DNA)
    subseq=getSubstrings(DNA,6)
    #subseq=['ATCGGA','TACCCA','AGCTAC','CGGATT','TTGCTA']
    print(subseq)
    p=permutations(subseq)
    #print(p)
    scs=SCS(p)
    print(scs)
#exhaustive search takes much more time

