#!/usr/bin/env python
# -*- coding: utf-8 -*-

from yeelink import YeeLinkClient, current_time

if __name__ == '__main__':
    ylc = YeeLinkClient('4060b64de984dfbf2fbaf311a90d510b')

    print ylc.device.list()

    #print ylc.datapoint.create('10296', '16612', '{"tylc.image.stamp":"%s", "value":22}' %current_time())
    #print ylc.datapoint.delete('10296', '16612', '2014-05-19T11:37:09')
    #print ylc.datapoint.edit('10296', '16612', '2014-05-19T11:47:25', '{"value":22}')

    #print ylc.image.upload('10296', '16660', fd = open('./test.jpg', 'rb'))
    #print ylc.image.get_info('10296', '16660', '2014-05-19T12:37:05')
    #print ylc.image.get_content('10296', '16660', '2014-05-19T12:37:05', './back.jpg')

    #print ylc.history('10296', '16612', '2014-05-18T00:00:00', '2014-05-19T23:59:59')
