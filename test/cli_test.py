#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 LG Electronics Inc.
# SPDX-License-Identifier: Apache-2.0

import getopt
import os
import sys
import json
from datetime import datetime
import logging
import fosslight_util.constant as constant
from fosslight_util.set_log import init_log
from fosslight_source.run_scancode import run_scan

logger = logging.getLogger(constant.LOGGER_NAME)


def main():
    global logger

    argv = sys.argv[1:]
    path_to_find_bin = os.path.abspath("test/test")
    start_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    output_file_name = ""

    oss_report_name = "test_result_func_call/result"
    output_dir = os.path.dirname(os.path.abspath(output_file_name))

    logger = init_log(os.path.join(output_dir, "fosslight_src_log_"+start_time+".txt"))

    ret = run_scan(path_to_find_bin, oss_report_name, True, -1, True)

    logger.warn("[Scan] Result: %s" % (ret[0]))
    logger.warn("[Scan] Result_msg: %s" % (ret[1]))

    if len(ret) > 2:
        logger.warn("[Scan] Result_items: %s" % (str(ret[2])))


if __name__ == '__main__':
    main()
