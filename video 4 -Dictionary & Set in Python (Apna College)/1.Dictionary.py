info={
    "Name":"Anindya",
    "Age":21,
    "Wife":"Neirjara Singh",
    "Her age":20,
    "Are adult":True
}
print(info)
print(info["Wife"])  #individual element printing.
info["Wife"]="Bina"
info["Surname"]="Chakrabarty"  #newly added.
print(info["Wife"])
print(info["Surname"])
print(type(info))