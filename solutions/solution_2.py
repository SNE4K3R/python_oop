### solution: Make members of MSPeak private 

# private member variables
# data Abstraction = Data Encapsulation + Data Hiding
# encapsulation is seen as the bundling of data with the methods that operate on that data
# information hiding on the other hand is the principle that some internal 
# information or data is "hidden", so that it can't be accidentally changed

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
            print("Error: Either mz or intensity or retention time or all three values are missing - could not show the peak!")
            

if __name__ == "__main__": 
    x = MSPeak(250, 60000, 300)
    x.show_peak()
    # x.mz(300) -> leads to an error, since variable is private
    print(x.get_mz())
    x.set_mz(500)
    print(x.get_mz())
    x.show_peak()
    
    print("Adding an additional peak: ")
    y = MSPeak(800, 80000, 600)
    
    for peak in [x,y]:
        peak.show_peak()
        
# getter and setter can be usually provided automatically by an IDE for every member variable.

# a even more pythonic way would be to use @property together with public variables for an example please see "code_chunks/2_additional_info_property_instead_of_private.py"
