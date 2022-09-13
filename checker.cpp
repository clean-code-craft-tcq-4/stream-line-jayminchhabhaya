#include <assert.h>
#include <iostream>
#include "checker.hpp"
using namespace std;
using namespace BatteryStatus;

bool printoutputtocommunicate(std::vector<float>temperaturedata,std::vector<float>socdata){
	if(temperaturedata.size() == 0 || socdata.size() == 0)
	{
		return false;
	}
	else
	{
		std::cout << "----------Temperature Sensor data----------" <<std::endl;
		for(int i= 0 ; i<temperaturedata.size(); ++i)
		{
			std::cout << temperaturedata[i] <<std::endl;
		}
		std::cout << "----------Soc Sensor data----------" <<std::endl;
		for(int i= 0 ; i<socdata.size(); ++i)
		{
			std::cout << socdata[i] <<std::endl;
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



