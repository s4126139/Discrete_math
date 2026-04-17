def factorial(k):
    if k == 0: return 1
    fact = 1
    for i in range(1,k+1):
        fact*= i
    return fact

def combination(n,k):
    return factorial(n)/((factorial(n-k)*factorial(k)))
print(combination(10,0))
#Problem. What is the expectation of the number of heads if we toss a coin ten times?
def expectation(ntoss):
    E = 0
    for i in range(ntoss+1):
        E+= i*combination(ntoss,i)/(2**ntoss)
    return E

print(expectation(10))


