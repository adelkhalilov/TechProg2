#!/usr/bin/python3
file = open ("index.h", "w")
file.write("#include <iostream>\n")
file.write("void index()\n")
file.write("{\n")
file.write("	std::cout << \"world \";\n")
file.write("}\n")
