#define CATCH_CONFIG_MAIN

#include "test/catch.hpp"
#include <iostream>
#include "checker.hpp"
#include <cstdlib> 
#include <ctime> 
using namespace BatteryStatus;


TEST_CASE("TEST_CASE 1 :: Generate Parameters of Battery Temperature") {
  
    Battery batteryobj;
    std::srand(static_cast<unsigned int>(std::time(nullptr))); 
  
    for (int count=1; count <= 25; ++count)
    {
        float randval =  std::rand()%100;
        assert(batteryobj.batteryIsOk(randval,TEMPERATURE) == true);
        assert(batteryobj.batteryIsOk(randval,SOC) == true);
	}
}
TEST_CASE("TEST_CASE 2 :: Generate Parameters of Battery SOC") {
  
    Battery batteryobj;
    std::srand(static_cast<unsigned int>(std::time(nullptr))); 
  
    for (int count=1; count <= 25; ++count)
    {
        float randval =  std::rand()%100;
        assert(batteryobj.batteryIsOk(randval,TEMPERATURE) == true);
        assert(batteryobj.batteryIsOk(randval,SOC) == true);
	}
}