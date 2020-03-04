from Smali.Dex import *
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("python Cli {dex_file} [outputdir]")
        sys.exit(0)
    elif len(sys.argv) == 3:
        outputdir = sys.argv[2]
    dex_file = sys.argv[1]
    dex = Dex(dex_file)
    print(dex)
    print(dex.getClass(720))
#    classes = dex.getAllClasses()
#    for _class in classes:
#        print(_class)
