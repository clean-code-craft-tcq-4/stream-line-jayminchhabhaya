#define CATCH_CONFIG_MAIN

#include "test/catch.hpp"
#include <iostream>
#include "checker.hpp"
#include <cstdlib> 
#include <ctime> 
using namespace BatteryStatus;


TEST_CASE("TEST_CASE 1 :: Generate Parameters of Battery Status") {
  Battery batteryobj;
  
    std::srand(static_cast<unsigned int>(std::time(nullptr))); 
  
    //for (int count=1; count <= 50; ++count)
    //{
    //    std::cout << std::rand()%100;
        //std::vector<float>TemperatureParametersofBatteryStatus{25, 70};
        assert(batteryobj.batteryIsOk(25,TEMPERATURE) == true);
        assert(batteryobj.batteryIsOk(70,SOC) == true);
	//}
}
