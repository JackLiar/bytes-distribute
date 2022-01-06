#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from datetime import datetime

import pandas as pd


def generate_fname(suffix: str) -> str:
    dt = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    return "-".join([dt, suffix])


def save_dist_to_xlsx(dist: dict, fpath: str, out_dir: str):
    """Save bytes distribution into a xlsx file

    Args:
        dist: bytes distribution dict
        fpath: input fpath string
        out_dir: output directory
    """
    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    dist = sorted(dist.items(), key=lambda kv: kv[1], reverse=True)
    fname = generate_fname(os.path.basename(fpath))
    fname = os.path.join(out_dir, fname)
    writer = pd.ExcelWriter(f"{fname}.xlsx", engine="xlsxwriter")
    df = pd.DataFrame.from_dict(
        {"token": (r[0] for r in dist), "count": (r[1] for r in dist)}
    )
    df.to_excel(writer, index=False)
    writer.save()


def save_dist_to_image(dist: dict, fapth: str, out_dir: str):
    """Save bytes distribution into a img"""
    pass
