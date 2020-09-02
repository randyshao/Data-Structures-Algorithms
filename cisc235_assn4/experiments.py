import assn4

def main():

    data = open("HOTNCU_project_names_2020.txt", "r")
    setData = []

    for i in data:
        setData.append(i[:-1])

    print(setData)

    table = 2301
    hash = assn4.HashTable()
    hash.avgSearchLength(setData, table)

main()