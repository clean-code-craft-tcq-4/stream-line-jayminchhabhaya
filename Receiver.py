import sys
from itertools import chain

Parameter1_ConsolePrint =['----------Temperature Sensor data----------']
Parameter2_ConsolePrint =['----------Soc Sensor data----------']

def ReadBatteryParameterReadingFromSender(LinesRead):
    StrippedData = StrippedReadingFromConsole(LinesRead)
    return getSensorReadings(StrippedData)

def StrippedReadingFromConsole(LinesRead):
    StrippedData = []
    for Reading in LinesRead:  
      ReadingList = list(Reading.split(','))
      StrippedData.append(ReadingList)
    return StrippedData

def getSensorReadings(Reading):
    # use output string to split 2 parameter readings
    Split_Parameter1Readings = Reading[Reading.index(Parameter1_ConsolePrint)+1:Reading.index(Parameter2_ConsolePrint)] 
    Split_Parameter2Readings = Reading[Reading.index(Parameter2_ConsolePrint)+1:]
    Parameter1Readings = ConverttoNumArray(Split_Parameter1Readings) 
    Parameter2Readings = ConverttoNumArray(Split_Parameter2Readings) 
    return Parameter1Readings , Parameter2Readings

def ConverttoNumArray(ParameterReadings):
    Parameter_Combinedlist = list(chain(*ParameterReadings))
    Parameter_NumArray = [int(i) for i in Parameter_Combinedlist]
    return Parameter_NumArray

def getMinMax_Value(ParameterReading):
    MinMaxReading =  min(ParameterReading), max(ParameterReading) 
    return MinMaxReading

def getMovingAverage(ParamterReading, window_size) :
    window = ParamterReading[-window_size:]
    movingAverage = round((sum(window)/window_size),2)
    return movingAverage

def ComputeStatistics(ParameterList):
    MinMaxReading = getMinMax_Value(ParameterList)
    movingAverage = getMovingAverage(ParameterList,window_size = 5)
    return MinMaxReading , movingAverage

def ReceiverOutput(ParameterList) :
    for message in range(0,len(ParameterList[1])):
      print(ParameterList[1][message])
      print(' Mininum Reading :', ComputeStatistics(ParameterList[0][message])[0][0], '\n', 'Maximum Reading :', ComputeStatistics(ParameterList[0][message])[0][1])
      print(' Moving Average :',ComputeStatistics(ParameterList[0][message])[1])

if __name__ == "__main__":  #pragma no cover
   SensorOutput = sys.stdin.read().splitlines()
   Paramter1Reading , Parameter2Reading = ReadBatteryParameterReadingFromSender(SensorOutput)
   ParameterList = [Paramter1Reading , Parameter2Reading ] ,[Parameter1_ConsolePrint,Parameter2_ConsolePrint]
   ReceiverOutput(ParameterList)