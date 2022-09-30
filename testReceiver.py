import  unittest
from Receiver import *

def setup_senderdata():
   testFileName = 'SenderData.txt'
   with open(testFileName,'r') as viewFileOpen:
       consoleoutput = viewFileOpen.read().splitlines()
   return consoleoutput


class BMS_Receiver(unittest.TestCase):
  def test_senderOutputRead(self):
    self.assertEqual(setup_senderdata(),['----------Temperature Sensor data----------', '19', '29', '7', '34', '40', '35', '22', '25', '20', '22', '----------Soc Sensor data----------', '34', '59', '49', '37', '27', '34', '62', '44', '77', '21'])
    
  def test_split_Consoleoutput(self):  
    input_stream = setup_senderdata() 
    self.assertEqual(StrippedReadingFromConsole(input_stream),[['----------Temperature Sensor data----------'], ['19'], ['29'], ['7'], ['34'], ['40'], ['35'], ['22'], ['25'], ['20'], ['22'], ['----------Soc Sensor data----------'], ['34'], ['59'], ['49'], ['37'], ['27'], ['34'], ['62'], ['44'], ['77'], ['21']])
    
  def test_ReadBatteryParameterReadingFromSender(self): 
    input_stream = setup_senderdata() 
    self.assertEqual(ReadBatteryParameterReadingFromSender(input_stream),([19, 29, 7, 34, 40, 35, 22, 25, 20, 22], [34, 59, 49, 37, 27, 34, 62, 44, 77, 21]))
  
  def test_getSensorReadings_from_StrippedConsoleOutput(self):
    strippedData = [['----------Temperature Sensor data----------'], ['19'], ['29'], ['7'], ['34'], ['40'], ['35'], ['22'], ['25'], ['20'], ['22'], ['----------Soc Sensor data----------'], ['34'], ['59'], ['49'], ['37'], ['27'], ['34'], ['62'], ['44'], ['77'], ['21']]
    self.assertTrue(getSensorReadings(strippedData)[0]==[19, 29, 7, 34, 40, 35, 22, 25, 20 , 22])
    self.assertTrue(getSensorReadings(strippedData)[1]==[34, 59, 49, 37, 27, 34, 62, 44, 77, 21])
   
  def test_ConvertString_to_NumArray(self):
    self.assertTrue(ConverttoNumArray([['19'], ['29'], ['7'], ['34'], ['40'], ['35'], ['22'], ['25'], ['20'], ['22']])==[19, 29, 7, 34, 40, 35, 22, 25, 20, 22])
    self.assertTrue(ConverttoNumArray([['34'], ['59'], ['49'], ['37'], ['27'], ['34'], ['62'], ['44'], ['77'], ['21']])==[34, 59, 49, 37, 27, 34, 62, 44, 77, 21])
  
  def test_getMinMaxReading(self):
    self.assertTrue(getMinMax_Value([19, 29, 7, 34, 40, 35, 22, 25, 20, 22])==(7,40))
    self.assertTrue(getMinMax_Value([34, 59, 49, 37, 27, 34, 62, 44, 77, 21])==(21,77))

  def test_getMovingAverage(self):
    self.assertTrue(getMovingAverage([19, 29, 7, 34, 40, 35, 22, 25, 20, 22],5)==24.8)
    self.assertTrue(getMovingAverage([34, 59, 49, 37, 27, 34, 62, 44, 77, 21],5)==47.6)

  def test_ComputeStatistics(self):
    self.assertTrue(ComputeStatistics([19, 29, 7, 34, 40, 35, 22, 25, 20, 22])==((7,40),24.8))
    self.assertTrue(ComputeStatistics([34, 59, 49, 37, 27, 34, 62, 44, 77, 21])==((21,77),47.6))

if __name__ == "__main__":  #pragma no cover
    unittest.main()