def extract_data(s):
    l = []
    with open(s, 'r') as f:
        for line in f:
            #print(line)  # new line char is being used
            line = line.replace("\n", "")
            #print(line)  # new line char is gone
            a = line.split(",")
            #print(a)  # right now, everything is a string
            date = a[0]
            #print(date)
            high = a[2]
            l.append([date, high])
    return l


def stock_change(new, old):
    return (100.0 * (new - old)) / old


def prepare_data(data):
    l = []
    for i in range(1, len(data) - 1):
        current_date = data[i + 1][0]
        old_high = float(data[i][1])
        new_high = float(data[i + 1][1])
        change = stock_change(new_high, old_high)
        l.append([current_date, new_high, change])
    return l


def write_data(s, p_data):
    with open(s, 'w') as f:
        f.write("data, highest price, change (%)\n")
        for e in p_data:
            date = e[0]
            #print(date)
            high = e[1]
            change = e[2]
            f.write("%s, %s, %s \n" % (date, str(high), str(change)))


def main():
    #data = extract_data("nasdaq.csv")
    #print(data)
    #p_data = prepare_data(data)
    #print(p_data)
    #write_data("output.csv", p_data)


main()
