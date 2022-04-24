import json 
import pytest
import sys 
sys.path.insert(0,'..')
from costack_sdk.costack_lambda import CostackRequest, costack_http


@costack_http(methods=['GET', 'POST'])
def sample_lambda_func(event, context):
    # event will be parsed 
    return event 

class TestLambdaSDK:
    def test_costack_request_parsing_for_get_method(self):
        with open("resources/sample_get.json", "r") as f:
            event = json.loads(f.read())
        request = CostackRequest(event)
        assert request.http_method == "GET"
        assert request.body == None
        assert "text/html" in request.header['accept']
        assert request.is_base64_encoded == False 
        # params is also a JSON file 
        assert request.params == {'name': '1000'}

    def test_costack_request_parsing_for_post_method(self):
        with open("resources/sample_post.json", "r") as f:
            event = json.loads(f.read())
        request = CostackRequest(event)
        assert request.http_method == "POST"
        # unique to post method 
        assert json.loads(request.body) == {"user_id":"123"}
        assert request.header['content-type'] == "application/json"
        assert request.is_base64_encoded == False 

    def test_sample_lambda_wrapper_get(self):
        with open("resources/sample_get.json", "r") as f:
            event = json.loads(f.read())
        request = sample_lambda_func(event, None)
        # should parse successfully
        assert request.http_method == "GET"

    def test_sample_lambda_wrapper_post(self):
        with open("resources/sample_post.json", "r") as f:
            event = json.loads(f.read())
        request = sample_lambda_func(event, None)
        # should parse successfully
        assert request.http_method == "POST"

