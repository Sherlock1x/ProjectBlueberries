#File "MasterPyramidChainModule101.py"

#"In the beginning was the Universe" John1:1a

import numpy

import numpy as np

arr = np.arange(100).reshape(10,10)

print (arr)

arr= arr*10000000

print(arr)

arr = np.arange(100).reshape(10,10)

print (arr)

arr= arr*10000

print (arr)

print (arr. nbytes) #(’Memory used (in bytes; 0 to 100 _PyramidChainContainers_ )

#http://matplotlib.org/api/pyplot_summary.html
import matplotlib.pyplot as plt
plt.plot(0,0,10,10,5,5,'ro')
plt.show()




import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
                30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
                84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])
print(s1) 


def Tracer(aClass):                                                ##On a decorator
    class Wrapper:
        def init(self, *args, **kargs):                            #On an instance creation
            self.wrapped = aClass(*args, **kargs)                  #Using enclosing scope name
        def getattr(self, attrname):
            print('Tracer:', attrname)
            return getattr(self.wrapped, attrname)                 #catches all but .wrapped
            return Wrapper                                         #delegate to wrapped object
@Tracer                                                               
class WorldVisionVirtualBank:  #Person:                            #Person = Tracer (Person)
    def init(self, name, amount, xpense):   #hours, rate):         #Wrapper remembers Person
        self.name = name
        self.amount = amount   #self.hours = hours
        self.xpense = xpense   #self.rate = rate                   #In-method fetch not traced
    def balance(self):         #def pay(self):
        return self.amount, -self.xpense     #return self.hours, *self.rate
        
@Tracer                                                               
class Container1:  #Person:                                                #Person = Tracer (Person)
    def init(self, name, amount, xpense):   #hours, rate):         #Wrapper remembers Person
        self.name = name
        self.amount = amount   #self.hours = hours
        self.xpense = xpense   #self.rate = rate                   #In-method fetch not traced
    def balance(self):         #def pay(self):
        return self.amount, -self.xpense     #return self.hours, *self.rate
    
@Tracer
class Acttrec1x100:
    def init(self, name, amount, xpense):
        self.name = name
        self.amount = amount
        self.xpense = xpense
    def balance(self):
        return self.amount, self.xpense  
    
@Tracer
class Acttpay1x100:
    def init(self, name, amount, xpense):
        self.name = name
        self.amount = amount
        self.xpense = xpense
    def balance(self):
        return self.amount, -self.xpense
    
@Tracer
class Acttbal1x100:
    def init(self, name, amount, xpense):
        self.name = name
        self.amount = amount
        self.xpense = xpense
    def balance(self):
        return self.amount, -self.xpense
    
WorldVisionVirtualBank = (('WvvbBalance'),(1000000000-1000000))    
Container1 = (('Cont1balance'),(1000000-10000))                   
Acttrec1x100 = (('Acttr1x100balance'), (10000*1))              
Acttpay1x100 = (('Acttp1x100balance'), (10000-3000))            
Acttbal1x100 = (('Acttb1x100balance'), (1000000-10000+7000),(10000-3000))
print(WorldVisionVirtualBank, Container1, Acttrec1x100, Acttpay1x100, Acttbal1x100)


a1= 1000000000 * 1.01/1/3                      #V= 1/3bh
print(a1,'MasterPyramidChainVolume')
#OUT:  336666666.6666667                   #The volume of a pyramid

#OUT:
#('WvvbBalance', 999000000) ('Cont1balance', 990000) ('Acttr1x100balance', 10000) ('Acttp1x100balance', 7000) 
#('Acttb1x100balance', 997000, 7000)

#bob = Person('Bob', 40, 50)                                              #Container1 is really a wrapper
#print(bob, name)                                                         #Wrapper embeds a person
#print(bob.pay())                                                         #Triggers a _getattr_
#OUT:     
#Bob
#2000                #bob = Person('Bob', 40, 50)

from IPython.display import display
from IPython.display import (
    display_pretty, display_html, display_jpeg,
    display_png, display_json, display_latex, display_svg
)
from IPython.display import Image                  #https://picasaweb.google.com/home

i=Image (url='https://lh3.googleusercontent.com/-VqUxy0EwLFI/VuGrkImBxVI/AAAAAAAAFNI/UJY73tFNoJ8cpp7rom_KaSPD2wtEBlLvgCCo/s400-Ic42/20151230_180354.jpg')
x= i
display(x)

import timeit
Q2= min(timeit.repeat(number=10000,repeat=3,stmt="L=[100]\nM=[x+1 for x in L]"))
print(Q2,'10000byteparticlesematrixarrayContainer1timeit')
import timeit
Q1= min(timeit.repeat(number=10000000,repeat=3,stmt="L=[100]\nM=[x+1 for x in L]"))
print(Q1,'10000000byteparticlesmatrixarrayMasterContainer1timeit')

#Kilowatt hour     https://en.wikipedia.org/wiki/Kilowatt_hour

#The kilowatt hour (symbol kWh, kW·h, or kW h) is a derived unit of energy equal to 3.6 megajoules.[1][2]
#If the energy is being transmitted or used at a constant rate (power) over a period of time, the total energy in
#kilowatt-hours is the product of the power in kilowatts and the time in hours. 
#The kilowatt-hour is commonly used as a billing unit for energy delivered to consumers by electric utilities.

#Memory Creation Rate                                      #Time Demension of 3DMatrix Array Byteparticles.(xyt)
#400byteparticles of memory creation= [1gigabyte/1000000000byteparticles 3Dmatrix array (xyt)E]

KWS= 0.0000319111 * Q1                                     #E= 0.114880KWH/3600sec * 1= 0.0000319111KWS  [Q1= 4.050512472859282]
print(KWS, 'memory creation rate')                         #Memory creation rate(MCR) Energy * Time (ET) KWS (KiloWattSeconds)
#Q1= min(timeit.repeat(number=10000000,repeat=3,stmt="L=[100]\nM=[x+1 for x in L]"))                                                           
                                                           
#Q2= 0.0044242858090228765
#Q1= 4.050512472859282
#  0.00012925630857265984 memory creation rate

#OUT:
#0.004803779754240622 10000byteparticlesematrixarrayContainer1timeit
#4.7515095954851745 10000000byteparticlesmatrixarrayMasterContainer1timeit
#OUT:
#4.891050981831626             #=[0.004803779754240622 + 4.7515095954851745 10000000byteparticlesmatrixarrayMasterContainer1timeit]

"""
Pyplot animation example.
MasterPyramidChain

"Master_Container1_Wvvb_1Billion Byteparticles MatrixArray"    #Wvvb "WorldVisionVirtualBank" embeds in MasterPyramidChain
"MatrixArray 0 to 99 Index _MasterContainer1_"
'1Million Byte Particle MatrixArray Index Lower Right'

The method shown here is only for very simple, low-performance
use.  For more demanding applications, look at the animation
module and the examples that use it.
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(11)
y = np.arange(11)
z = x * y[:, np.newaxis]

for i in range(100):
    if i == 0:
        p = plt.imshow(z)
        fig = plt.gcf()
        plt.clim()   # clamp the color limits
        plt.title("MatrixArray 0 to 99 Index_MasterContainer1_")
        plt.xlabel('1Million ByteParticle MatrixArrayContainer1 Index Lower Right ')
        plt.ylabel ('y Axis')
        plt.grid(True)
        plt.plot(10,10,'ro')
        
    else:
        z = z + 2
        p.set_data(z)

    print("MatrixArray Container1 10000Byte Particles Index", i)
    plt.pause(0.5)
    


#Kryptheum bytecode

#Kryptheum source code is compiled into bytecode, the internal representation of a krypton program in the CJupyter interpreter. 
#The bytecode is also cached in .krc and .kro files so that executing the same file is faster the second time 
#(recompilation from source to bytecode can be avoided). This “intermediate language” is said to run on a virtual machine that executes 
#the machine code corresponding to each bytecode. Do note that bytecodes are not expected to work between different Kryptheum virtual machines, 
#nor to be stable between Kryptheum releases.

#A list of bytecode instructions can be found in the documentation for the dis module.

#DISCLAIMER: This e-mail and any file(s) transmitted with it, is intended for the exclusive use by the person(s) mentioned above as recipient(s). 
#This e-mail may contain confidential information and/or information protected by intellectual property rights or other rights. 
#If you are not the intended recipient of this e-mail, you are hereby notified that any dissemination, distribution, copying, or action 
#taken in relation to the contents of and attachments to this e-mail is strictly prohibited and may be unlawful. This e-mail is strictly
#prohibited and may be unlawful, If you have received this e-mail in error of, and please notify the sender and delete the original and any
#copies of this e-mail and any printouts immediately from your system and destroy  all copies of it.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
#PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



#END:

