APDRILL = 0
MVDRILL = 0
DVDRILL = 0
APneedle = 0
MVneedle = 0
DVneedle = 0
APfiber = 0
MVfiber = 0
DVfiber = 0


class fuck:

    def __init__(self):

        self.offsetimport = []
        self.importfile_name = 'offsets.txt'
        self.offsetimport = []
        self.importfile_name = 'offsets.txt'

        file = open(self.importfile_name, 'r')

        while True:
            line = file.readline()
            if not line:
                break
            self.offsetimport.append(line.strip())
        file.close()
        fuck.APDRILL = self.offsetimport[0]
        fuck.MVDRILL = self.offsetimport[1]
        fuck.DVDRILL = self.offsetimport[2]

        fuck.APneedle = self.offsetimport[3]
        fuck.MVneedle = self.offsetimport[4]
        fuck.DVneedle = self.offsetimport[5]

        fuck.APfiber = self.offsetimport[6]
        fuck.MVfiber = self.offsetimport[7]
        fuck.DVfiber = self.offsetimport[8]

        print('offset values')
        print(fuck.APDRILL)
        print(fuck.MVDRILL)
        print(fuck.DVDRILL)
        print(fuck.APneedle)
        print(fuck.MVneedle)
        print(fuck.MVneedle)
        print(fuck.APfiber)
        print(fuck.MVfiber)
        print(fuck.DVfiber)

letsgo = fuck()