class decoder3x8():
    def __init__(self):
        self.outlines8 = [0,0,0,0,0,0,0,1]
    def decode(self, inlines3:list):
        for i in range(len(self.outlines8)):
            self.outlines8[i] = 0
        index = inlines3[0] * 4 + inlines3[1] * 2 + inlines3[2]
        self.outlines8[7-index] = 1
        return self.outlines8
    

class demultiplexer():
    def __init__(self):
        self.dedecoder = decoder3x8()
        self.outline = [0,0,0,0,0,0,0,0]
    def demultiplex(self, value:int, inlines3:list):
        outlines = self.dedecoder.decode(inlines3)
        for i in range(len(outlines)):
            self.outline[i] = 0
            if(outlines[i] and value):
                self.outline[i] = value
        return self.outline

dedemu = demultiplexer()
print(dedemu.demultiplex(1, [0,1,1]))
print(dedemu.demultiplex(1, [1,1,1]))