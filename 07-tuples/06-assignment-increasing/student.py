def increasing(ns):
    if ns == ():
        return True
    else:
        for i in range(len(ns)):
            for j in range(len(ns)):
                if j > i:
                    if ns[i] > ns[j]:
                        return False
        return True

                
# ns = (3,2,4,9)
# print(increasing(ns))