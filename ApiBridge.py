import requests


class ApiBridge:
    def __init__(self, host: str, port: int, ssl: bool) -> None:
        self.host = host
        self.port = port

        self.base_direction = f"{'https' if ssl else 'http'}://{host}:{port}"

    def get_info_for_media(self, media: str):
        resquest_string = f"{self.base_direction}/media-sources/{media}"
        res = requests.get(resquest_string)
        return res.json()

    def post_links_with_errors_for_media(self, error_data, media: str):
        request_string = f"{self.base_direction}/link-errors/{media}"
        res = requests.post(request_string, data=error_data)
        return res.json()

    def post_extracted_info(self, extracted_data, media: str):
        request_string = f"{self.base_direction}/extracted-data/{media}"
        res = requests.post(request_string, data=extracted_data)
        return res.json()
