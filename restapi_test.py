import requests
from restapi import MtgRestApi


def test_check_create_class():
    service = MtgRestApi()
    print(service)
    assert service is not None


def test_check_getRestApiUrl_Method():
    service = MtgRestApi()
    url = service.getRestApiUrl()
    assert url is not ""


def test_check_getMtgCards_Method_None():
    service = MtgRestApi()
    cards = service.getMtgCards()
    assert cards is not None


def test_check_getMtgCards_Method_GreaterThan_Zero():
    service = MtgRestApi()
    cards = service.getMtgCards()
    assert len(cards) > 0
