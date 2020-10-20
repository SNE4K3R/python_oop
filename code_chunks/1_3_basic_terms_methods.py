# method

# initalize the instance right after creation
class MSPeak:
    def __init__(self,
                 mz=None,
                 intensity=None):
        self.mz = mz
        self.intensity = intensity
    
    def show_peak(self):
        if self.mz and self.intensity:
            print("The peak can be found at mz " + str(self.mz) + " with an intensity of " + str(self.intensity))
        else:
            print("Error: Either mz or intensity or both values are missing - could not show the peak!")

if __name__ == "__main__": 
    # x = MSPeak(250, 60000) # using the __init__ method "constructor"
    x = MSPeak()
    x.show_peak()
    x.mz = 250
    x.intensity = 600000
    x.show_peak()
