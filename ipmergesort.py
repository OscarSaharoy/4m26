
def ipmergesort( A ):

    mergesort( A, 0, len(A) )

    return A

def mergesort( A, low, high ):

    if high - low <= 1:
        return

    pivot = ( low + high ) // 2

    mergesort( A, low, pivot )
    mergesort( A, pivot, high )
    merge( A, low, pivot, high )


def swap( A, i, j ):
    A[i], A[j] = A[j], A[i]

def merge( A, low, pivot, high ):

    il = 0
    ih = pivot

    while il < pivot or ih < high:
        if il < pivot and A[il] < A[ih]:
            il += 1
        
