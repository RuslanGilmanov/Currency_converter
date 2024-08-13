import pytest
from unittest.mock import Mock
from currency_converter import api_parse
from config import API_KEY
import responses


@responses.activate
def test_api_parse_successful():
    # Mock the API response
    url = "https://api.example.com"
    responses.add(responses.GET, url, json={"data": "some data"}, status=200)

    # Call the function and assert the result
    params = {"key": "value"}
    result = api_parse(url, params)
    assert result == {"data": "some data"}


@responses.activate
def test_api_parse_non_200_status():
    # Mock the API response with a non-200 status code
    url = "https://api.example.com"
    responses.add(responses.GET, url, status=404)

    # Call the function and assert that it raises a ValueError
    params = {"key": "value"}
    with pytest.raises(ValueError, match="Information not found"):
        api_parse(url, params)
