import os 
import sys

def main(): 
    startNumber = 21 # aka the number you LEFT ON last time
      
    for filename in os.listdir("./"):
        # checks to see if the filename is a number and if the file isnt the script it's self
        if filename != sys.argv[0] and not filename.split(".")[0].isdigit():
            startNumber += 1
            dst = str(startNumber) + ".jpg"
            src = filename 
            os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 