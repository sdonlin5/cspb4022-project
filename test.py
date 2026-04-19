#!/usr/bin/env python
from utils.dropCols import drop_cols

from extract import get_pbp
import polars as pl

test = get_pbp([2024, 2025]).sample(100)
test.sample(20)

test2 = drop_cols(test, "~/Dev/cspb4022-project/dropCalculatedStats.txt")
test2.sample(20)





