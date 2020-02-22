from homeapi_python.light import Light

import requests
import urllib3

class Client:
    _lights = {}

    def __init__(self, endpoint='https://localhost:44380', verify_ssl=False):
        self.endpoint = endpoint.rstrip('/')
        self.verify_ssl = verify_ssl

        if not verify_ssl:
            urllib3.disable_warnings()

    def _get(self, path):
        return requests.get(self.endpoint + path, verify=self.verify_ssl).json()

    def _post(self, path, data):
        return requests.post(self.endpoint + path, verify=self.verify_ssl, json=data).json()

    def get_lights(self):
        response = self._get('/api/lights/list-lights')

        # Handle errors
        assert 'data' in response

        lights = response['data']

        for light in lights:
            light_id = int(light['id'])

            if light_id in self._lights:
                continue

            self._lights[light_id] = Light(self, light)

        return self._lights
