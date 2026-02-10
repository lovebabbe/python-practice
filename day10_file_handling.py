# Write data to a file
file = open("students.txt", "w")
file.write("Amit - 78\nNeha - 85\nRahul - 90")
file.close()

print("Data written to file")



# Read data from a file
file = open("students.txt", "r")
content = file.read()
print(content)
file.close()




# Append data to a file
file = open("students.txt", "a")
file.write("\nSita - 88")
file.close()

print("Data appended")




# Read file line by line
file = open("students.txt", "r")
for line in file:
    print(line)
file.close()


