# 13.5


def intersect(array1, array2):
    result = []
    idx1 = 0
    idx2 = 0
    len1 = len(array1)
    len2 = len(array2)
    while idx1 < len1 and idx2 < len2:
        if array1[idx1] == array2[idx2]:
            result.append(array1[idx1])
            while idx2 < len2 and array1[idx1] == array2[idx2]:
                idx2 += 1
        elif array1[idx1] < array2[idx2]:
            idx1 += 1
        else:
            idx2 += 1
    return result


def test():
    n = 10
    m = 4
    array1 = [item for item in range(0, n)]
    array2 = [item for item in range(n-m, n)]

    print "Array1:"
    print array1
    print "Array2:"
    print array2
    result = intersect(array1, array2)
    print "Result"
    print result