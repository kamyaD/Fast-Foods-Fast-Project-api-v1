import os

# helps in creating temporary database 
import tempfile

import pytest

from app import app

@pytest.fixture #The purpose of test fixtures is to provide a fixed baseline upon which tests can reliably and repeatedly execute
def client():
    order, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    