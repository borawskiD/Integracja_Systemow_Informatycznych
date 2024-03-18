import csv


def generate(start, end):

    start = (start.split("."))
    end = end.split(".")

    start = [int(x) for x in start]
    end = [int(x) for x in end]


    while start[3] != end[3]:
        start[3] = start[3] + 1
        print()
        return [str(start[0]) + "." + str(start[1]) + "." + str(start[2]) + "." + str(start[3]), "P" + str(start[3])]
    print(start)


def openFile():
    with open('pc.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["pc_name", "ip"]
        writer.writerow(field)
        current = "172.30.2.0"
        end = "172.30.2.100"
        while (current != end):
            newUser = generate(current, end)
            current = newUser[0]
            writer.writerow(newUser)

openFile()