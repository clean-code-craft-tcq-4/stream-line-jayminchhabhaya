#include <assert.h>
#include <iostream>
#include "checker.hpp"
using namespace std;
using namespace BatteryStatus;
void printError(std::string str){
	cout<<str << " out of range! "<<endl;
}
void printoutputtocommunicate(std::vector<float>ParametersofBattery){
	 for (int Parameters : ParametersofBattery) {
        std::cout << Parameters << ", ";
    }
}
bool ChecksStatus(int min,int max,float value, std::string str){
	if(value < min || value > max) {
    printError(str);
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
	return ChecksStatus(MINTEMPERATURE,MAXTEMPERATURE,temperature,"Temperature");
}
bool Battery::batterysocIsOk(float soc){
	 return ChecksStatus(MINSOC,MAXSOC,soc,"State of Charge");
}



