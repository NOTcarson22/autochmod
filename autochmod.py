import os
def autoChmod(filename):
    os.system("touch " + str(filename))
    os.system("chmod uog=rwx " + str(filename))
print(autoChmod(input("type a filename and its exstension: ")))
