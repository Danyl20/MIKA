import random
dogs = ["mika", "moli", "berta", "uga", "bona"]
cats = ["mota", "vara"]
random.shuffle(dogs)
random.shuffle(cats)
range(20)
for item in  range(2):
    print(str(item + 1)+". "+dogs[item]+ " play with " + (cats[item]) + ".")
