"""
DNA
"""


def longest_subsequence(string_1, string_2):
    """ADD YOUR CODE HERE """
    string_1=string_1.upper()
    string_2=string_2.upper()

    longest=0
    subseq=[]

    for i in range(len(string_1)):
        for j in range(len(string_2)):
            m=0
            empty=""
            while i+m<len(string_1) and j+m<len(string_2):
                if string_1[i+m]==string_2[j+m]:
                    empty+=string_1[i+m]
                    m+=1
                else:
                    break

            if len(empty)>longest:
                longest=len(empty)
                subseq=[empty]
            elif len(empty)==longest and empty not in subseq:
                subseq.append(empty)
                subseq=sorted(set(subseq))

    #filter
    if longest<2:
        return []
        

    return subseq






def main():
    """
    This main function reads the data input files and
    prints to the standard output. 
    NO NEED TO CHANGE THE MAIN FUNCTION.
    """

    # read the data
    # number of lines
    n_lines = int(input())

    # for each pair
    for _ in range(0, n_lines):
        str_1 = input()
        str_2 = input()

        # call longest_subsequence
        subsequences = longest_subsequence(str_1, str_2)

        # write out result(s)
        if not subsequences:
            print("No Common Sequence Found")

        for subsequence in subsequences:
            print(f"{subsequence}")

        # insert blank line
        print()


if __name__ == "__main__":
    main()
