def check_range(value,limit):
    if isinstance(value,bool):
        raise ValueError("Bool is not accepted")
    try:
        return float(value) <= limit and float(value) >= -limit
    except:
        raise ValueError()