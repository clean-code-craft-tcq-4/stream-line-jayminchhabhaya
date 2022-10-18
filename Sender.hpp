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
#define TEMPERATURE 0
#define SOC 1

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
			std::vector<float>temperaturedata{};		
		    bool batteryIsOk(float ParametersofBatteryStatus,int BatteryParameterStatus);
			static bool batteryTemperatureIsOk(float temperature);
			static bool batterysocIsOk(float soc);
			std::vector<std::function<bool(float)>> functptr;
			bool printoutputtocommunicate(std::vector<float> data , string Parameter);
			std::vector<float>socdata{};
			
    };
}