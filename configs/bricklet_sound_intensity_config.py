# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Sound Intensity Bricklet communication config

from generators.configs.commonconstants import THRESHOLD_OPTION_CONSTANT_GROUP

from generators.configs.openhab_commonconfig import *

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 238,
    'name': 'Sound Intensity',
    'display_name': 'Sound Intensity',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'Measures sound intensity',
        'de': 'Misst Schallintensität'
    },
    'released': True,
    'documented': True,
    'discontinued': False, # selling remaining stock, replaced by Sound Pressure Level Bricklet
    'features': [
        'device',
        'bricklet_get_identity'
    ],
    'constant_groups': [],
    'packets': [],
    'examples': []
}

com['constant_groups'].append(THRESHOLD_OPTION_CONSTANT_GROUP)

com['packets'].append({
'type': 'function',
'name': 'Get Intensity',
'elements': [('Intensity', 'uint16', 1, 'out', {'range': (0, 4095)})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the current sound intensity.

The value corresponds to the
`upper envelop <https://en.wikipedia.org/wiki/Envelope_(waves)>`__
of the signal of the microphone capsule.

If you want to get the intensity periodically, it is recommended to use the
:cb:`Intensity` callback and set the period with
:func:`Set Intensity Callback Period`.
""",
'de':
"""
Gibt die aktuelle Schallintensität zurück.

Der Wert entspricht der
`Hüllkurve <https://de.wikipedia.org/wiki/H%C3%BCllkurvendemodulator>`__
des Signals der Mikrophonkapsel.

Wenn die Schallintensität periodisch abgefragt werden soll, wird empfohlen
den :cb:`Intensity` Callback zu nutzen und die Periode mit
:func:`Set Intensity Callback Period` vorzugeben.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Intensity Callback Period',
'elements': [('Period', 'uint32', 1, 'in', {'scale': (1, 1000), 'unit': 'Second', 'default': 0})],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period with which the :cb:`Intensity` callback is triggered
periodically. A value of 0 turns the callback off.

The :cb:`Intensity` callback is only triggered if the intensity has changed
since the last triggering.
""",
'de':
"""
Setzt die Periode mit welcher der :cb:`Intensity` Callback ausgelöst wird.
Ein Wert von 0 deaktiviert den Callback.

The :cb:`Intensity` Callback wird nur ausgelöst, wenn sich die Intensität seit
der letzten Auslösung geändert hat.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Intensity Callback Period',
'elements': [('Period', 'uint32', 1, 'out', {'scale': (1, 1000), 'unit': 'Second', 'default': 0})],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`Set Intensity Callback Period`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`Set Intensity Callback Period` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Intensity Callback Threshold',
'elements': [('Option', 'char', 1, 'in', {'constant_group': 'Threshold Option', 'default': 'x'}),
             ('Min', 'uint16', 1, 'in', {'default': 0}),
             ('Max', 'uint16', 1, 'in', {'default': 0})],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the thresholds for the :cb:`Intensity Reached` callback.

The following options are possible:

.. csv-table::
 :header: "Option", "Description"
 :widths: 10, 100

 "'x'",    "Callback is turned off"
 "'o'",    "Callback is triggered when the intensity is *outside* the min and max values"
 "'i'",    "Callback is triggered when the intensity is *inside* the min and max values"
 "'<'",    "Callback is triggered when the intensity is smaller than the min value (max is ignored)"
 "'>'",    "Callback is triggered when the intensity is greater than the min value (max is ignored)"
""",
'de':
"""
Setzt den Schwellwert für den :cb:`Intensity Reached` Callback.

Die folgenden Optionen sind möglich:

.. csv-table::
 :header: "Option", "Beschreibung"
 :widths: 10, 100

 "'x'",    "Callback ist inaktiv"
 "'o'",    "Callback wird ausgelöst, wenn die Intensität *außerhalb* der min und max Werte ist"
 "'i'",    "Callback wird ausgelöst, wenn die Intensität *innerhalb* der min und max Werte ist"
 "'<'",    "Callback wird ausgelöst, wenn die Intensität kleiner als der min Wert ist (max wird ignoriert)"
 "'>'",    "Callback wird ausgelöst, wenn die Intensität größer als der min Wert ist (max wird ignoriert)"
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Intensity Callback Threshold',
'elements': [('Option', 'char', 1, 'out', {'constant_group': 'Threshold Option', 'default': 'x'}),
             ('Min', 'uint16', 1, 'out', {'default': 0}),
             ('Max', 'uint16', 1, 'out', {'default': 0})],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the threshold as set by :func:`Set Intensity Callback Threshold`.
""",
'de':
"""
Gibt den Schwellwert zurück, wie von :func:`Set Intensity Callback Threshold` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Debounce Period',
'elements': [('Debounce', 'uint32', 1, 'in', {'scale': (1, 1000), 'unit': 'Second', 'default': 100})],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period with which the threshold callback

* :cb:`Intensity Reached`

is triggered, if the thresholds

* :func:`Set Intensity Callback Threshold`

keeps being reached.
""",
'de':
"""
Setzt die Periode mit welcher der Schwellwert-Callback

* :cb:`Intensity Reached`

ausgelöst wird, wenn der Schwellwert

* :func:`Set Intensity Callback Threshold`

weiterhin erreicht bleibt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Debounce Period',
'elements': [('Debounce', 'uint32', 1, 'out', {'scale': (1, 1000), 'unit': 'Second', 'default': 100})],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the debounce period as set by :func:`Set Debounce Period`.
""",
'de':
"""
Gibt die Entprellperiode zurück, wie von :func:`Set Debounce Period` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Intensity',
'elements': [('Intensity', 'uint16', 1, 'out', {'range': (0, 4095)})],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`Set Intensity Callback Period`. The :word:`parameter` is the intensity
of the sensor.

The :cb:`Intensity` callback is only triggered if the intensity has changed
since the last triggering.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit :func:`Set Intensity Callback Period`,
ausgelöst. Der :word:`parameter` ist gemessene Schallintensität.

Der :cb:`Intensity` Callback wird nur ausgelöst, wenn sich die Intensität seit
der letzten Auslösung geändert hat.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Intensity Reached',
'elements': [('Intensity', 'uint16', 1, 'out', {'range': (0, 4095)})],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered when the threshold as set by
:func:`Set Intensity Callback Threshold` is reached.
The :word:`parameter` is the intensity of the encoder.

If the threshold keeps being reached, the callback is triggered periodically
with the period as set by :func:`Set Debounce Period`.
""",
'de':
"""
Dieser Callback wird ausgelöst, wenn der Schwellwert, wie von
:func:`Set Intensity Callback Threshold` gesetzt, erreicht wird.
Der :word:`parameter` ist die gemessene Schallintensität.

Wenn der Schwellwert erreicht bleibt, wird der Callback mit der Periode, wie
mit :func:`Set Debounce Period` gesetzt, ausgelöst.
"""
}]
})

com['examples'].append({
'name': 'Simple',
'functions': [('getter', ('Get Intensity', 'intensity'), [(('Intensity', 'Intensity'), 'uint16', 1, None, None, None)], [])]
})

com['examples'].append({
'name': 'Callback',
'functions': [('callback', ('Intensity', 'intensity'), [(('Intensity', 'Intensity'), 'uint16', 1, None, None, None)], None, None),
              ('callback_period', ('Intensity', 'intensity'), [], 50)]
})

com['examples'].append({
'name': 'Threshold',
'functions': [('debounce_period', 1000),
              ('callback', ('Intensity Reached', 'intensity reached'), [(('Intensity', 'Intensity'), 'uint16', 1, None, None, None)], None, None),
              ('callback_threshold', ('Intensity', 'intensity'), [], '>', [(2000, 0)])]
})

com['openhab'] = {
    'imports': oh_generic_channel_imports(),
    'param_groups': oh_generic_channel_param_groups(),
    'channels': [
        oh_generic_old_style_channel('Intensity', 'Intensity')
    ],
    'channel_types': [
        oh_generic_channel_type('Intensity', 'Number', 'Sound Intensity',
                    update_style='Callback Period',
                    description="""The current sound intensity. The value has a range of 0 to 4095.\n\nThe value corresponds to the `upper envelop <https://en.wikipedia.org/wiki/Envelope_(waves)>`__ of the signal of the microphone capsule.""")
    ],
    'actions': ['Get Intensity']
}
