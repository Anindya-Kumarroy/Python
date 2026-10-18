collection=set()             # collection = {} , this is dictionary.
print(type(collection))
collection.add(1)
collection.add((1,2,3))      # Tuple adding.
print(collection)
collection.remove((1,2,3))   # Removing 
print(collection)

collection.clear()           # All cleared
print(collection)            # Everything removed.