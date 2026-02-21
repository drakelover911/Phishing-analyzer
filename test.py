with open("spam.txt", "r") as f:
    keywords = f.read()

print(keywords.splitlines())
for object in keywords.lower().splitlines():
    print(object)

string ="zero chance zero risk you have been chosen you are winner!"
points = 0
for object in keywords.lower().splitlines():
    if object in string:
        points +=1
print(points)