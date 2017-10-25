# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Motion Detector Bricklet communication config

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 292,
    'name': 'Motion Detector V2',
    'display_name': 'Motion Detector 2.0',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'Passive infrared (PIR) motion sensor, 7m range',
        'de': 'Passiver Infrarot (PIR) Bewegungssensor, 7m Reichweite'
    },
    'comcu': True,
    'released': False,
    'documented': False,
    'packets': [],
    'examples': []
}


com['packets'].append({
'type': 'function',
'name': 'Get Motion Detected',
'elements': [('Motion', 'uint8', 1, 'out', ('Motion', [('Not Detected', 0),
                                                       ('Detected', 1)]))],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns 1 if a motion was detected. How long this returns 1 after a motion
was detected can be adjusted with one of the small potentiometers on the
Motion Detector Bricklet, see :ref:`here
<motion_detector_bricklet_sensitivity_delay_block_time>`.

There is also a blue LED on the Bricklet that is on as long as the Bricklet is
in the "motion detected" state.
""",
'de':
"""
Gibt 1 zurück wenn eine Bewegung detektiert wurde. Wie lange 1 zurückgegeben
wird nachdem eine Bewegung detektiert wurde kann mit einem kleinen Poti auf
dem Motion Detector Bricklet eingestellt werden, siehe :ref:`hier
<motion_detector_bricklet_sensitivity_delay_block_time>`.

Auf dem Bricklet selbst ist eine blaue LED, die leuchtet solange das Bricklet
im "Bewegung detektiert" Zustand ist.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Sensitivity',
'elements': [('Sensitivity', 'uint8', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
0-100
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Sensitivity',
'elements': [('Sensitivity', 'uint8', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Indicator',
'elements': [('Top Left', 'uint8', 1, 'in'),
             ('Top Right', 'uint8', 1, 'in'),
             ('Bottom', 'uint8', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Indicator',
'elements': [('Top Left', 'uint8', 1, 'out'),
             ('Top Right', 'uint8', 1, 'out'),
             ('Bottom', 'uint8', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Motion Detected',
'elements': [],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is called after a motion was detected.
""",
'de':
"""
Dieser Callback wird aufgerufen nachdem eine Bewegung detektiert wurde.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Detection Cycle Ended',
'elements': [],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is called when the detection cycle ended. When this
callback is called, a new motion can be detected again after approximately 2
seconds.
""",
'de':
"""
Dieser Callback wird aufgerufen wenn ein Bewegungserkennungszyklus
beendet ist. Wenn dieser Callback aufgerufen wurde kann wieder
eine weitere Bewegung erkannt werden nach ungefähr 2 Sekunden.
"""
}]
})


