# -*- coding: utf-8 -*-
import vt
import time
import re
import base64
import json

client = vt.Client("e4a26c5ff4b1dfa6f2c084da458e8ee5582cd0e9ee66493668abd6a4f32d0223")

def _ScanPs2_Lit(filepath):
    with open(filepath, "rb") as f:
        analysis = client.scan_file(f)
    md5 = re.findall(r"[0-9a-f]{32}", base64.b64decode(analysis.id).decode())[0]
    try:
        file = client.get_object(f"/files/{md5}")
        result = file.last_analysis_stats
    except:
        while True:
            analysis = client.get_object(f"/analyses/{analysis.id}")
            if analysis.status == "completed":
                break
            time.sleep(30)
        #Output -> json
        result = analysis.stats
    print(result)