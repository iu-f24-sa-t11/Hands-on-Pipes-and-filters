from components.filters import Filter


class ProxyFilter(Filter):
    def handle_data(self, data):
        return data
