def swappingfiles():
    file1 = input("enter files name - ")
    file2 = input("enter files name - ")

    with open(file1, 'r') as r:
    data_r = r.read()

	with open(file2, 'r') as r:
    data_r = r.read()

    with open(file1, 'w') as r:
    r.write(data_r)

    with open(file2, 'w') as r:
    r.write(data_a)

swappingfiles()