def setthreads(size, side):
    nominals = [8,10,12,14,16,18,20,22,25,28,32,36,40,45,50,56,63,70,80,90,100,112,125]
    try:
        threadindex = nominals.index(size)
    except:
        side = "error"
        print("Error\nThread specified is not in standards.\nGL thread standards include: 8,10,12,14,16,18,20,22,25,28,32,36,40,45,50,56,63,70,80,90,100,112,125")

        #print(size, side, threadindex)



    boltParameters = {"D_major_max": [8, 10, 12, 14, 16, 18, 20, 22, 25, 28, 32, 36, 40, 45, 50, 56, 63, 70, 80, 90, 100, 112 ,125],
                      "D_major_min": [7.65, 9.65, 11.65, 13.60, 15.60, 17.50, 19.50, 21.50, 24.50, 27.50, 31.30, 35.30, 39.3, 44.20, 49.20, 55.20, 62.00, 69.00, 79.00, 89.00, 89.80, 110.80, 123.80],
                      "D_minor_max": [6.60, 8.60, 10.60, 12.32, 14.32, 15.98, 17.98, 19.98, 22.98, 25.98, 29.30, 33.30, 37.30, 42.30, 47.30, 53.30, 60.00, 67.00, 77.00, 87.00, 97.00, 109.00, 122.00],
                      "D_minor_min": [6.25, 8.25, 10.25, 11.92, 13.92, 15.48, 17.48, 19.48, 22.48, 25.48, 28.60, 32.60, 36.60, 41.60, 46.50, 52.60, 59.00, 66.00, 76.00, 86.00, 95.00, 108.80, 120.80],
                      "pitch": [2.00, 2.00, 2.00, 2.50, 2.50, 3.00, 3.00, 3.00, 3.00, 3.50, 4.00, 4.00, 4.00, 4.00, 4.00, 4.00, 5.00, 5.00, 5.00, 5.00, 5.00, 5.00, 5.00]}

    nutParameters = {"D_major_max": [8.30, 10.30, 12.30, 14.35, 16.35, 18.40, 20.40, 22.40, 25.40, 28.40, 32.55, 36.55, 40.55, 45.55, 50.80, 56.80, 64.00, 71.00, 81.00, 91.00, 101.00, 113.00, 126.00],
                      "D_major_min": [8.10, 10.10, 12.10, 14.10, 16.10, 18.10, 20.10, 22.10, 25.10, 28.10, 32.15, 36.15, 40.15, 45.15, 50.30, 56.30, 63.40, 70.40, 80.40, 90.40, 100.40, 112.40, 125.40],
                      "D_minor_max": [6.90, 8.90, 10.90, 12.67, 14.67, 16.38, 18.38, 20.38, 23.38, 26.38, 29.85, 33.85, 37.85, 42.85, 48.10, 54.10, 61.00, 68.00, 78.00, 88.00, 98.00, 110.00, 123.00],
                      "D_minor_min": [6.70, 8.70, 10.70, 12.42, 14.42, 16.08, 18.08, 20.08, 23.08, 26.08, 29.45, 33.45, 37.45, 42.45, 47.60, 53.60, 60.40, 67.40, 77.40, 87.40, 97.40, 109.40, 122.40],
                      "pitch": [2.00, 2.00, 2.00, 2.50, 2.50, 3.00, 3.00, 3.00, 3.00, 3.50, 4.00, 4.00, 4.00, 4.00, 4.00, 4.00, 5.00, 5.00, 5.00, 5.00, 5.00, 5.00, 5.00]}
    if side == "bolt":
        #pull from bolt parameters
        return [boltParameters["D_major_max"][threadindex], boltParameters["D_major_min"][threadindex], boltParameters["D_minor_max"][threadindex], boltParameters["D_minor_min"][threadindex], boltParameters["pitch"][threadindex]]
    elif side == "nut":
        #pull from nut parameters
        return [nutParameters["D_major_max"][threadindex], nutParameters["D_major_min"][threadindex], nutParameters["D_minor_max"][threadindex], nutParameters["D_minor_min"][threadindex], nutParameters["pitch"][threadindex]]
    else:
        #error throw fit
        print("an error has occured using default GL14 threads")
        return [nutParameters["D_major_max"][3], nutParameters["D_major_min"][3], nutParameters["D_minor_max"][3], nutParameters["D_minor_min"][3], nutParameters["pitch"][3]]


class adapterside:
    def __init__(self, string):
        splitString = string.split("-")
        self.type = splitString[0]
        self.size = int(splitString[1])
        side = splitString[2]
        if side == "internal":
            self.side = "nut"
        elif side == "external":
            self.side = "bolt"
        else:
            self.side = side
    def taperparams(self):
        length = self.size % 100
        width = int((self.size - length)/100)
        return [width,length]
    def get_order(self):
        #set order based on order for solidworks model
        order = 0
        if self.type == "Taper":
            order += 1
        else:
            order += 3
        if self.side == "nut":
            order += 1
        else:
            order +=2
        return order

    def __str__(self):
        return f'{self.type} {self.size} {self.side}'
run = True
while run:	#I didnt want to fix the indent
#if __name__ == '__main__':
    setSide1 = False
    setSide2 = False

    print("This program is designed to generate an equations file for an adapter for glassblowing. It can do standard 10 to 1 taper joints and Knuckle Thread DIN 168 (GL designation).")
    while setSide1 == False:
        try:
            #select side 1
            side1input = input("What do you want on side 1? (examples: GL-14-nut, Taper-2440-external, GL-18-bolt): \n")
            side1 = adapterside(side1input)
            setSide1 = True
        except:
            print("Invalid Entry. Make sure to enter in the form 'standard-size-side' where standard can be Taper or GL, size is the nominal size, and side is internal, external, nut, or bolt")

    while setSide2 == False:
        try:
            #select side 2
            side2input = input("What do you want on side 2? (examples: GL-14-nut, Taper-2440-external, GL-18-bolt): \n")
            side2 = adapterside(side2input)
            setSide2 = True
        except:
            print("Invalid Entry. Make sure to enter in the form 'standard-size-side' where standard can be Taper or GL, size is the nominal size, and side is internal, external, nut, or bolt")

    #set proper sides, internal taper then external taper, then internal threads, then external threads


    #Taper {24}-{40} {10} series 7-25 is the min size and 103-60 is the max size in this series. they both work with the model
    #GL {14} {nut}

    #side1 = adapterside("GL", 14, "nut")
    #side2 = adapterside("Taper", 2440, "external")




    if side1.get_order() > side2.get_order():
        intermediate = side1
        side1 = side2
        side2 = intermediate
    #defaults
    Taper_1 = [24,40]
    Taper_2 = [24,40]
    GL_1 = 14
    GLType_1 = "nut"
    GL_2 = 14
    GLType_2 = "bolt"
    #set taper group
    taperSlope = 10
    #set thread parameters
    [D_major_max_1, D_major_min_1, D_minor_max_1, D_minor_min_1, pitch_1] = setthreads(GL_1, GLType_1)
    [D_major_max_2, D_major_min_2, D_minor_max_2, D_minor_min_2, pitch_2] = setthreads(GL_2, GLType_2)

    if side1.type == "GL":
        [D_major_max_1, D_major_min_1, D_minor_max_1, D_minor_min_1, pitch_1] = setthreads(side1.size, side1.side)
        #print("threads on side 1")
    elif side1.type == "Taper":
        Taper_1 = side1.taperparams()
        #print("taper on side 1")
    else:
       print("Using defaults on side 1")

    if side2.type == "GL":
        #print(side2.size)
        #print(side2.type)
        [D_major_max_2, D_major_min_2, D_minor_max_2, D_minor_min_2, pitch_2] = setthreads(side2.size, side2.side)
        #print("threads on side 2")
        #print([D_major_max_2, D_major_min_2, D_minor_max_2, D_minor_min_2, pitch_2])
    elif side2.type == "Taper":
        Taper_2 = side2.taperparams()
        #print("taper on side 2")
    else:
        print("Using defaults on side 2")

    #print([D_major_max_2, D_major_min_2, D_minor_max_2, D_minor_min_2, pitch_2])
    # Opening a file
    file1 = open('thread and taper adapter parameters.txt', 'w')


    equations = f"""
    "Taper slope" = {taperSlope}
    'standard taper ratio\n
    "min major diameter 1" = {D_major_min_1}
    'minimum major diameter\n
    "max major diameter 1" = {D_major_max_1}
    'max major diameter\n
    "major diameter 1" = ("min major diameter 1" + "max major diameter 1") / 2
    'average major diameter\n
    "min minor diameter 1" = {D_minor_min_1}
    'minimum major diameter\n
    "max minor diameter 1" = {D_minor_max_1}
    'max major diameter\n
    "minor diameter 1" = ("min minor diameter 1" + "max minor diameter 1") / 2
    'average major diameter\n

    "min major diameter 2" = {D_major_min_2}
    'minimum major diameter\n
    "max major diameter 2" = {D_major_max_2}
    'max major diameter\n
    "major diameter 2" = ("min major diameter 2" + "max major diameter 2") / 2
    'average major diameter\n
    "min minor diameter 2" = {D_minor_min_2}
    'minimum major diameter\n
    "max minor diameter 2" = {D_minor_max_2}
    'max major diameter\n
    "minor diameter 2" = ("min minor diameter 2" + "max minor diameter 2") / 2
    'average major diameter\n

    "pitch 1" = {pitch_1}
    'thread pitch\n
    "pitch 2" = {pitch_2}
    'thread pitch\n
    "Taper wide end 1" = {Taper_1[0]}
    'taper at larger end of taper\n
    "taper length 1" = {Taper_1[1]}
    'taper length\n
    "taper Wide end 2" = {Taper_2[0]}
    'large end of taper\n
    "taper length 2" = {Taper_2[1]}
    'taper length\n
    "wall min thickness" = 6
    'min thickness of walls add to outer most diameter of internal features will give thickness equal to half the value
    """

    # Writing multiple strings
    # at a time
    file1.write(equations)

    # Closing file
    file1.close()

    # Checking if the data is
    # written to file or not
    file1 = open('thread and taper adapter parameters.txt', 'r')
    #print(file1.read())
    print("New Equations file generated: 'thread and taper adapter parameters.txt'")
    file1.close()
    #print(side1)
    #print(side2)
    continueRunning = input("Type 1 to generate another")
    if continueRunning == 1:
        run = True
    else:
        run = False
