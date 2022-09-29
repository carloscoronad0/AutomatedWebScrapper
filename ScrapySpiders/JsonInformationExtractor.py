import json

from typing import Dict, List

FILEPATH = "datos+fecha+cuerpo_v6.json"


class JsonExtractor:
    def __init__(self, media: str) -> None:
        if media:
            self.info = self.get_json_data_from_file(FILEPATH)
            self.filtered_by_empty_info = self.get_empty_by_specific_media_data(media)

    def get_json_data_from_file(self, path_to_file: str) -> Dict:
        with open(path_to_file) as f:
            text = f.read()
            return json.loads(text)

    def get_all_systems_from_data(self) -> List[str]:
        return list(dict.fromkeys([elem["medio"] for elem in self.info]))

    def get_empty_by_specific_media_data(self, media: str):
        match_elements = []
        for elem in self.info:
            if (elem["medio"] == media) and (not elem["cuerpo"]):
                match_elements.append(elem)

        return match_elements


# aux = JsonExtractor("www.paginasiete.bo")
# print(aux.filtered_by_empty_info)

