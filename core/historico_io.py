import logging
from os.path import isfile

loger = logging.getLogger(__name__)


class OpenTxt():
    def __init__(self):
        pass

    def read_data(self, path):
        data = []
        if not isfile(path):
            loger.warning("Arquivo %s não existe", path)
            return data
        with open(path, "r", encoding="utf-8") as file:
            data = file.read().strip().split("\n")
        print(data)
        loger.debug(f"lendo {path}")
        return data

    def write_data(self, path, line_data):
        try:
            with open(path, "a", encoding="utf-8") as info:
                info.write(line_data + "\n")
        except Exception as eror:
            loger.error(f"{eror}")


if __name__ == "__main__":
    txt = OpenTxt()
    print(txt.read_data("./../historico/cargos.txt"))
# logging.StreamHandler()
# import time
# time.sleep(10)
