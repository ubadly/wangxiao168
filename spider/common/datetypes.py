class SchoolType:
    def __init__(self, url):
        self._url = url

    @property
    def url(self):
        return self._url

    @property
    def data(self) -> dict:
        return {
            "url": self._url,
        }
