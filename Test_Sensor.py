import ProdSensor


def test_moisture_sensor_returns_int():
    moist = ProdSensor.Sensor_Control()
    assert type(moist.moisture_check()) is int


def test_moisture_sensor_failure():
    moist = ProdSensor.Sensor_Control()
    assert moist.moisture_check() < 0
