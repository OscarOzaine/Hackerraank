def newRoadSystem(roadRegister):
    s = 0
    ss = 0
    for i in range(0, len(roadRegister)):
        s = sum(roadRegister[i])
        ss = 0
        for row in roadRegister:
            if row[i] == True:
                ss += 1

        if s != ss:
            return False
    return True
    