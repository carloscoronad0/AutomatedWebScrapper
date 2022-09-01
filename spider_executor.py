# %%
import os
import subprocess

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
            output_name = f.replace('_spider.py', '')
            subprocess.run(
                [
                    "scrapy",
                    "runspider",
                    f"{SPIDERS_PATH}/{f}",
                    "-o",
                    f"{SPIDERS_PATH}/{output_name}.json",
                ]
            )


clean_from_json_files()
execute_scrapy_spiders()
