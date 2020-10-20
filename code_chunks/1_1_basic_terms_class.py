# Class 
class MSPeak:
    pass # null operation - placeholder


# if module is imported by another program main is not used. 
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__": 
    x = MSPeak() 
    y = MSPeak()
    y_alias = y # reference to y 
    
    print(x==y)
    print(y==y_alias) 
