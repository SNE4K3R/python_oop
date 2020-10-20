
# use static method to count instances without creating one
class MSPeak:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
    
    @staticmethod # does not need a reference to an instance!
    def instanceCount():
        return MSPeak.__counter
    
if __name__ == "__main__":
    print(MSPeak.instanceCount())
    x = MSPeak()
    print(x.instanceCount())
    print(MSPeak.instanceCount())
