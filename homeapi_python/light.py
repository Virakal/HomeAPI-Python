class Light:
    def __init__(self, client, data: dict):
        self.client = client
        self.id = data['id']
        self.name = data['name']
        self._brightness = float(data['brightnessPercentage'])
        self._is_on = data['isOn']
        self.is_reachable = data['isReachable']

        self._current_state = {
            "LightIds": [self.id],
            "PowerState": data['isOn'],
            "Brightness": data['brightness'],
            "TransitionMilliseconds": data['transitionMilliseconds'],
        }

    def _set_state(self, **state):
        new_state = {**self._current_state, **state}

        response = self.client._post('/api/lights/set-light-state', new_state)

        if 'success' in response and response['success']:
            self._current_state = new_state
            return response

        raise Exception('Failed to update light state')

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, brightness_percentage: float):
        if not 0 <= brightness_percentage <= 100:
            raise ValueError('Brightness must be between 0 and 100')

        # Don't support percentages yet
        brightness = int((2**8 - 1) * (brightness_percentage / 100))
        print(f"Setting brightness to {brightness}")

        self._set_state(Brightness=brightness)
        self._brightness = brightness_percentage

    @property
    def is_on(self):
        return self._is_on

    @is_on.setter
    def is_on(self, value=True):
        self._set_state(PowerState=value)
        self._is_on = value
