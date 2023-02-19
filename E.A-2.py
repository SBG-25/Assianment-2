########## Problem-1
def lastdigit(n):
    return n[-1]
def listtosort(tuples):
  return sorted(tuples, key=lastdigit)
print(listtosort([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

########## Problem-2
alpha_value = {}
for i in range(97, 97 + 26):
    alpha_value[chr(i)] = i
print(alpha_value)