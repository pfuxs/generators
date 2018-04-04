# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# LCD 128x64 Bricklet communication config

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 298,
    'name': 'LCD 128x64',
    'display_name': 'LCD 128x64',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'LCD with 128x64 pixel',
        'de': 'LCD mit 128x64 Pixel'
    },
    'comcu': True,
    'released': False,
    'documented': False,
    'discontinued': False,
    'packets': [],
    'examples': []
}

com['packets'].append({
'type': 'function',
'name': 'Write Pixels Low Level',
'elements': [('X Start', 'uint8', 1, 'in'),
             ('Y Start', 'uint8', 1, 'in'),
             ('X End', 'uint8', 1, 'in'),
             ('Y End', 'uint8', 1, 'in'),
             ('Pixels Length', 'uint16', 1, 'in'),
             ('Pixels Chunk Offset', 'uint16', 1, 'in'),
             ('Pixels Chunk Data', 'bool', 56*8, 'in')],
'high_level': {'stream_in': {'name': 'Pixels'}},
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Writes pixels to the specified window.

The x-axis goes from 0-127 and the y-axis from 0-63. The pixels are written
into the window line by line from left to right.

If automatic draw is enabled (default) the pixels are directly written to
the screen and only changes are updated. If you only need to update a few
pixels, only these pixels are updated on the screen, the rest stays the same.

If automatic draw is disabled the pixels are written to a buffer and the
buffer is transferred to the display only after :func:`Draw Buffered Frame`
is called.

Automatic draw can be configured with the :func:`Set Display Configuration`
function.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Read Pixels Low Level',
'elements': [('X Start', 'uint8', 1, 'in'),
             ('Y Start', 'uint8', 1, 'in'),
             ('X End', 'uint8', 1, 'in'),
             ('Y End', 'uint8', 1, 'in'),
             ('Pixels Length', 'uint16', 1, 'out'),
             ('Pixels Chunk Offset', 'uint16', 1, 'out'),
             ('Pixels Chunk Data', 'bool', 60*8, 'out')],
'high_level': {'stream_out': {'name': 'Pixels'}},
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Reads pixels from the specified window.

The x-axis goes from 0-127 and the y-axis from 0-63. The pixels are read
from the window line by line from left to right.

If automatic draw is enabled the pixels that are read are always the same that are
shown on the display.

If automatic draw is disabled the pixels are read from the internal buffer
(see :func:`Draw Buffered Frame`).

Automatic draw can be configured with the :func:`Set Display Configuration`
function.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Clear Display',
'elements': [],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Clears the complete content of the display.
""",
'de':
"""
Löscht den kompletten aktuellen Inhalt des Displays.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Display Configuration',
'elements': [('Contrast', 'uint8', 1, 'in'),
             ('Backlight', 'uint8', 1, 'in'),
             ('Invert', 'bool', 1, 'in'),
             ('Automatic Draw', 'bool', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Sets the configuration of the display.

You can set a contrast value from 0 to 63, a backlight intensity value
from 0 to 100 and you can invert the color (black/white) of the display.

If automatic draw is set to *true*, the display is automatically updated with every
call of :func:`Write Pixels` or :func:`Write Line`. If it is set to false, the
changes are written into a temporary buffer and only shown on the display after
a call of :func:`Draw Buffered Frame`.

The default values are contrast 21, backlight intensity 100, inverting off
and automatic draw on.
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Display Configuration',
'elements': [('Contrast', 'uint8', 1, 'out'),
             ('Backlight', 'uint8', 1, 'out'),
             ('Invert', 'bool', 1, 'out'),
             ('Automatic Draw', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the configuration as set by :func:`Set Display Configuration`.
""",
'de':
"""
Gibt die Konfiguration zurück, wie von :func:`Set Display Configuration`
gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Write Line',
'elements': [('Line', 'uint8', 1, 'in'),
             ('Position', 'uint8', 1, 'in'),
             ('Text', 'string', 22, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Writes text to a specific line (0 to 7) with a specific position
(0 to 21). The text can have a maximum of 22 characters.

For example: (1, 10, "Hello") will write *Hello* in the middle of the
second line of the display.

The display uses a special 5x7 pixel charset. You can view the characters
of the charset in Brick Viewer.
""",
'de':
"""
Schreibt einen Text in die angegebene Zeile (0 bis 7) mit einer vorgegebenen
Position (0 bis 21). Der Text kann maximal 22 Zeichen lang sein.

Beispiel: (1, 10, "Hallo") schreibt *Hallo* in die Mitte der zweiten Zeile
des Displays.

Das Display nutzt einen speziellen 5x7 Pixel Zeichensatz. Der Zeichensatz
kann mit Hilfe von Brick Viewer angezeigt werden.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Draw Buffered Frame',
'elements': [('Force Complete Redraw', 'bool', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Draws the currently buffered frame. Normally each call of :func:`Write Pixels` or
:func:`Write Line` draws directly onto the disply. If you turn automatic draw off
(:func:`Set Display Configuration`), the data is written in a temporary buffer and
only transferred to the display by calling this function.

Set the *force complete redraw* parameter to *true* to redraw the whole display
instead of only the changed parts. Normally it should not be necessary to set this to
*true*. It may only become necessary in case of stuck pixels because of errors.
""",
'de':
"""
"""
}]
})


com['packets'].append({
'type': 'function',
'name': 'Get Touch Position',
'elements': [('Pressure', 'uint16', 1, 'out'),
             ('X', 'uint16', 1, 'out'),
             ('Y', 'uint16', 1, 'out'),
             ('Age', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the last valid touch position.

* *X*: Touch position on x-axis (0-127)
* *Y*: Touch position on y-axis (0-63)
* *Pressure*: Amount of pressure applied by the user (0-300).
* *Age*: Age of touch press in ms (how long ago it was).
""",
'de':
"""
TBD
"""
}]
})


com['packets'].append({
'type': 'function',
'name': 'Set Touch Position Callback Configuration',
'elements': [('Period', 'uint32', 1, 'in'),
             ('Value Has To Change', 'bool', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
The period in ms is the period with which the :cb:`Touch Position` callback
is triggered periodically. A value of 0 turns the callback off.

If the `value has to change`-parameter is set to true, the callback is only
triggered after the value has changed. If the value didn't change within the
period, the callback is triggered immediately on change.

If it is set to false, the callback is continuously triggered with the period,
independent of the value.

The default value is (0, false).
""",
'de':
"""
Die Periode in ms ist die Periode mit der der :cb:`Touch Position` Callback
ausgelöst wird. Ein Wert von 0 schaltet den Callback ab.

Wenn der `value has to change`-Parameter auf True gesetzt wird, wird der
Callback nur ausgelöst, wenn der Wert sich im Vergleich zum letzten mal geändert
hat. Ändert der Wert sich nicht innerhalb der Periode, so wird der Callback
sofort ausgelöst, wenn der Wert sich das nächste mal ändert.

Wird der Parameter auf False gesetzt, so wird der Callback dauerhaft mit der
festen Periode ausgelöst unabhängig von den Änderungen des Werts.

Der Standardwert ist (0, false).
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Touch Position Callback Configuration',
'elements': [('Period', 'uint32', 1, 'out'),
             ('Value Has To Change', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the callback configuration as set by
:func:`Set Touch Position Callback Configuration`.
""",
'de':
"""
Gibt die Callback-Konfiguration zurück, wie mittels
:func:`Set Touch Position Callback Configuration` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Touch Position',
'elements': [('Pressure', 'uint16', 1, 'out'),
             ('X', 'uint16', 1, 'out'),
             ('Y', 'uint16', 1, 'out'),
             ('Age', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`Set Touch Position Callback Configuration`. The :word:`parameters` are the
same as for :func:`Get Touch Position`.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit
:func:`Set Touch Position Callback Configuration`, ausgelöst. Die :word:`parameters` sind
die gleichen wie die von :func:`Get Touch Position`.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Touch Gesture',
'elements': [('Gesture', 'uint8', 1, 'out', ('Gesture', [('Left To Right', 0),
                                                         ('Right To Left', 1),
                                                         ('Top To Bottom', 2),
                                                         ('Bottom To Top', 3)])),
             ('Duration', 'uint32', 1, 'out'),
             ('X Start', 'uint16', 1, 'out'),
             ('Y Start', 'uint16', 1, 'out'),
             ('X End', 'uint16', 1, 'out'),
             ('Y End', 'uint16', 1, 'out'),
             ('Age', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns one of four touch gestures that can be automatically detected by the Bricklet.

The gestures are swipes from left to right, right to left, top to bottom and bottom to top.

Additionally to the gestures a vector with a start and end position of the gesture is is
provided. You can use this vecotr do determine a more exact location of the gesture (e.g.
the swipe from top to bottom was on the left or right part of the screen).

The *age*-parameter corresponds to the age of gesture in ms (how long ago it was).
""",
'de':
"""
TBD
"""
}]
})


com['packets'].append({
'type': 'function',
'name': 'Set Touch Gesture Callback Configuration',
'elements': [('Period', 'uint32', 1, 'in'),
             ('Value Has To Change', 'bool', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
The period in ms is the period with which the :cb:`Touch Gesture` callback
is triggered periodically. A value of 0 turns the callback off.

If the `value has to change`-parameter is set to true, the callback is only
triggered after the value has changed. If the value didn't change within the
period, the callback is triggered immediately on change.

If it is set to false, the callback is continuously triggered with the period,
independent of the value.

The default value is (0, false).
""",
'de':
"""
Die Periode in ms ist die Periode mit der der :cb:`Touch Gesture` Callback
ausgelöst wird. Ein Wert von 0 schaltet den Callback ab.

Wenn der `value has to change`-Parameter auf True gesetzt wird, wird der
Callback nur ausgelöst, wenn der Wert sich im Vergleich zum letzten mal geändert
hat. Ändert der Wert sich nicht innerhalb der Periode, so wird der Callback
sofort ausgelöst, wenn der Wert sich das nächste mal ändert.

Wird der Parameter auf False gesetzt, so wird der Callback dauerhaft mit der
festen Periode ausgelöst unabhängig von den Änderungen des Werts.

Der Standardwert ist (0, false).
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Touch Gesture Callback Configuration',
'elements': [('Period', 'uint32', 1, 'out'),
             ('Value Has To Change', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the callback configuration as set by
:func:`Set Touch Gesture Callback Configuration`.
""",
'de':
"""
Gibt die Callback-Konfiguration zurück, wie mittels
:func:`Set Touch Gesture Callback Configuration` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Touch Gesture',
'elements': [('Gesture', 'uint8', 1, 'out',  ('Gesture', [('Left To Right', 0),
                                                          ('Right To Left', 1),
                                                          ('Top To Bottom', 2),
                                                          ('Bottom To Top', 3)])),
             ('Duration', 'uint32', 1, 'out'),
             ('X Start', 'uint16', 1, 'out'),
             ('Y Start', 'uint16', 1, 'out'),
             ('X End', 'uint16', 1, 'out'),
             ('Y End', 'uint16', 1, 'out'),
             ('Age', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`Set Touch Gesture Callback Configuration`. The :word:`parameters` are the
same as for :func:`Get Touch Gesture`.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit
:func:`Set Touch Gesture Callback Configuration`, ausgelöst. Die :word:`parameters` sind
die gleichen wie die von :func:`Get Touch Gesture`.
"""
}]
})