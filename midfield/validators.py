import requests


class Midfield:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = 'https://api.midfield.ai/api/prompt/'

    def validate(self, prompt, validate_input, validate_output):
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
            raise Exception(f"Error: {response.json().get('error')}")

        return response.json()
