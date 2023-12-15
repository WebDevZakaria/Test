import pytest

pytestmark = pytest.mark.django_db


class TestReceiptModel:

    def test_str_return (self, receipt_factory):
        receipt =  receipt_factory(storename = "test-store")
        assert receipt.__str__() == "test-store"

class TestReceiptView:

    def test_str_return (self, receipt_factory):
        receipt =  receipt_factory(storename = "test-store")
        assert receipt.__str__() == "test-store"

