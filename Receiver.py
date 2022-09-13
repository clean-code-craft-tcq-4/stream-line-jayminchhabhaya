import sys

BatteryParameters = ["----------Temperature Sensor data----------", "----------Soc Sensor data----------"]

def ReadBatteryParameterDataFromConsole():
    LinesRead = sys.stdin.readlines()
    StrippedData = []
    for Reading in LinesRead:
      Reading = Reading.strip('\n')
      ReadingList = list(map(float,Reading.split(',')))
      StrippedData.append(ReadingList)
    print(StrippedData)
    return StrippedData