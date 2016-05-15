#Hello World! by lorszil

import sys

def main():

# name
    if len(sys.argv) == 2:
        name = sys.argv[1]

# no name
    else:
        name = "World"

#hello name
    print( "Hello", name,"!" )

# if __name__ == "__main__":
    #execute only if run as a script
main()
