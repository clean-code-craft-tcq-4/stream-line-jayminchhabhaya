#define CATCH_CONFIG_MAIN

#include "test/catch.hpp"
#include <iostream>
#include "checker.hpp"
using namespace BatteryStatus;


TEST_CASE("TEST_CASE 1 :: Detects samples in two ranges") {
  Battery batteryobj;
  std::vector<float>ParametersofBatteryStatus{25, 70};
  assert(batteryobj.batteryIsOk(ParametersofBatteryStatus) == true);
  std::vector<float>ParametersofBatteryStatus1{50, 85};
  assert(batteryobj.batteryIsOk(ParametersofBatteryStatus1) == false);
}
