def Cmn(np,nq,nr):
    if np==0 and nr==0 and nr==0:
        return 0
    elif abs(np-nq)>1 or abs(np-nr)>1 or abs(nq-nr)>1:
        return 0
    lista=[np//3,nq//3,nr//3]
    min3=min(lista)
    count=0
    if abs(np-nq)<=1 or abs(np-nr)<=1 or abs(nq-nr)<=1:
        if (np-3*min3)>=0 and (nq-3*min3)>=0 and (nr-3*min3)>=0:
            count+=6*2
            np=np-3*min3
            nq=nq-3*min3
            nr=nr-3*min3
        while not min3:
            if abs(np-nq)<=1 or abs(np-nr)<=1 or abs(nq-nr)<=1:
                count+=2
    return count
print(Cmn(2,1,1))