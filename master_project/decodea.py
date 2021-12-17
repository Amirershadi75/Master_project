#!/usr/bin/python
import sys, getopt
import struct
import math

def PIC_CONVERSION_FloatPicToFloatIEEE(picfloat):
  # Microchip sign bit; in bit 23
  bitSign = picfloat[2] & 0x80
  
  IEEEfloat = []
  for i in range (0, 4):
      IEEEfloat.append(0)
  # copy bit 0 - 1
  IEEEfloat[0] = picfloat[0]
  IEEEfloat[1] = picfloat[1]
  # clear bit 23
  IEEEfloat[2] = picfloat[2] & ~0x80
  # if bit 24 is set, set bit 23
  if picfloat[3] & 0x01:
    IEEEfloat[2] = IEEEfloat[2] | 0x80
  # shift bits 24-31 one right
  IEEEfloat[3] = picfloat[3] >> 1;
  
  # set bit 31 as sign bit
  IEEEfloat[3] = IEEEfloat[3] | bitSign;

  concat = (IEEEfloat[3]<<24) | (IEEEfloat[2]<<16) | (IEEEfloat[1]<<8) | (IEEEfloat[0])
  concat_asbyte = struct.pack('I', concat)
  concatasfloat = struct.unpack('f', concat_asbyte)[0]
 
  return concatasfloat
  
# float PIC_CONVERSION_FloatPicToFloatIEEE (float pic)
# {
# uint8_t* ptrData = (uint8_t*)&pic;
# uint8_t  bitSign;
# // Microchip sign bit; in bit 23
# bitSign = ptrData[2] & 0x80;
# // clear bit 23
# ptrData[2] &= ~0x80;
# // if bit 24 is set, set bit 23
# if(ptrData[3] & 0x01)
# {
  # ptrData[2] |= 0x80;
# }
# // shift bits 24-31 one right
# ptrData[3] >>= 1;
# // set bit 31 as sign bit
# ptrData[3] |= bitSign;
# return pic;
# }

def meanValue( sum,  n):
  return sum / float(n)

def stdErrorOfMean(n, sum, sq_sum):
  return math.sqrt((sq_sum - (sum*sum) / float(n)) /(float(n) * (float(n-1))))
  
from tkinter import filedialog
from tkinter import *
Tk().withdraw()
def main(rawdata):
  argv=[]
  inputfile = ''
  outputfile = ''
  try:
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
    print('test.py -i <inputfile> -o <outputfile>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
       print('test.py -i <inputfile> -o <outputfile>')
       sys.exit()
    elif opt in ("-i", "--ifile"):
       inputfile = arg
    elif opt in ("-o", "--ofile"):
       outputfile = arg
  print('Input file is "', inputfile)
  print('Output file is "', outputfile)

  #select input file when not given
  if inputfile == "":
    inputfile = rawdata
    outputfile = inputfile
  
  # if outputfile != "":
  #   filename = outputfile + ".inc";
  #   fout = open(filename, "a");
  #   fout.write("Inclination data generated from \""+inputfile+"\" \ntimestamp;depth;inclination;azimuth;\n");
  #   fout.close();
    
  readFromFile(inputfile, outputfile)
  
  
class LoggerData:
  def __init__(self, pack):
    self.timeStamp = pack.timeStamp
    self.housekeeping = {}
    tmp = pack.housekeeping.split(';')
    if int(tmp[0])== 2:
      #print(float(tmp[1]))
      self.housekeeping['system_24V'] = float(tmp[1])
      self.housekeeping['system_12V'] = float(tmp[2])
      self.housekeeping['system_5V'] = float(tmp[3])
      self.housekeeping['system_3V'] = float(tmp[4])
      self.housekeeping['system_temp'] = float(tmp[5])
      self.housekeeping['vbus'] = float(tmp[6])
      self.housekeeping['ground_contact'] = int(tmp[7])
      
    self.encoder = {}  
    tmp = pack.encoder.split(';')
    if int(tmp[0]) == 201:
      self.encoder['time'] = tmp[1]
      self.encoder['depth'] = tmp[2]
      self.encoder['velocity'] = tmp[3]
      self.encoder['acceleration'] = tmp[4]
    
    self.acc = []
    for i in range (0, 9):
      self.acc.append([])
      for j in range (0, 3):
        self.acc[i].append({})
        
        self.acc[i][j]['x'] = {}
        if bool(pack.acc[i][j]['x']):
          self.acc[i][j]['x']['mean'] = meanValue(pack.acc[i][j]['x']['sum'], pack.acc[i][j]['x']['n']) / 4096.
          self.acc[i][j]['x']['sig'] = stdErrorOfMean(pack.acc[i][j]['x']['n'], pack.acc[i][j]['x']['sum'], pack.acc[i][j]['x']['sq_sum']) / 4096.
                
        if bool(pack.acc[i][j]['y']):
          self.acc[i][j]['y'] = {}
          self.acc[i][j]['y']['mean'] = meanValue(pack.acc[i][j]['y']['sum'], pack.acc[i][j]['y']['n']) / 4096.
          self.acc[i][j]['y']['sig'] = stdErrorOfMean(pack.acc[i][j]['y']['n'], pack.acc[i][j]['y']['sum'], pack.acc[i][j]['y']['sq_sum'])  / 4096.
        
        if bool(pack.acc[i][j]['z']):
          self.acc[i][j]['z'] = {}
          self.acc[i][j]['z']['mean'] = meanValue(pack.acc[i][j]['z']['sum'], pack.acc[i][j]['z']['n']) / 4096.
          self.acc[i][j]['z']['sig'] = stdErrorOfMean(pack.acc[i][j]['z']['n'], pack.acc[i][j]['z']['sum'], pack.acc[i][j]['z']['sq_sum'])  / 4096.
            
    self.compass = {}
    self.compass['x'] = pack.compass['x']['sum']
    self.compass['y'] = pack.compass['y']['sum']
    self.compass['z'] = pack.compass['z']['sum']
    self.compass['Hr'] = pack.compass['Hr']['sum']
        
    self.giro = {}
    self.giro['x'] = {}
    self.giro['x']['mean'] = meanValue(pack.giro['x']['sum'], pack.giro['x']['n'])
    self.giro['x']['sig'] = stdErrorOfMean(pack.giro['x']['n'], pack.giro['x']['sum'], pack.giro['x']['sq_sum'])
    
    self.giro['y'] = {}
    self.giro['y']['mean'] = meanValue(pack.giro['y']['sum'], pack.giro['y']['n'])
    self.giro['y']['sig'] = stdErrorOfMean(pack.giro['y']['n'], pack.giro['y']['sum'], pack.giro['y']['sq_sum'])
    
    self.giro['z'] = {}
    self.giro['z']['mean'] = meanValue(pack.giro['z']['sum'], pack.giro['z']['n'])
    self.giro['z']['sig'] = stdErrorOfMean(pack.giro['z']['n'], pack.giro['z']['sum'], pack.giro['z']['sq_sum'])
        
    self.pressure = [];
    for i in range (0, 2):
      self.pressure.append([])
      for j in range (0, 3):
        self.pressure[i].append({})
        
    for i in range (0, 2):
      for j in range (0, 3):
        self.pressure[i][j]['n'] = pack.pressure[i][j]['n']
        self.pressure[i][j]['sum'] = pack.pressure[i][j]['sum']
        self.pressure[i][j]['sq_sum'] = pack.pressure[i][j]['sq_sum']
        
    
        
  def __str__(self):
    returnstr = ""
    returnstr +=  "TimeStamp: " + str(self.timeStamp) +\
                  "\nSystem_24V:      " + str(self.housekeeping['system_24V']) +\
                  "\nSystem_12V:      " + str(self.housekeeping['system_12V']) +\
                  "\nSystem_5V:       " + str(self.housekeeping['system_5V']) +\
                  "\nSystem_3V:       " + str(self.housekeeping['system_3V']) +\
                  "\nSystem_temp:     " + str(self.housekeeping['system_temp']) +\
                  "\nSystem_vbus:     " + str(self.housekeeping['vbus']) +\
                  "\nSystem_ground:   " + str(self.housekeeping['ground_contact']) +\
                  "\nEncoder:" +\
                  "\n   Time:         " + str(self.encoder['time']) +\
                  "\n   Depth:        " + str(self.encoder['depth']) +\
                  "\n   Velocity:     " + str(self.encoder['velocity']) +\
                  "\n   Acceleration: " + str(self.encoder['acceleration']) +\
                  "\nPressure:" +\
                  "\n   top:          " + str(self.pressure[0]) +\
                  "\n   bottom:       " + str(self.pressure[1]) +\
                  "\nCompass:" +\
                  "\n   x:            " + str(self.compass['x']) +\
                  "\n   y:            " + str(self.compass['y']) +\
                  "\n   z:            " + str(self.compass['z']) +\
                  "\n   Hr:           " + str(self.compass['Hr']) +\
                  "\nGiro:" +\
                  "\n   x:            " + str(self.giro['x']) +\
                  "\n   y:            " + str(self.giro['y']) +\
                  "\n   z:            " + str(self.giro['z']) +\
                  "\nAccelerometer:"
    for i in range(0, 9):
      for j in range(0, 3):
        if (bool(self.acc[i][j]['x']) and bool(self.acc[i][j]['y']) and bool(self.acc[i][j]['z'])):
          returnstr += "\n" + str(i+1) + str(j+1) + ": x = " +   str(self.acc[i][j]['x']) +\
                       "\n    y = " + str(self.acc[i][j]['y']) +\
                       "\n    z = " + str(self.acc[i][j]['z']) + '\n'
    return returnstr     

  def write2file(self, filename):
    fout = open(filename, "a")

    fout.write(str(self.timeStamp) + ';')
    fout.write(str(self.encoder['time']) + ';')
    fout.write(str(self.encoder['depth']) + ';')
    fout.write(str(self.encoder['velocity']) + ';')
    fout.write(str(self.encoder['acceleration']) + ';')
    
    fout.write(str(self.compass['x']) + ";")
    fout.write(str(self.compass['y']) + ";")
    fout.write(str(self.compass['z']) + ";")
    fout.write(str(self.compass['Hr']) + ";")
    
    fout.write(str(self.giro['x']['mean']) + ";" + str(self.giro['x']['sig']) + ";")
    fout.write(str(self.giro['y']['mean']) + ";" + str(self.giro['y']['sig']) + ";")
    fout.write(str(self.giro['z']['mean']) + ";" + str(self.giro['z']['sig']) + ";")
    
    for i in range(0, 2):     
      fout.write(str(self.pressure[i]) + ";")
    
    for i in range(0, 9):
      for j in range(0, 3):
        if (bool(self.acc[i][j]['x']) and bool(self.acc[i][j]['y']) and bool(self.acc[i][j]['z'])):
          fout.write("[" + str(self.acc[i][j]['x']) + ";" + str(self.acc[i][j]['y']) + ";" + str(self.acc[i][j]['z']) + "];")
        
    
    
    fout.write(str(self.giro) + ";")
    

    fout.write('\n')
    fout.close()
  


class LoggerPackage:
  def __init__(self, packCount):
    self.packCount = packCount
    self.timeStamp = 0
    self.housekeeping = ""
    self.encoder = ""
    self.acc = []
    for i in range (0, 9):
      self.acc.append([])
      for j in range (0, 3):
        self.acc[i].append({})
        
        self.acc[i][j]['x'] = {}
        self.acc[i][j]['y'] = {}
        self.acc[i][j]['z'] = {}
            
    self.compass = {}
    self.compass['x'] = {}
    self.compass['y'] = {}
    self.compass['z'] = {}
    self.compass['Hr'] = {}
        
    self.giro = {}
    self.giro['x'] = {}
    self.giro['y'] = {}
    self.giro['z'] = {}
        
    self.pressure = [];
    for i in range (0, 2):
      self.pressure.append([])
      for j in range (0, 3):
        self.pressure[i].append({})
        

        
  def __str__(self):
    returnstr = ""
    returnstr += "Packege: " + str(self.packCount) + "\ntimeStamp: " +\
                 str(self.timeStamp) + "\nSystem: " + \
                 str(self.housekeeping) + "\nEncoder: " +\
                 str(self.encoder) + "\nAccelerometer:"
                 
    for i in range(0, 9):
      returnstr += "\n" + str(i+1) + "1: x = " + str(self.acc[i][0]['x']) + "\n    y = " + str(self.acc[i][0]['y']) + "\n    z = " + str(self.acc[i][0]['z']) +\
                   "\n" + str(i+1) + "2: x = " +   str(self.acc[i][1]['x']) + "\n    y = " + str(self.acc[i][1]['y']) + "\n    z = " + str(self.acc[i][1]['z']) +\
                   "\n" + str(i+1) + "3: x = " +   str(self.acc[i][2]['x']) + "\n    y = " + str(self.acc[i][2]['y']) + "\n    z = " + str(self.acc[i][2]['z'])

    returnstr += "\n\nCompass: x = " + str(self.compass['x']) +\
               "\n         y = " + str(self.compass['y']) +\
               "\n         z = " + str(self.compass['z']) +\
               "\n         Hr = " + str(self.compass['Hr']) +\
               "\nGiro: " + str(self.giro['x']) +\
               "\n      " + str(self.giro['y']) +\
               "\n      " + str(self.giro['z']) +\
               "\nPressure: \n 1: " + str(self.pressure[0]) +\
               "\n 2: " + str(self.pressure[1])
           
    return returnstr
           
  def write2file(self, filename):
    fout = open(filename, "a")

    fout.write(str(self.timeStamp) + ';')
    fout.write(str(self.housekeeping))
    fout.write(str(self.encoder))
    fout.write(str(self.compass) + ";")    
    fout.write(str(self.giro) + ";")    
    for i in range(0, 2):     
      fout.write(str(self.pressure[i]) + ";")
      
    for i in range(0, 9):
      for j in range(0, 3):
        fout.write("[" + str(self.acc[i][j]['x']) + ";" + str(self.acc[i][j]['y']) + ";" + str(self.acc[i][j]['z']) + "];")

    fout.write('\n')
    fout.close()
    
 
def getInclination(data):
    try:
        vectorLenght = math.sqrt(data.acc[8][1]['x']['mean']*data.acc[8][1]['x']['mean'] + data.acc[8][1]['y']['mean']*data.acc[8][1]['y']['mean'] + data.acc[8][1]['z']['mean']*data.acc[8][1]['z']['mean'])
        inclination = math.acos(data.acc[8][1]['z']['mean'] / vectorLenght)
        azimuth = math.atan2(data.acc[8][1]['y']['mean'], data.acc[8][1]['x']['mean'])  
        return [data.timeStamp, data.encoder['depth'], math.degrees(inclination), math.degrees(azimuth)]

    except:
        pass

def writeArray2file(array, filename):
    fout = open(filename, "a")

    for i in range(len(array)):     
      fout.write(str(array[i]) + ";")

    fout.write('\n')
    fout.close()

 
def processPackage(pack, packCount, outputfile):
  #print(pack)
  #print("\nValid Package: " + str(packCount) + "\n\n")
   
  data = LoggerData(pack);
  
  inclinationData = getInclination(data);
  
  if outputfile != "":
    pack.write2file('test'+".raw");
    # pack.write2file(outputfile+".raw");
    # data.write2file(outputfile+".conv");
    # writeArray2file(inclinationData, outputfile+".inc")
  
  #print(data)
  

    
  
def readFromFile(inputfile, outputfile):
  #init counters
  packCount = 0  

  with open(inputfile, "rb") as f:
    byte = f.read(1)
    while byte:
      if byte == b'$':
        # New Data
        packCount = packCount + 1
        pack = LoggerPackage(packCount)
        # skip 2 bytes
        byte = f.read(1)
        byte = f.read(1)
        # timeStamp length 17 bytes utf-8
        pack.timeStamp = int(f.read(17).decode('utf-8'))
        # skip 2 bytes
        byte = f.read(1)
        byte = f.read(1)
        # read housekeeping
        byte = f.read(1)
        while byte != b'\r' :
            pack.housekeeping += byte.decode('utf-8')
            byte = f.read(1)
        byte = f.read(1)
        # read encoder
        byte = f.read(1)
        while byte != b'\r' :
            pack.encoder += byte.decode('utf-8')
            byte = f.read(1)
        byte = f.read(1)
        
        #begin Binary            
        byte = f.read(1)
        inpack = 1;
        while inpack:
          escapeByte = byte;
          if escapeByte == b'\r':
            byte = f.read(1)
            byte = f.read(1)
            if byte == b'#':
              processPackage(pack, packCount, outputfile)
              inpack = 0;
          else:
            byte = f.read(1)
            address = byte[0]
            #print("Address: " + str(address))
            byte = f.read(1)
            status = byte[0]
            #print("Status: "+ str(status))
            if escapeByte == b'A':
              if address < 90 or address == 92:
                pack.acc[int(address/10)-1][address%10-1]['x']['n'] = f.read(1)[0]
                pack.acc[int(address/10)-1][address%10-1]['x']['sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
                pack.acc[int(address/10)-1][address%10-1]['x']['sq_sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
                
                pack.acc[int(address/10)-1][address%10-1]['y']['n'] = f.read(1)[0]
                pack.acc[int(address/10)-1][address%10-1]['y']['sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
                pack.acc[int(address/10)-1][address%10-1]['y']['sq_sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
                
                pack.acc[int(address/10)-1][address%10-1]['z']['n'] = f.read(1)[0]
                pack.acc[int(address/10)-1][address%10-1]['z']['sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
                pack.acc[int(address/10)-1][address%10-1]['z']['sq_sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
                  
            elif escapeByte == b'G':              
              pack.giro['x']['n'] = f.read(1)[0]
              pack.giro['x']['sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
              pack.giro['x']['sq_sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
              
              pack.giro['y']['n'] = f.read(1)[0]
              pack.giro['y']['sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
              pack.giro['y']['sq_sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
              
              pack.giro['z']['n'] = f.read(1)[0]
              pack.giro['z']['sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
              pack.giro['z']['sq_sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
              
              pack.compass['x']['n'] = f.read(1)[0]
              pack.compass['x']['sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
              pack.compass['x']['sq_sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
              
              pack.compass['y']['n'] = f.read(1)[0]
              pack.compass['y']['sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
              pack.compass['y']['sq_sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
              
              pack.compass['z']['n'] = f.read(1)[0]
              pack.compass['z']['sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
              pack.compass['z']['sq_sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))

              pack.compass['Hr']['n'] = f.read(1)[0]
              pack.compass['Hr']['sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
              pack.compass['Hr']['sq_sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))

            elif escapeByte == b'N':
            
              for i in range (0, 3):
                pack.pressure[int(address/10)-9][i]['n'] = f.read(1)[0]
                pack.pressure[int(address/10)-9][i]['sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
                pack.pressure[int(address/10)-9][i]['sq_sum'] = PIC_CONVERSION_FloatPicToFloatIEEE(f.read(4))
              
            byte = f.read(1)
      byte = f.read(1)
  f.close()
  print("\nSuccessfull read of " + str(packCount) + " valid packages: \n\n")
  
  
  
     

if __name__ == "__main__":
   main(sys.argv[1:])