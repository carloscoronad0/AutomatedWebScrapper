# %%
import os
import subprocess
import json

from ApiBridge import ApiBridge

SPIDERS_PATH = "./ScrapySpiders"


def clean_from_json_files():
    files_on_path = os.listdir(SPIDERS_PATH)
    for f in files_on_path:
        if f.endswith(".json"):
            subprocess.run(["rm", f"{SPIDERS_PATH}/{f}"])


def execute_scrapy_spiders():
    files_on_path = os.listdir(SPIDERS_PATH)

    for f in files_on_path:
        if f.endswith("_spider.py"):
            print(f"Executing spider: {f}")
            output_name = f.replace("_spider.py", "")
            subprocess.run(
                [
                    "scrapy",
                    "runspider",
                    f"{SPIDERS_PATH}/{f}",
                    "-o",
                    f"{SPIDERS_PATH}/{output_name}_extract.json",
                ]
            )


def upload_to_database(host: str, port: int):
    bridge = ApiBridge(host, port, False)
    files_on_path = os.listdir(SPIDERS_PATH)

    for f in files_on_path:
        if f.endswith("_extract.json"):
            fl = open(f"{SPIDERS_PATH}/{f}", "r")
            text = fl.read()
            fl.close()
            extracted_data = json.loads(text)

            media = f.replace("_extract.json", "")
            bridge.post_extracted_info(extracted_data, media)


clean_from_json_files()
execute_scrapy_spiders()
upload_to_database()
