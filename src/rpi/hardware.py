import logging
import subprocess


def get_temperature() -> float:
    raw = (
        subprocess.check_output(["vcgencmd measure_temp"], shell=True)
        .decode("utf8")
        .strip()
    )
    logging.info(f"Got temperature {raw}")
    temp = raw.split("=")[1]
    temp = temp.split("'")[0]
    return float(temp)
