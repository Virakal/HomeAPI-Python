class Light:
    def __init__(self, client, data: dict):
        self.client = client
        self.id = data['id']
        self.name = data['name']
        self.brightness = float(data['brightnessPercentage'])
        self.is_on = data['isOn']
        self.is_reachable = data['isReachable']

    def set_brightness(self, brightness_percentage: float):
        if not 0 <= brightness_percentage <= 100:
            raise ValueError('Brightness must be between 0 and 100')

        # Don't support percentages yet
        brightness = int((2**8 - 1) * (brightness_percentage / 100))
        print(f"Setting brightness to {brightness}")

        self.client._post('/api/lights/set-light-state', {
            "LightIds": [self.id],
            "Brightness": brightness,
        })
