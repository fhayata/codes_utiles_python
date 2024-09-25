# Dans l'ordre d'apparition dans la phrase
def get_min_max_words(sentence):
    min_word = ""
    max_word = ""
    p = sentence.split(" ")
    min_word = min(p, key=len)
    max_word = max(p, key=len)
    return (min_word, max_word)

# Tenant compte de l'ordre alphabétique
def get_min_max_words2(sentence):
    p = sentence.split(" ")
    p.sort()
    min_word = min(p, key=len)
    max_word = max(p, key=len)
    return (min_word, max_word)

min, max = get_min_max_words("Voci une phrase totalement inutile")
# print(f"Le mot le plus court est ***"+min+ "*** et le mot le plus long est ***"+max)

min, max = get_min_max_words2("Voci une phrase totalement inutile")