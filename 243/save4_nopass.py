import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

import pytest

from ips import (ServiceIPRange, parse_ipv4_service_ranges,
                 get_aws_service_range)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network('192.0.2.8/29')


@pytest.fixture(scope='module')
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


# write your pytest code ...

@pytest.mark.parametrize("service, region, cidr", [
    ('AMAZON', 'af-south-1', '3.2.34.0/26' ),
])
def test_ServiceIPRange(service, region, cidr):
    ip_range= ServiceIPRange(
                service=service,
                region=region,
                cidr=IPv4Network(cidr))

    expected_str = f"{cidr} is allocated to the {service} service in the {region} region"

    assert str(ip_range) == expected_str


def test_ServiceIPRange_invalid_ip():
    with pytest.raises(ValueError):
        ip_range= ServiceIPRange(
                service='foo',
                region='bar',
                cidr=IPv4Network('invalid'))


def test_parse_ipv4_service_ranges(json_file):
    ip_ranges = parse_ipv4_service_ranges(json_file)
    assert len(ip_ranges) == 1886
    assert ip_ranges[0].cidr == IPv4Network("13.248.118.0/24")
    assert ip_ranges[0].region == "eu-west-1"
    assert ip_ranges[0].service == "AMAZON"
    assert ip_ranges[-1].cidr == IPv4Network("54.250.251.0/24")
    assert ip_ranges[-1].region == "ap-northeast-1"
    assert ip_ranges[-1].service == "WORKSPACES_GATEWAYS"


@pytest.mark.parametrize("address, expected", [
            ('0.0.0.0', []),
            ('255.255.255.255', []),
            ('54.153.254.10', [
                            ServiceIPRange(
                            service='AMAZON', 
                            region='ap-southeast-2', 
                            cidr=IPv4Network('54.153.128.0/17')), 
                        ServiceIPRange(
                            service='EC2', 
                            region='ap-southeast-2', 
                            cidr=IPv4Network('54.153.128.0/17')), 
                        ServiceIPRange(
                            service='WORKSPACES_GATEWAYS', 
                            region='ap-southeast-2', 
                            cidr=IPv4Network('54.153.254.0/24'))
                        ]),
    ])
def test_get_aws_service_range(address, expected, json_file):
    service_range = get_aws_service_range(address, parse_ipv4_service_ranges(json_file))
    assert service_range == expected
    

def test_get_aws_service_range_invalid_ip(json_file):
    with pytest.raises(ValueError,match=r"Address must be a valid IPv4 address"):
        service_range = get_aws_service_range(
            'invalid',
            parse_ipv4_service_ranges(json_file))


urlretrieve(URL, PATH)
print(get_aws_service_range('54.153.254.10', parse_ipv4_service_ranges(PATH)))

