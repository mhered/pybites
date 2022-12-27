import pytest

from numbers_to_dec import list_to_decimal

def test_valid_cases():
    samples = [
        {'input':[0,4,2,8], 'result':428},
        {'input':[1,2], 'result':12},
        {'input':[3], 'result':3},
        {'input':[0,6,5,9], 'result':659},
    ]
    for sample in samples:
        assert list_to_decimal(sample['input']) == sample['result']

def test_bool_type_error():
    samples = [
        {'input':[6,2,True]},
        {'input':[3.6,4,1]},
        {'input':['4',5,3,1]},
        {'input':[[5,3],1]},
        {'input':['foo',1]},
    ]
    with pytest.raises(TypeError):
        for sample in samples:
            list_to_decimal(sample['input'])
        
def test_bool_value_error():
    samples = [
        {'input':[-3,0]},
        {'input':[1,12,1]},
        {'input':[-1,10,32]},

    ]
    with pytest.raises(ValueError):
        for sample in samples:
            list_to_decimal(sample['input'])
        