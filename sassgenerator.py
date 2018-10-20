from bs4 import BeautifulSoup
import glob
import os
import sassgen

if __name__ == "__main__" :
    # pathName = os.path.dirname(__file__)
    # print(glob.glob(pathName + "/*.html"))
    gen = sassgen.GenerateComponents()
    files = os.listdir('./html')
    for file in files:
        html = BeautifulSoup(open("./html/" + file), "html.parser")
        print(gen.getClasses(html))
        print('\n')












