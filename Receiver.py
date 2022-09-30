import sys
from itertools import chain

Parameter1_ConsolePrint =['----------Temperature Sensor data----------']
Parameter2_ConsolePrint =['----------SOC Sensor data----------']

def ReadBatteryParameterReadingFromSender(LinesRead):
    StrippedData = StrippedReadingFromConsole(LinesRead)
    ParameterList = getSensorReadings(StrippedData),[Parameter1_ConsolePrint,Parameter2_ConsolePrint]
    return ParameterList

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
    ReceiverOutput = ''
    for message in range(0,len(ParameterList[1])):
      ParamterName = ''.join(ParameterList[1][message])
      MinimumReading = ComputeStatistics(ParameterList[0][message])[0][0]
      MaximumReading =  ComputeStatistics(ParameterList[0][message])[0][1]
      MovingAverage = ComputeStatistics(ParameterList[0][message])[1]
      ReceiverOutput += ("{0}\n{1}{2}\n{3}{4}\n{5}{6}\n".format(ParamterName, ' Mininum Reading :', MinimumReading, ' Maximum Reading :', MaximumReading, ' Moving Average :',MovingAverage))
    print(ReceiverOutput)
    return ReceiverOutput

if __name__ == "__main__":  #pragma no cover
   SensorOutput = sys.stdin.read().splitlines()
   ParameterList = ReadBatteryParameterReadingFromSender(SensorOutput)
   ReceiverOutput(ParameterList)