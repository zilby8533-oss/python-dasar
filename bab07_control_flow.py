# if - elif - else
nilai = 82
if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
else:
    grade = "D"
print("Nilai", nilai, "-> grade", grade)

# for loop
for i in range(1, 6):
    print("Perulangan ke-", i)

for buah in ["apel", "jeruk", "mangga"]:
    print("Buah:", buah)

# while, continue, dan break
hitung = 0
while True:
    hitung += 1
    if hitung == 3:
        continue
    if hitung > 5:
        break
    print("while:", hitung)
