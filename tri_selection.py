import random
def tri_selection(l):
    for non_trie in range(0, len(l)-1):
        min = l[non_trie]
        min_index = non_trie
        for i in range(non_trie+1, len(l)):
            if l[i] < min:
                min = l[i]
                min_index = i
        l[min_index] = l[non_trie]
        l[non_trie] = min
    return l

def generate_table(n, min, max):
    l = []
    for i in range(0, n):
        l.append(random.randint(min, max))
    return l


t = generate_table(10, 1, 10)
print(t)
print(tri_selection(t))