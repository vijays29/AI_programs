def columns(array):return zip(*array)
def magic_square(m):
    n=len(m)
    row_sums={sum(row) for row in m}
    col_sums={sum(col) for col in columns(m)}
    diagonal_sums={
        sum([m[i][i] for i in range(n)]),
        sum([m[i][-i-1] for i in range(n)])
    }
    sums=row_sums|col_sums|diagonal_sums
    return len(sums)==1
if __name__=="__main__":
    square1=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    square2=[
        [2,7,6],
        [9,5,1],
        [4,3,8]
    ]
    print(magic_square(square1))
    print(magic_square(square2))    