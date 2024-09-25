file = open("fichier.txt", "w")
for i in range(1, 11):
    file.write(f"{i}\n")
file.close()