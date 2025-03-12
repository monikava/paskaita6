
print("\n1 Užduotis\n")
print("----read----readline----readlines----")
people = open('.\\files\\people.csv')
read_people = people.read()
# readline_people = people.readline()
# readlines_people = people.readlines()

print("Read text: \n" + read_people)
# print(readline_people)
# print(readlines_people)

other_people = people.read()
print("Other text: \n" + other_people)

people.close()




