def remove_letter(x, world):
    nw=""
    for i in world:
        if x not in i:
            nw += i
    return nw

print(remove_letter('a', "apple") == "pple")
