from coordinate_validator import check_longitude,check_latitude


def test_check_longitude():
    assert check_longitude(10) == True
    assert check_longitude(181) == False


def test_check_latitude():
    assert check_latitude(10) == True
    assert check_latitude(91) == False
