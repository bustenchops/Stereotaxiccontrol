def calibratedistance():
    global APsteps
    global MVsteps
    global DVsteps

    global APstepdistance
    global MVstepdistance
    global DVstepdistance
    file_name = '../Calibration.txt'
    calibratetemp = ['a','b','c']
    print(calibratetemp)
    r = 0
    file = open(file_name, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        print(line.strip())
        calibratetemp[r] = line.strip()
        print(calibratetemp[r])
        r += 1
    file.close()

    APstepdistance = calibratetemp[0]
    MVstepdistance = calibratetemp[1]
    DVstepdistance = calibratetemp[2]
    print('here')
    print(APstepdistance)
    print(MVstepdistance)
    print(DVstepdistance)


    calibratetemp[0] = "fuck"
    calibratetemp[1] = "right"
    calibratetemp[2] = "off"

    # Specify the file name


    # Open the file in write mode
    with open(file_name, "w") as file:
        # Write each variable to the file in Pine Script format
        for x, value in enumerate(calibratetemp):

            varvalue = calibratetemp[x]
            file.write(f"{varvalue}\n")
    file.close()
    print(f"Variables have been written to calibration.txt")

calibratedistance()