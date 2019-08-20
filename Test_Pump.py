import ProdPump


def test_pump_total_time():
    pump = ProdPump.Pump_Control()
    assert pump.pump_water(2, 0.1) == 3
    assert pump.pump_water(2, 2) == 22
