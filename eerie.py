f = open("save_data.txt", "w")
f.write("Goodbye World!")
f.close()

f = open("save_data.txt", "r")
print(f.read())
