
x = int(input())

f = open("track.txt", "w")

print("#include <iostream>")
print("#include <stdlib.h>")

print("int main(int argc, char* argv[]) {")
print("int number = atoi(argv[1]);")

for i in range(0, x):
    ans = "\"Even\\n\"" if i % 2 == 0 else "\"Odd\\n\""
    print("if(number == ", str(i), ") {")
    print("std::cout << " + ans + " << std::endl;")
    print("}")
    f.write(str(i) + "\n")

print("}")
