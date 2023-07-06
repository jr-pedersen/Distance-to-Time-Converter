import csv
csv_file_path = "/Users/jakepedersen/desktop/gatewayDistances.csv"
o_file = "Glenn"  # ASSET NAME e.g. "TDRSX" OR " Goddard"

# converter fcn
def convertDistance(distance):
    return distance/300000


try:
    with open(csv_file_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # header
        with open(o_file, "w") as output:
            output.write(f"# Name : {o_file}\n")
            output.write("# Contents : BW, DELAY\n")
            for row in reader:
                time = row[0]
                distance = float(row[6])
                converted_time = convertDistance(distance)
                output.write(f"{time}, {converted_time}\n")
    print(f"Data imported successfully. The new file '{o_file}' has been created with converted vals")

except Exception as x:
    print("F", str(x))
