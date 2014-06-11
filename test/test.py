#!/usr/bin/env python

from yeelink import YeeLinkClient
from yeelink import current_time

client = YeeLinkClient('youer_app_id')
print client.datapoint.create('device_id', 'sensor_id', '{"timestamp":"%s", "value":%s}' %(current_time(), 1111))
