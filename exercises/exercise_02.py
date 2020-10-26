## Make the attributes of the MSPeaks class private

# initalize the instance right after creation
class MSPeak:
    def __init__(self,
                 mz=None,
                 intensity=None,
                 rt=None):
        self.__mz = mz
        self.__intensity = intensity
        self.__rt = rt

    def set_mz(self, mz):
        self.__mz = mz

    def get_mz(self):
        return self.__mz

    def set_intensity(self, intensity):
        self.__intensity = intensity

    def get_intensity(self):
        return self.__intensity

    def set_rt(self, rt):
        self.__rt = rt

    def get_rt(self):
        return self.__rt

    def show_peak(self):
        if self.__mz and self.__intensity and self.__rt:
            print("The peak can be found at mz " + str(self.__mz) + " with an intensity of " + str(self.__intensity) +
                  " at the retention time of " + str(self.__rt) + " seconds")
        else:
            print("Error: Either rt, mz, intensity or several values are missing - could not show the peak!")


if __name__ == "__main__":
    # x = MSPeak(250, 60000, 500) # using the __init__ method "constructor"
    x = MSPeak()
    x.show_peak()
    x.set_mz(250)
    x.set_intensity(600000)
    x.set_rt(500)
    x.show_peak()
