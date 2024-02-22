import pytest
from wallet import Wallet

@pytest.fixture
def wallet():
    return Wallet()

def test_initial_balance(wallet):
    assert wallet.balance == 0

def test_add_money(wallet):
    wallet.add_money(100)
    assert wallet.balance == 100

def test_spend_money(wallet):
    wallet.add_money(100)
    wallet.spend_money(30)
    assert wallet.balance == 70

def test_add_negative_money(wallet, capsys):
    wallet.add_money(-50)
    captured = capsys.readouterr()
    assert "Введіть коректну суму для додавання." in captured.out

def test_spend_more_than_balance(wallet, capsys):
    wallet.spend_money(100)
    captured = capsys.readouterr()
    assert "Недостатньо грошей на рахунку." in captured.out
