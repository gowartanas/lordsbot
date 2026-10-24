class BotSettings:

    def __init__(self, data=None):
        self.data = data or {}

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value

    def update(self, data):
        if data:
            self.data.update(data)

    def is_enabled(self, key, default=False):
        value = self.data.get(key, default)
        return bool(value)

    def all(self):
        return dict(self.data)