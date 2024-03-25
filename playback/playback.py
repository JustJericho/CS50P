#input

data = input()
f_data = ""

#loop for replacement

#huh odd
#treating x as some random char, I have no clue how to access .at() like in c++
#python is weird

for x in data:
    if(x) == " ":
        x="..."
        f_data = f_data + x
    else:
        f_data = f_data + x
#print

print(f_data)