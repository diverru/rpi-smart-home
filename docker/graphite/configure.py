#!/usr/bin/env python
import argparse

import os


def replace(fname, handler):
    output = []
    section_data = {}
    section_name = None

    def flush_section():
        if section_name is None:
            return
        handler(section_name, section_data)
        output.append("[{}]".format(section_name))
        for key in sorted(section_data):
            output.append("{} = {}".format(key, section_data[key]))
        output.append("")

    for s in open(fname).readlines():
        s = s.rstrip()
        if section_name is None and (not s or s.startswith("#")):
            output.append(s)
            continue
        if s.startswith("["):
            flush_section()
            section_data = {}
            section_name = s[1:-1]
            continue
        if "=" in s:
            name, _, value = s.partition("=")
            section_data[name.strip()] = value.strip()

    flush_section()
    with open(fname, "w") as f:
        for s in output:
            f.write(s + "\n")


def main(args):
    def replace_retentions(_, data):
        if data.get("pattern") == ".*":
            data["retentions"] = "1m:24h,10m:7d,1h:1800d"

    def replace_x_files_factor(section, data):
        if section == "default_average":
            data["xFilesFactor"] = 0

    replace(os.path.join(args.path, "storage-schemas.conf"), replace_retentions)
    replace(os.path.join(args.path, "storage-aggregation.conf"), replace_x_files_factor)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("path")
    args = p.parse_args()
    main(args)