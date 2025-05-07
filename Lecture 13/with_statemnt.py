import os
os.getcwd()

fstream = open("my_first_txt_file.txt", "w")
try:
    fstream.write("1Hello мир!\n")
    fstream.write("H2ello мир!\n")
    fstream.write("He3llo мир!\n")
    fstream.write("Hel4lo мир!\n")
    fstream.write("Hell5o мир!\n")
    fstream.write("Hello6 мир!\n")
    fstream.write("Hello 7мир!\n")
except:
    print("up")
finally:
    fstream.close()

with open("my_second_txt_file.txt", "w") as fstream:
    fstream.write("1Hello мир!\n")
    fstream.write("H2ello мир!\n")
    fstream.write("He3llo мир!\n")
    fstream.write("Hel4lo мир!\n")
    fstream.write("Hell5o мир!\n")
    fstream.write("Hello6 мир!\n")
    fstream.write("Hello 7мир!\n")
