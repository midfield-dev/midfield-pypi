import requests


class Midfield:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = 'https://api.midfield.ai/api/prompt/'

    def validate(self, prompt, validate_input: bool = True, validate_output: bool = False):
        if not self.api_key:
            raise ValueError("API KEY is required")

        headers = {
            'Content-Type': 'application/json'
        }

        payload = {
            'apikey': self.api_key,
            'prompt': prompt,
            'validate_input':validate_input,
            'validate_output':validate_output,
        }
        response = requests.post(self.api_url, json=payload, headers=headers)
        if response.status_code != 200:
            if validate_output:
                raise Exception(f"Error: {response.json().get('error')},\nValidate Input: {response.json().get('input_result')},\nValidate Output: {response.json().get('output_result')}")
            else:
                raise Exception(f"Error: {response.json().get('error')},\nvalidate Input: {response.json().get('input_result')}")
        return response.json()
