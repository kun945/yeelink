#!/bin/bash

time=`date +%Y-%m-%dT%H:%M:%S`
curl --request POST --data "{\"timestamp\":\"$time\", \"value\":88}"  --header "U-ApiKey: 4060b64de984dfbf2fbaf311a90d510b" http://api.yeelink.net/v1.0/device/10296/sensor/16528/datapoints
