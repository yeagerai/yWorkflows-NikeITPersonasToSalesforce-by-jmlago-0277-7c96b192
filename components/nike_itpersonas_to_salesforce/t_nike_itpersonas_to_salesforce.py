
import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError
from your_component_file import (
    NikeITPersonasToSalesforce,
    NikeITPersonasToSalesforceIn,
    NikeITPersonasToSalesforceOut,
    nike_it_personas_to_salesforce_app,
)

client = TestClient(nike_it_personas_to_salesforce_app)

# Replace `your_mocked_data_function` with a function that generates mocked data for testing
from your_mocked_data_function import generate_mocked_data

# List of test cases with mocked input and expected output data
test_cases = generate_mocked_data()

@pytest.mark.parametrize("test_case", test_cases)
def test_transform(test_case):
    mocked_input = test_case["input"]
    expected_output = test_case["output"]

    # Call the component's `transform()` method with the mocked input data
    instance = NikeITPersonasToSalesforce()
    result = instance.transform(mocked_input, callbacks=None)

    # Assert that the output matches the expected output
    assert result == expected_output

# Test with FastAPI TestClient
@pytest.mark.parametrize("test_case", test_cases)
def test_transform_api(test_case):
    mocked_input = test_case["input"]
    expected_output = test_case["output"]

    response = client.post("/transform/", json=mocked_input.dict())

    assert response.status_code == 200
    assert response.json() == expected_output.dict()

# Include error handling and edge case scenarios
def test_invalid_input():
    # Replace `invalid_input` with an example of invalid input data
    invalid_input = ...  

    with pytest.raises(ValidationError):
        NikeITPersonasToSalesforceIn(**invalid_input)
