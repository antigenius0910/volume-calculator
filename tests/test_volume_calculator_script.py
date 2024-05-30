import pytest
from volume_calculator.volume_calculator_script import main

def test_main(monkeypatch):
    inputs = iter(['1', '3', '5', '2', '4', '3', '5', '5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('builtins.print', lambda x: x)

    main()
