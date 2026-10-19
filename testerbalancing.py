'''
Description: Generate all combinations of balanced parentheses for a given number of pairs.
'''



def generate_parentheses(n: int) -> list[str]:
    result=[]

    if n == 0 or n%2!= 0:
        return result

    def generate(curr, open, closed):
        if len(curr)==n:
            result.append(curr)
            return

        if open< n // 2:
            generate(curr + "(" , open+1 , closed)

        if closed<open:
            generate(curr + ")" , open, closed+1)

    
    generate("" ,0 ,0)

    return result


if __name__ == '__main__':
    n = int(input())
    print(generate_parentheses(n))
