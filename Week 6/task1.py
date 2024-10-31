import os
def cwd():
    path = os.getcwd()
    print(f"Current working directory: {path}")
    print("The directory contains the following files:")
    for file in os.listdir(path):
        print(file)

def run():
    print ("processing.......")
    cwd()

run()