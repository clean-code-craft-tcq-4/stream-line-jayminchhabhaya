#include <assert.h>
#include <iostream>
#include "Sender.hpp"
using namespace std;
using namespace BatteryStatus;


bool Battery::printoutputtocommunicate(std::vector<float> data, string Parameter){
	if(!data.empty()){
		std::cout <<  "----------" << Parameter << " Sensor data----------" <<std::endl;
		for(unsigned i= 0 ; i<data.size()-1; ++i)
		{
			std::cout << data[i] <<std::endl;
		}
	    return true;
	}
	return false;
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



