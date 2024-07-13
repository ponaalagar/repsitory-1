def myReader(filename):
    try:
        with open(filename, 'r+') as f:
            fcontent=f.read()
            print(fcontent)
    except IOError:
        print(IOError)
    else:
        print("ok")
fname=input('Enter the filename : ')
myReader(fname)

