import os 
import sys

def main(): 
    startNumber = 1
      
    for filename in os.listdir("./"): 
        if filename != sys.argv[0]:
            dst = str(startNumber) + ".jpg"
            src = filename 
            os.rename(src, dst) 
            startNumber += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 