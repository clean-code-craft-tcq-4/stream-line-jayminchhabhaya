#include <assert.h>
#include <iostream>
#include "checker.hpp"
using namespace std;
using namespace BatteryStatus;

void printoutputtocommunicate(std::vector<float>ParametersofBattery){
	 for (int Parameters : ParametersofBattery) {
        std::cout << Parameters << ", ";
    }
	std::cout <<'\n';
}
bool ChecksStatus(int min,int max,float value){
	if(value < min || value > max) {
    return false;
	}
	return true;
}
bool Battery::batteryIsOk(std::vector<float>ParametersofBatteryStatus) {
	int i = 0;
	for (const auto& funptr : functptr) {
      if(!funptr(ParametersofBatteryStatus[i++]))
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



