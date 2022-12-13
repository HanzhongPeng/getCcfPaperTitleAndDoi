import csv

def read_csv(csvFileName):
    name_all = []  #包含了ABC三个list
    name_A = []
    name_B = []
    name_C = []
    with open(csvFileName, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['level'] == "A":
                name_A.append(row["website"].strip())
            if row['level'] == "B":
                name_B.append(row["website"].strip())
            if row['level'] == "C":
                name_C.append(row["website"].strip())
        name_all.append(name_A)
        name_all.append(name_B)
        name_all.append(name_C)

        return name_all

# result 0\1\2分别是ABC类会议的包含的volume
# result = read_csv("conf_csv.csv")
# print(result[2])

