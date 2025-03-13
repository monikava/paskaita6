
print("\n1 Užduotis. Susikurkite vieną keletą failų, pamėginkite juos nuskaityti taikant įvairas metodikas (viską vienu metu, po atskirą eilutę, sudedant į dictionary, ir pan.).")
print("\n----read----readline----readlines----\n")

text = open('.\\files\\tekstas.txt')
read_text = text.read()
# readline_text = text.readline()
# readlines_text = text.readlines()

print("Read text: \n" + read_text)
# print(readline_text)
# print(readlines_text)

other_text = text.read()
print("\nOther text: \n" + other_text)

text.close()

print("\n----seek----\n")

text = open('.\\files\\tekstas.txt')
read_text = text.read()
print("Read text: \n" + read_text)

text.seek(0)
seek_text = text.read()
print("\nSeek text: \n" + seek_text)
text.close()

print("\n----with----\n")

with open('.\\files\\tekstas.txt') as file:
    text = file.read()
print(text)

file = open('.\\files\\tekstas.txt')
text = file.read()
print("\n" + text)

print(file.closed)
file.close()
print(file.closed)
# print(file.read())

file = open('.\\files\\tekstas.txt')
text = file.read()
close_text = file.close()
print(file.closed)

with open('.\\files\\tekstas.txt') as file:
    text2 = file.read()
print(file.closed)

with open('.\\files\\tekstas.txt') as file2:
    line = file2.readline()
    print(line)
    line = file2.readline()
    print(line)
    line = file2.readline()
    print(line)
    line = file2.readline()
    print(line)
    line = file2.readline()
    print(line)

with open('.\\files\\tekstas.txt') as file3:
    whole_file = file3.readlines()
    print("Whole file: \n" + str(whole_file))
    fixed_file = [line3[:-1] for line3 in whole_file]
    # fixed_file = [line3.rstrip('\n') for line3 in whole_file]
    print("Fixed file: \n" + str(fixed_file))

with open('.\\files\\tekstas.txt') as file4:
    text4 = file4.read().splitlines()
    print(text4)

with open('.\\files\\tekstas.txt') as file5:
    print(type(file5.read()))
    file5.seek(0)
    print(type(file5.readline()))
    file5.seek(0)
    print(type(file5.readlines()))

lines = []

with open('.\\files\\tekstas.txt') as file6:
    while True:
        line6 = file6.readline().rstrip("\n")
        if not line6:
            break
        print("Line read: ", line6)
        lines.append(line6)
print(lines)

lines2 = []
with open('.\\files\\tekstas.txt') as file7:
    for line7 in file7:
        line7 = line7.rstrip("\n")
        print("Line read: ", line7)
        lines2.append(line7)
print(lines2)

students = []

with open('.\\files\\studentai.txt') as file8:
    for row in file8:
        row = row.rstrip("\n")
        split_row = row.split(";")
        student = dict(
            name=split_row[0],
            surname=split_row[1],
            age=split_row[2],
            university=split_row[3],
            average=split_row[4]
        )
        students.append(student)
print(students)

print("\n2 Užduotis. Pamėginkite išvesti skirtingą informaciją į keletą atskirų failų. Tiek perrašant kas yra tame faile, tiek bandant jį papildyti. Galite išvesti kokių nors skaičiavimų informaciją.")

with open('.\\files\\writing.csv','w') as writing:
    writing.write('first\n')
    writing.write('second\n')
    writing.write('third\n')
    writing.write('fourth\n')

writing = open('.\\files\\writing.csv','w')
writing.write('sixth\n')
writing.close()

with open('.\\files\\writing.csv','w') as writing:
    writing.write("previously added text\n")
with open('.\\files\\writing.csv','w') as writing:
    writing.write("Labas krabas\n")
with open('.\\files\\writing.csv','a') as writing:
    writing.write("more text\n")
    writing.write("and even more text\n")
    writing.write("and even more text\n")
    writing.write("and even more text\n")
with open('.\\files\\writing.csv','r+') as writing:
    writing.write("add a little bit of text\n")

with open('.\\files\\writing.csv','w') as writing:
    writing.write("I was here first")

with open('.\\files\\writing.csv','r+') as writing:
    writing.write(':)')
    writing.seek(10)
    writing.write(":(")


print("\n3 Užduotis. Susikurkite duomenų failą, iš kurio nusiskaitytumėte informaciją apie automobilius. Išskaičiuokite keletą norimų dalykų (pvz. metų vidurkį) ir skaičiavimų rezultatus išveskite rezultatų faile.")

with open('.\\files\\cars.csv') as cars:
    cars.read()


