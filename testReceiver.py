import  unittest
from Receiver import *

#Creating sender data for test
def setup_senderdata(): 
   testFileName = 'SenderData.txt'
   with open(testFileName,'r') as viewFileOpen:
       consoleoutput = viewFileOpen.read().splitlines()
   return consoleoutput


class BMS_Receiver(unittest.TestCase):
  def test_senderOutputRead_forReceiver(self):
    self.assertEqual(setup_senderdata(),['----------Temperature Sensor data----------', '19', '29', '7', '34', '40', '35', '22', '25', '20', '22', '----------SOC Sensor data----------', '34', '59', '49', '37', '27', '34', '62', '44', '77', '21'])
  
  def test_ConvertSenderConsoleoutput_forStatistics(self): 
    input_stream = setup_senderdata() 
    self.assertEqual(ReadBatteryParameterReadingFromSender(input_stream),(([19, 29, 7, 34, 40, 35, 22, 25, 20, 22], [34, 59, 49, 37, 27, 34, 62, 44, 77, 21]), [['----------Temperature Sensor data----------'], ['----------SOC Sensor data----------']]))
    self.assertNotEqual(ReadBatteryParameterReadingFromSender(input_stream),(([19, 29, 7, 34, 40, 35, 22, 25, 20, 0], [34, 59, 49, 37, 27, 34, 62, 44, 77, 0]), [['----------Temperature Sensor data----------'], ['----------SOC Sensor data----------']]))


  def test_SeparateEachSensorReadings(self):  
    input_stream = setup_senderdata() 
    self.assertEqual(StrippedReadingFromConsole(input_stream),[['----------Temperature Sensor data----------'], ['19'], ['29'], ['7'], ['34'], ['40'], ['35'], ['22'], ['25'], ['20'], ['22'], ['----------SOC Sensor data----------'], ['34'], ['59'], ['49'], ['37'], ['27'], ['34'], ['62'], ['44'], ['77'], ['21']])
    self.assertNotEqual(StrippedReadingFromConsole(input_stream),[['----------Temperature Sensor data----------'], ['19'], ['29'], ['7'], ['34'], ['40'], ['35'], ['22'], ['25'], ['20'], ['0'], ['----------SOC Sensor data----------'], ['34'], ['59'], ['49'], ['37'], ['27'], ['34'], ['62'], ['44'], ['77'], ['0']])
    
  def test_getSensorReadings_from_StrippedConsoleOutput(self):
    strippedData = [['----------Temperature Sensor data----------'], ['19'], ['29'], ['7'], ['34'], ['40'], ['35'], ['22'], ['25'], ['20'], ['22'], ['----------SOC Sensor data----------'], ['34'], ['59'], ['49'], ['37'], ['27'], ['34'], ['62'], ['44'], ['77'], ['21']]
    self.assertTrue(getSensorReadings(strippedData)[0]==[19, 29, 7, 34, 40, 35, 22, 25, 20 , 22])
    self.assertTrue(getSensorReadings(strippedData)[1]==[34, 59, 49, 37, 27, 34, 62, 44, 77, 21])
   
  def test_ConvertString_to_NumArray(self):
    self.assertTrue(ConverttoNumArray([['19'], ['29'], ['7'], ['34'], ['40'], ['35'], ['22'], ['25'], ['20'], ['22']])==[19, 29, 7, 34, 40, 35, 22, 25, 20, 22])
    self.assertTrue(ConverttoNumArray([['34'], ['59'], ['49'], ['37'], ['27'], ['34'], ['62'], ['44'], ['77'], ['21']])==[34, 59, 49, 37, 27, 34, 62, 44, 77, 21])
  
  def test_getMinMaxReading(self):
    self.assertTrue(getMinMax_Value([19, 29, 7, 34, 40, 35, 22, 25, 20, 22])==(7,40))
    self.assertTrue(getMinMax_Value([34, 59, 49, 37, 27, 34, 62, 44, 77, 21])==(21,77))
    self.assertTrue(getMinMax_Value([19, 29, 7, 0, 40, 35, 22, 44, 20, 22])==(0,44))
    self.assertTrue(getMinMax_Value([80, 59, 49, 37, 27, 34, 62, 44, 7, 21])==(7,80))

  def test_getMovingAverage_withVaryingWindowsize(self):
    self.assertTrue(getMovingAverage([19, 29, 7, 34, 40, 35, 22, 25, 20, 22],5)==24.8)
    self.assertTrue(getMovingAverage([34, 59, 49, 37, 27, 34, 62, 44, 77, 21],5)==47.6)
    self.assertEqual(getMovingAverage([19, 29, 7, 34, 40, 35, 22, 25, 20, 22],3),22.33)
    self.assertEqual(getMovingAverage([34, 59, 49, 37, 27, 34, 62, 44, 77, 21],7),43.14)

  def test_ComputeReceiverStatistics(self):
    self.assertTrue(ComputeStatistics([19, 29, 7, 34, 40, 35, 22, 25, 20, 22])==((7,40),24.8))
    self.assertTrue(ComputeStatistics([34, 59, 49, 37, 27, 34, 62, 44, 77, 21])==((21,77),47.6))
    self.assertFalse(ComputeStatistics([19, 29, 7, 0, 40, 35, 22, 44, 20, 22])==((7,40),24.8))
    self.assertFalse(ComputeStatistics([80, 59, 49, 37, 27, 34, 62, 44, 7, 21])==((21,77),47.6))

  def test_ReceiverOutput(self):
    ParameterList = ([[19, 29, 7, 34, 40, 35, 22, 25, 20, 22],[34, 59, 49, 37, 27, 34, 62, 44, 77, 21]],[['----------Temperature Sensor data----------'],['----------SOC Sensor data----------']]) 
    self.assertEqual(ReceiverOutput(ParameterList), '----------Temperature Sensor data----------\n Mininum Reading :7\n Maximum Reading :40\n Moving Average :24.8\n----------SOC Sensor data----------\n Mininum Reading :21\n Maximum Reading :77\n Moving Average :47.6\n')


if __name__ == "__main__":  #pragma no cover
    unittest.main()