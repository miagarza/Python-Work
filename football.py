
def football(n):

    #basically creating the matrix/spiral
    spiral = [[0 for i in range(n)] for i in range(n)]
    maxval=n*n
    print(maxval)

#     #mapping it out
    spiral[0][n-1]=maxval
    row=0
    col=n-1

    #counters
    #maxturns=(n*2)-2
    
    movement=n-1

#     #spiral[row][col-1]=maxval-1
#     #print(spiral)

    while movement > 0:

#         # LEFT
        for i in range(movement):
            col -= 1
            maxval -= 1
            spiral[row][col] = maxval

#         # DOWN
        for i in range(movement):
            row += 1
            maxval -= 1
            spiral[row][col] = maxval

#         # RIGHT
#         for i in range(movement):
#             col += 1
#             maxval -= 1
#             spiral[row][col] = maxval

#         # UP
#         for i in range(movement - 1):
#             row -= 1
#             maxval -= 1
#             spiral[row][col] = maxval

#         row+=2
#         col-=2
#         movement -= 2
#         #turns+=1
#     print(spiral)

    
# football(11)






def football(n):

    #basically creating the matrix/spiral
    spiral = [[0 for i in range(n)] for i in range(n)]
    maxval=n*n
    print(maxval)

    #mapping it out
    toprow=0
    bottomrow=n-1

    left=0
    right=n-1

    while toprow<=bottomrow and left<=right:

        # LEFT
        for i in range(movement):
            col -= 1
            maxval -= 1
            spiral[row][col] = maxval

        # DOWN
        for i in range(movement):
            row += 1
            maxval -= 1
            spiral[row][col] = maxval

        # RIGHT
        for i in range(movement):
            col += 1
            maxval -= 1
            spiral[row][col] = maxval

        # UP
        for i in range(movement - 1):
            row -= 1
            maxval -= 1
            spiral[row][col] = maxval

        row+=2
        col-=2
        movement -= 2
        #turns+=1
    print(spiral)

    
football(11)
