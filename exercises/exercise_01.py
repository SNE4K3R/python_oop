## Add the retention time to the MSPeaks class

# initalize the instance right after creation
class MSPeak:
    def __init__(self,
                 mz=None,
                 intensity=None,
                 rt=None):
        self.mz = mz
        self.intensity = intensity
        self.rt = rt

    def show_peak(self):
        if self.mz and self.intensity and self.rt:
            print("The peak can be found at rt " + str(self.rt) + " and at mz " + str(self.mz) + " with an intensity of " + str(self.intensity))
        else:
            print("Error: Either rt, mz, intensity or several values are missing - could not show the peak!")


if __name__ == "__main__":
    # x = MSPeak(250, 60000) # using the __init__ method "constructor"
    x = MSPeak()
    x.show_peak()
    x.mz = 250
    x.intensity = 600000
    x.rt = 100
    x.show_peak()
