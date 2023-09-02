import subprocess
from find_Text import FindText
from robot.api.deco import keyword


class BaseAction:

    @staticmethod
    @keyword
    def click(text, partial=False):
        try:
            x, y = FindText.get_text(text, partial)
            subprocess.run(["adb", "-s", "104e6ae3", "shell", "input", "tap", str(x), str(y)], check=True,
                           shell=True)
        except subprocess.CompletedProcess as e:
            raise e

    @staticmethod
    @keyword
    def isPresent(text, partial=False):
        try:
            dump_result = FindText.get_text(text, partial)
            if dump_result is not None:
                print(f"'{text}' is present")
        except Exception as e:
            raise e