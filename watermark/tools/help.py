def clamp(val, _min, _max):
    """Keep a value within a certain limit"""
    if val < _min:
        return _min
    elif val > _max:
        return _max
    else:
        return val
