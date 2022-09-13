#include <assert.h>
#include <iostream>
#include "checker.hpp"
using namespace std;
using namespace BatteryStatus;

bool Battery::printoutputtocommunicate(){
	if(temperaturedata.empty() || socdata.empty())
	{
		return false;
	}
	else
	{
		std::cout << "----------Temperature Sensor data----------" <<std::endl;
		for (const int& i : temperaturedata) {
        std::cout << i <<std::endl;
        }
		std::cout << "----------Soc Sensor data----------" <<std::endl;
		for (const int& i : socdata) {
        std::cout << i <<std::endl;
        }
		return true;
	}
}
bool ChecksStatus(int min,int max,float value){
	if(value < min || value > max) {
    return false;
	}
	return true;
}
bool Battery::batteryIsOk(float ParametersofBatteryStatus,int BatteryParameterStatus) {
      if(functptr[BatteryParameterStatus](ParametersofBatteryStatus))
	  {
		  if(BatteryParameterStatus){
		     socdata.push_back(ParametersofBatteryStatus);  
		  }
		  else{
		   	temperaturedata.push_back(ParametersofBatteryStatus);  
		  }
	  }
	  return true;
}
bool Battery::batteryTemperatureIsOk(float temperature){
	return ChecksStatus(MINTEMPERATURE,MAXTEMPERATURE,temperature);
}
bool Battery::batterysocIsOk(float soc){
	 return ChecksStatus(MINSOC,MAXSOC,soc);
}



