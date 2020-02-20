s = str(input())
a_index = s.find("A")
b_index = s.rfind("Z")
print(b_index - a_index + 1)