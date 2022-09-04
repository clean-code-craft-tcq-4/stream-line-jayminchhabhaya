#include <assert.h>
#include <iostream>
#include "checker.hpp"
using namespace std;
using namespace BatteryStatus;

void printoutputtocommunicate(float ParametersofBattery){
       std::cout << ParametersofBattery << ",";
}
bool ChecksStatus(int min,int max,float value){
	if(value < min || value > max) {
    return false;
	}
	return true;
}
bool Battery::batteryIsOk(float ParametersofBatteryStatus) {
	for (const auto& funptr : functptr) {
      if(!funptr(ParametersofBatteryStatus))
	  {
		return false;
	  }
    }
	printoutputtocommunicate(ParametersofBatteryStatus);
	return true;
}
bool Battery::batteryTemperatureIsOk(float temperature){
	return ChecksStatus(MINTEMPERATURE,MAXTEMPERATURE,temperature);
}
bool Battery::batterysocIsOk(float soc){
	 return ChecksStatus(MINSOC,MAXSOC,soc);
}



