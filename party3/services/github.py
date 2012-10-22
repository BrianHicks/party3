'check if github is up'
import requests
import json

from party3.supplies import notify

def run():
    'check if github is up'
    overall = requests.get('https://status.github.com/status.json')
    if not overall.ok:
        return notify(
            'Could not reach github. Status code: %d' % overall.status_code
        )

    if overall.json['status'] != 'good':
        msg = 'github status was not good. The following status are impacted: '

        realtime = requests.get('https://status.github.com/realtime.json')
        if not realtime.ok:
            return notify(
                'Could not reach github realtime. '
                'Status code: %d' % overall.status_code
            )

        return notify(
            msg + ', '.join([
                key for key, value in realtime.json if value is False
            ])
        )

    return notify('Github is good')
