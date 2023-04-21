
def chess(n):
    print("Can 2x1 dominoes fill this chessboard?")
    s = ""
    for i in range(n): #creates row of chessboard with n values
        if i % 2 == 0:
            s += "|#"
        else:
            s += "|_"
        if i == (n-1):
            s += "|"

    for j in range(n): #prints rows of chessboard n times
        if j % 2 == 0:
            print(s)
        else:
            print(s[::-1])
        
    numhash = s.count("#")*n
    numempty = s.count("_")*n
    print("Number of hashtags: %i" % numhash)
    print("Number of empty spaces: %i" % numempty)
    
    print(input("Remove opposing corners(#,_): "))
"""
    if numhash != numempty:
        print("Cannot fill this chessboard fully with 2x1 dominoes, remainder is not zero.")
    else:
        print("Board may be filled with 2x1 dominoes fully through parity.")
        print("Number of hashtags is equal to the number of empty spaces.")
"""    
chess(8)
