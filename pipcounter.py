file1 = open("Data.txt", "r")# this will open the file in read mode so that

d = dict()# this is to create an empty dictionary


for line in file1:

    line = line.strip()

    numbers = line.split(" ")



    for number in numbers:


        if number in d:

            d[number] = d[number] + 1

        else:

            d[number] = 1


for key in list(d.keys()):
    print(key,":", d[key])

file1.close
