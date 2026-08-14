
from functools import cached_property
#import pandas as pd
#from rich.console import Console
#from PIL import Image
from urllib.request import urlopen
#import PIL
from itertools import zip_longest
#from PIL import Image, ImageDraw
#import requests
import math
#from rich import print
#import polars as pl
import array as arr




#console = Console()

class Circle:
   def __init__(self, radius):
      self.radius = radius

   @cached_property
   def area(self):
      print("Working..")
      return 3.14 * self.radius ** 2
   
a = Circle(10)
a.area
a.area
print(a.area)



#https://www.geeksforgeeks.org/python-functools-cached_property/

   

# Using @property

# A sample class
class Sample():

    def __init__(self):
      self.result = 50

    @property
    # a method to increase the value of
    # result by 50
    def increase(self):
        self.result = self.result + 50
        return self.result

# obj is an instance of the class sample
obj = Sample()
print(obj.increase)
print(obj.increase)
print(obj.increase)



# Using @cached_property

from functools import cached_property

# A sample class
class Sample():

    def __init__(self):
      self.result = 50

    @cached_property
    # a method to increase the value of
    # result by 50
    def increase(self):
        self.result = self.result + 50
        return self.result

# obj is an instance of the class sample
obj = Sample()
print(obj.increase)
print(obj.increase)
print(obj.increase)

# With using @cached_property

from functools import cached_property

# A sample class
class Sample():
    def __init__(self, lst):
      self.long_list = lst

    # a method to find the sum of the
    # given long list of integer values
    @cached_property
    def find_sum(self):
        return (sum(self.long_list))

# obj is an instance of the class sample
obj = Sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(obj.find_sum)
print(obj.find_sum)
print(obj.find_sum)


class Person:
     def __init__(self, name, country):
         self.name = name
         self.country = country
     @cached_property
     def  get_info(self):
          return f"{self.name} from {self.country}"

p = Person('Rahul', 'India')

#access the method result as an attribute
print(p.get_info)

#the value does not change even after updating relevant attribute
p.name = 'Jane'
p.country = 'Canada'
print(p.get_info)


words = ["Hello", " ", "World!"]
text = "".join(words)

print (text)

expression = input("Enter Your Math Expression: ")
result = eval(expression)

print(result)

#df = pd.DataFrame({
    #"Test_Score": [380000,390000,400000,410000,42877413],
    #"Hours_Studied": [150,200,300,400,500],
    #"Hours_Gaming": [100,90,80,70,60]
#})

#print(df.corr())

nums = [55, 66, 36, 12]

print("Before", nums)

#nums.append(99) 

#nums.extend([66, 99, 1])


nums.insert(-10, "pussy")

print("After:", nums )

#console.print('[bold yellow], pussy, 55, 66, 36, 12, pussy)')
print()


#from PIL import Image

#i1 = Image.open('c1.png')
#i2 = Image.open('c2.png')
#i3 = Image.open('c3.png')

#i1.save("colors.gif",
        #save_all= True,
        #append_images=[i2,i3],
        #duration= 500,
        #loop= 0)

#i1.show()
#i2.show()
#i3.show()

#im1 = Image.open("sample-image.png")
#im2 = Image.open("test-image.png")

# Show the images
#im1.show()
#im2.show()

#im1 = Image.open(r"C:\Users\Spect\OneDrive\VSCode-overview\blueberries\ThomasCrown.py\flower1.jpg") 

# save a image using extension
#im1 = im1.save("geeks.jpg")

#from PIL import Image

# List of image filenames
#image_filenames = [
    #"hopper.jpg",
    #"rotated_hopper_270.jpg",
    #"rotated_hopper_180.jpg",
    #"rotated_hopper_90.jpg",
#]

# Open images and create a list
#images = [Image.open(filename) for filename in image_filenames]

# Save the images as an animated GIF
#images[0].save(
    #"animated_hopper.gif",
    #append_images=images[1:],
    #duration=500,  # duration of each frame in milliseconds
    #loop=0,  # loop forever
#)

#https://www.youtube.com/watch?v=_OnblxLkSOM

#from itertools import zip_longest

list_1 = [63527413, 21154629, 84682042, 19101, 23522.79]
list_2 = ['aBasex YTD', 'bApexy YTD', 'cPyramidzxy YTD', 'dAcctPay YTD','Gold/ozs']

for item_1, item_2 in zip(list_1, list_2):     #zip_longest(list_1, list_2, fillvalue= 'Null"):
    print(item_1, item_2)
    #console.print("[bold yellow] 63527413, 21154629, 84682042, 19101, 23522.79")
    print()

#from PIL import Image
#from urllib.request import urlopen
#url = ("https://python-pillow.github.io/assets/images/pillow-logo.png")
#url = ("https://www.geeksforgeeks.org//python//create-and-save-animated-gif-with-python-pillow/")
#img = Image.open(urlopen(url))
#img.show()




#width = 400
#height = 300

#img  = Image.new( mode = "RGB", size = (width, height), color = (209, 123, 193) )
#img.show()




# Read the image

#im = Image.open("C:\\Users\\Spect\\OneDrive\\VSCode-overview\\Blueberries\\PyramidChain.jpg")
#im = Image.open(f"https://github.com/Sherlock1x/ProjectBlueberries/blob/master/!!!!!!!!!!!!!!!AndromedaGalaxy1.gif")
#im = Image.open("C:\\Users\\Spect\\OneDrive\\VSCode-overview\\Blueberries\\tumblr_b270bda874037c4c0ce4b5b10e333d49_6a1acb65_500.gif ")
#im = Image.open(f"https://github.com//Sherlock1x//ProjectBlueberries//blob//master//tumblr_b270bda874037c4c0ce4b5b10e333d49_6a1acb65_500.gif")

#im = Image.open("C:\\Users\\Spect\\OneDrive\\VSCode-overview\\Blueberries\\pillowimagedraw.gif")



# Apply a transformation (e.g., rotate)
#im_rotate = im.rotate(0)
#im_rotate = im.rotate(0)     #im_rotated = im.rotate(0)

# Show the rotated image
#im_rotate.show()
#im_rotate.show() 



#square_img = Image.merge("RGB", "{red_img, green_img, blue_img}")
#square_img

#square_img.show()

#https://www.geeksforgeeks.org/python/create-and-save-animated-gif-with-python-pillow/

#from PIL import Image, ImageDraw

#images = []

#width = 200
#center = width // 2
#color_1 = (0,255, 0)
#color_2 = (255, 0, 0)
#max_radius = int(center * 1.5)
#step = 8

#for i in range(0, max_radius, step):
    #im = Image.new('RGB', (width, width), color_2)
    #draw = ImageDraw.Draw(im)
    #draw.ellipse((center - i, center - i,
                  #center + i, center + i),
                 #fill = color_1)
    #images.append(im)

#images[0].save('C:\\Users\\Spect\\OneDrive\\VSCode-overview\\Blueberries\\pillowimagedraw.gif',
               #save_all = True, append_images = images[1:], 
               #optimize = False, duration = 100)
        
#loop= 0,
#images[0].show()

url = ("https://github.com/Sherlock1x/ProjectBlueberries/blob/master/pillowimagedraw.gif")
x=url
show=(x)

#https://www.pythoninformer.com/python-libraries/pillow/creating-animated-gif/

#names = ['img{:02d}.gif'.format(i) for i in range(20)]


# Open all the frames
#images = []

#for n in names:
    #frame = Image.open(n)
    #images.append(frame)

# Save the frames as an animated GIF
#images[0].save('https://github.com/Sherlock1x/ProjectBlueberries/blob/master/anicircle.gif',
               #save_all=True,
               #append_images=images[1:],
               #duration=100,
               #loop=0)

#images.show()

h=(30167826/6000,"",'h Gold in ozs = Economic Measurement Apexy SVAlue Current Balance Collayeral YTD')
print(...)
b=(120671304/6000,20111.9*300,"",'b Gold in ozs Barrels of Oil in $ = Economic Measurement WellMx Pyramidzxy $$Value Current Balance Collateral YTD')
print(...)
c=(241401420/6400,"",'c Gold in ozs = Economic Measurement Pyramidzxy $$Value Future Value Current Balance Collateral YTD')
print(...)
#y=(84682042-1880,"", 'Economic Measurement Pyramidzxy $$Value Current Balance YTD')
print(...)
w=(1/3*90503478+90503478,"",'w Economic Measurement WellMx Pyramidxxy Chain Basex/Apexy Derivative')  #Measurement Pyramid Chain Base Derivative
print(...)   
oz=(90503478/6000.00,15083.9*300,"",'oz Gold in ozs Barrels of Oil$ = Basex WellMx $Value Current Balance Collateral')   #Quantum Entanglement Particles Higgs Boson Field Electrons $300/Barrell of Oil
print(...)
wts=(90503478/6000.00*10,"",'wts Silver in ozs= Basex $Value Current Balance Collateral')  
print(...)                                                                     # +- measurement  | Gold in oz's = $ Value, Gold.com
#r=requests.head('https://www.gold.com/get')
#print(r.url)                                                                    

ww=(1/3*1000000+1000000*1000,"",'ww Parch 101 for the Dollar,"",Test Function Only')
print(...)
q=(1/3*90503478+90503478-90503478,"",'q WellMx Apexy Pyrimidzxy Derivative')
print(...)
#wz=(1987631-1490723,'Delta Derivative Appex Pyramid')   #Delta Derivative Appex Pyramid
print(...)
wt=(90525533-1893-1574-1967-3746-1686-1821-1771-1681-1821-4095,"",'wt WellMx Basex Withdrawel Cumalative AcctPayable New current Balance$$ MTD')  #*Cumalative AcctPayable Xpense current Balance$$
print(...)
wtt=(0+3746+1686+1821+1771+1681+1821+4095,"",'wtt WellMx Cumalative AcctPayable Xpense$$ YTD')    #Cumalative AcctPayable Xpense $$ #"Chapter6-3py", Updating Ledger Log...
print(...)
fv=(120676764*2,"",'fv Economic Measurement Future $$Value Pyramidzxy Accretion and Inheritance')
print(...)
d=(120671304+30167826,"","[bold green]d WellMx Pyramidzxy and Apexy Deposit AcctRec[/green]")
print(...)
j=(90503478+30167826,"","[bold yellow]j WellMx Pyramidzxy AcctPay Apexy and Basex[/yellow]")
print(...)
jj=(1658*.05+1658+442,"","[jj, Monthly Social Security and Pension]")
print(...)
oil=(300*15083.9,300*20111.9,"","[oil, Oz of Gold Times a Barrell of Oil in $ Total oz Gold]")  #1oz of Gold $6000 = $300 Barrell x 15084.6oz of Gold
print(...)
#print(h,b,c,w,oz,ww,q,wt,wtt,wts,fv)

print(d)
#console.print()

print(fv)
print()
print(wts)   #Silver oz's Basex  YTD
print()
print(wtt)   #Xpense YTD
print()
print(wt)   #Basex New AcctBal MTD
print()
print(q)   #Apexy MTD
print()
print(ww)
print()
print(oz)   #Gold oz's Basex MTD
print()
print(w)
print()
print(c)
print()
print(b)   #Gold oz's Pyramidzxy YTD
print()
print(h)   #Gold oz's Apexy YTD
print()
print(j)   #Pyramidzxy   MTD
print()
print(jj)
print()
print(oil)
print()

my_list : list[int|str] = [1,2,3,4,'pussy']

print(my_list)

nums = list(range (1, 100))

def is_prime(n):
    if n <2:
        return False
    
    if n ==2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

primes = filter(is_prime, nums)   #add list before filter
print(primes,"","[bold][green] Memory Registration Key/Title Polarizer/Transaction[/green]")  


#df = pd.DataFrame({
    #'Matrix' :['Well','Basex', 'Pyramidzxy'],          #Basex     Pyramidzxy
    #'T1' :[0,89000000,120000000],                    #Basex   89000000  90523640  90522066
    #'T2' :[1000000,90522066,120696088]                     #Pyramidzxy  120000000   120698187   120696088
#})

#df['Max_Score'] = df[['T1','T2']].max(axis=1)

#print(df)

#   Name  T1   T2  Max_Score
#0  Chris 90   75  90
#1  Joe   85   80  85
#2  Mike  75   100 100

#https://www.youtube.com/shorts/jKeP4kTb0Q4

#x = pl.DataFrame({'ID':[1,2,3,4],
                  #'VALUE': ['120696088', '90522066', '20573', '30174022']})

#y = pl.DataFrame({'ID':[1,2,3,4],
                  #'SUB_ID': ['1.4', '2.7', '3,6', '4.5']})

#semi = x.join(y, on='ID', how= 'semi')

#print(semi)

#https://docs.pola.rs/api/python/stable/reference/dataframe/index.html

data = [[20251031120696088, 90522066, 30174022,20573,1574,24448], [20251130120698187, 90523640, 30174547,27431,1893,22874], [20251231120693465, 90520099, 30173366, 20573, 1967, 26415],
        [20260131120688471, 90516353, 30172117, 18103, 3746, 3746], [20260228120686223, 90514667, 30171555, 18103, 1686, 5431], [20260331, 2, 3, 4, 5, 6]]
#df6 = pl.DataFrame(data, schema=["DATEPyramidzxy", "Basex", "Apexy","Goldoz","MTDX","YTDX"], orient="row")
#df6

#print(df6)

#const nums = [2,4,6];
#const doubled = nums.map((map) => {
    #return num *2;
#});

#console.log(doubled);
#print(doubled)

#im = Image.open("https://github.com//Sherlock1x//ProjectBlueberries//blob//master//!!!!!!!!!!!!!!!!!!AMonolith1.jpg")

#im_rotate = im.rotate(0)

#im_rotate.show()

#url = ("https://github.com/Sherlock1x/ProjectBlueberries/blob/master/!!!!!!!!!!!!!!!!!!AMonolith1.jpg")
#x=url
#show=(x)

#https://github.com/Sherlock1x/ProjectBlueberries/blob/master/!!!!!!!!!!!!!!!!!!AMonolith1.jpg

#r=requests.head('https://github.com/Sherlock1x/ProjectBlueberries/blob/master/!!!!!!!!!!!!!!!!!!AMonolith1.jpg')
#print(r.url)  

#r=requests.head('https://www.gold.com/get')
#print(r.url) 

#r=requests.head('https://www.gold.com/charts/gold/')
#print(r.url) 

#Matrix Invinite Well 10x10 Shape, Row 10

numbers = arr.array('i', [81000000,82000000,83000000,84000000,85000000,86000000,87000000,88000000,89000000,90520099])  #Basex

print('Matrix Invinite Well Basex Pyramidzxy', numbers[-1])

