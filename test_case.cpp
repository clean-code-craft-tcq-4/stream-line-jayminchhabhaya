#define CATCH_CONFIG_MAIN

#include "test/catch.hpp"
#include <iostream>
#include "checker.hpp"
#include <cstdlib> 
#include <ctime> 
using namespace BatteryStatus;


TEST_CASE("TEST_CASE 1 :: Generate Parameters of Battery Temperature and SOC") {
  
    Battery batteryobj;
    std::srand(static_cast<unsigned int>(std::time(nullptr))); 
  
    for (int count=1; count <= 100; ++count)
    {
        assert(batteryobj.batteryIsOk((std::rand()%100),TEMPERATURE) == true);
	}
	for (int count=1; count <= 100; ++count)
    {
        assert(batteryobj.batteryIsOk((std::rand()%100),SOC) == true);
	}
	assert(batteryobj.printoutputtocommunicate() == true);
}
TEST_CASE("TEST_CASE 2 :: Fail to Generate Parameters of Battery") {
  
    Battery batteryobj;
    std::srand(static_cast<unsigned int>(std::time(nullptr))); 
	assert(batteryobj.printoutputtocommunicate() == false);
}