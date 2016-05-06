class SortSolution(object):
    def __init__(self,seq):
        self.seq = seq

    def Bubble(self):
        for i in range(len(self.seq))[::-1]:
            for j in range(i):
                if self.seq[j] > self.seq[j+1]:
                    self.seq[j],self.seq[j+1] = self.seq[j+1],self.seq[j]

    def SelectSort(self):
        for i in range(len(self.seq)):
            min = i
            for j in range(i+1,len(self.seq)):
                if self.seq[min] > self.seq[j]:
                    self.seq[min], self.seq[j] = self.seq[j], self.seq[min]

def QuickSort(seq):
    if len(seq) <= 1:
        return seq
    return QuickSort([left for left in seq[1:] if left <= seq[0]]) + [seq[0]] + QuickSort(
        [right for right in seq[1:] if right > seq[0]])


def insertSort(seq,n):
    if n == 0:
        return
    insertSort(seq,n-1)
    j = n
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1],seq[j] = seq[j],seq[j-1]
        j = j-1



if __name__ == '__main__':
    seq = [2,8,5,3,1]
    insertSort(seq,4)
    print(seq)
    Sort = SortSolution(seq)
    Sort.SelectSort()
    print(Sort.seq)
    #Sort.Bubble()
    #print(Sort.seq)

    #QuickSort(seq)
    #print(QuickSort(seq))
