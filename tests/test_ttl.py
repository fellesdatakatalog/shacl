import pytest
from shacl.examplettl import datasetrdf


def test_datasetrdf():
    rdf = datasetrdf()
    assert "http://example.com/catalogs/1" in rdf.decode()
