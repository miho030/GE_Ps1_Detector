# -*- coding: utf-8 -*-

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os.path
import argparse
import xml.etree.ElementTree as ET

# Windows Command to generate the XML file
# wevtutil query-events "Windows Powershell" /uni:true /f:XML > winps.xml

parser=argparse.ArgumentParser(description='A parser for the Windows Powershell event log XML generated by wevutil command.')
parser.add_argument('xml', help='Path of the XML File')
args=parser.parse_args()
filename=args.xml
if not os.path.isfile(filename):
  print('Not found:%s' % filename)
  exit(1)
ns='{http://schemas.microsoft.com/win/2004/08/events/event}'  #namespace
f = open(filename, 'r', encoding='utf-16')
xml=f.read()
#print(xml)
xml= "<eventlog>" + xml + "</eventlog>"
root = ET.fromstring(xml)
for event in root:
  for e in event:
    for f in e:
      pass
  eventid=event.find(ns + 'System').find(ns + 'EventID').text
  eventrecid=event.find(ns + 'System').find(ns + 'EventRecordID').text
  time=event.find(ns + 'System').find(ns + 'TimeCreated').attrib
  ps=event.find(ns + 'EventData').findall(ns + 'Data')
  if eventid=="800":
    if(ps[0].text):
      #print("ID:     \t%s" % (eventrecid,))
      #print("EID:      \t%s" % (eventid,))
      #print("Time:    \t%s" % (time,))
      #print("PS:      \t%s" % (ps[0].text))
      print((ps[0].text))
