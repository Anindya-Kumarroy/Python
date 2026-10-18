str="i am learning Python from Shraddha Khapra"     
print(str.endswith("pra"))                       # If ends then True, otherwise False.
print(str.capitalize())                          # First letter of the string became capital.
print(str)                                       # No changes in main string.

print(str.replace("o","a"))                      # o will be replacesd by a.
print(str.replace("Python","Javascript"))        # Python will be replaced by Javascript.

print(str.find("o"))                             # First index where o exist for the first time will be returned.
print(str.find("Q"))                             # Doesn't exist ,so -1 will be returned.

print(str.count("o"))                            # How many times o exist .