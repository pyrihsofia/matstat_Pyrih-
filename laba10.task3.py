import matplotlib.pyplot as plt


with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()


vowels = ['a', 'e', 'i', 'o', 'u', 'y']


counts = []
for v in vowels:
    counts.append(text.count(v))

plt.bar(vowels, counts)
plt.title("Частота появи голосних літер у тексті")
plt.xlabel("Голосні літери")
plt.ylabel("Кількість появ")

plt.savefig("histogram_golosni.png")
plt.show()
