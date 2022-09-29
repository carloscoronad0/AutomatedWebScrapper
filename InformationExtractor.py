from multiprocessing.sharedctypes import Value
import os
import json

from typing import Dict, List

from matplotlib.mlab import complex_spectrum
from ApiBridge import ApiBridge


class InformationExtractor:
    def __init__(
        self, api_extractor: ApiBridge = None, source_folder: str = ""
    ) -> None:
        self.api_extractor = api_extractor
        self.source_folder = source_folder

    def get_media_info_from_api(self, media: str):
        info = self.api_extractor.get_info_for_media(media).content
        return info

    def get_media_info_from_json_file(self, filename: str):
        complete_path = os.path.join(self.source_folder, filename)
        if os.path.isfile(complete_path):
            f = open(complete_path, "r")
            text = f.read()
            f.close()

            return json.loads(text)
        else:
            raise ValueError(f"Path {complete_path} does not exist")
