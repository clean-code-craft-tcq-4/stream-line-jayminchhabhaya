#pragma once
#include <assert.h>
#include <iostream>
#include <vector>
#include <functional>
using namespace std;
#define MINTEMPERATURE 0
#define MAXTEMPERATURE 45
#define MINSOC 20
#define MAXSOC 80

namespace BatteryStatus
{
	class Battery
	{
		public:
		    Battery(){
				functptr.emplace_back(Battery::batteryTemperatureIsOk);	
				functptr.emplace_back(Battery::batterysocIsOk); 
			};
			~Battery(){};
		    bool batteryIsOk(float ParametersofBatteryStatus);
			static bool batteryTemperatureIsOk(float temperature);
			static bool batterysocIsOk(float soc);
			std::vector<std::function<bool(float)>> functptr;
			
    };
}