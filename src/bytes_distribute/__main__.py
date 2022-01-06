#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import pprint

import click


@click.group()
def main():
    pass


@click.command()
@click.option("--input", help="target file", required=True)
@click.option(
    "--max-bytes",
    type=click.IntRange(1000, 15000),
    default=10000,
    help="max input bytes of a single file",
)
@click.option(
    "--token-len",
    "length",
    type=click.IntRange(2, 5),
    default=4,
    help="default byte token length",
)
def file(
    input: str,
    max_bytes: int,
    length: int,
):
    input = os.path.abspath(input)
    tokens = dict()
    with open(input, "rb") as fp:
        data = fp.read(max_bytes)
        i = 0
        while i + length < len(data):
            token = data[i : i + length]
            cnt = tokens.get(token, 0)
            tokens[token] = cnt + 1
            i += length

    pprint.pprint(
        sorted(tokens.items(), key=lambda kv: kv[1], reverse=True)[:20],
    )


main.add_command(file)

if __name__ == "__main__":
    main()
