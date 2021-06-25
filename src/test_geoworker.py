from geoworker import check_latitude, check_longitude, get_distance_coordinates_in_km

lisbon = (38.865693, -9.138679)
madrid = (40.459833, -3.719194)

def test_check_latitude():
    assert check_latitude(10) == True
    assert check_latitude("80.0") == True
    assert check_latitude(200) == False


def test_check_longitude():
    assert check_longitude(10) == True
    assert check_longitude("80.0") == True
    assert check_longitude(200) == False


def test_get_distance_coordinates_in_km():
    assert get_distance_coordinates_in_km(lisbon[0],lisbon[1],madrid[0],madrid[1]) == 496.5090019749831