# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Industrial Analog Out Bricklet 2.0 communication config

from generators.configs.openhab_commonconfig import *

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 2116,
    'name': 'Industrial Analog Out V2',
    'display_name': 'Industrial Analog Out 2.0',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'Generates configurable DC voltage and current, 0V to 10V and 4mA to 20mA',
        'de': 'Erzeugt konfigurierbare Gleichspannung und -strom, 0V bis 10V und 4mA bis 20mA'
    },
    'released': True,
    'documented': True,
    'discontinued': False,
    'features': [
        'device',
        'comcu_bricklet',
        'bricklet_get_identity'
    ],
    'constant_groups': [],
    'packets': [],
    'examples': []
}

com['constant_groups'].append({
'name': 'Voltage Range',
'type': 'uint8',
'constants': [('0 To 5V', 0),
              ('0 To 10V', 1)]
})

com['constant_groups'].append({
'name': 'Current Range',
'type': 'uint8',
'constants': [('4 To 20mA', 0),
              ('0 To 20mA', 1),
              ('0 To 24mA', 2)]
})

com['constant_groups'].append({
'name': 'Out LED Config',
'type': 'uint8',
'constants': [('Off', 0),
              ('On', 1),
              ('Show Heartbeat', 2),
              ('Show Out Status', 3)]
})

com['constant_groups'].append({
'name': 'Out LED Status Config',
'type': 'uint8',
'constants': [('Threshold', 0),
              ('Intensity', 1)]
})

com['packets'].append({
'type': 'function',
'name': 'Set Enabled',
'elements': [('Enabled', 'bool', 1, 'in', {'default': False})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Enables/disables the output of voltage and current.
""",
'de':
"""
Aktiviert/deaktiviert die Ausgabe von Spannung und Strom.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Enabled',
'elements': [('Enabled', 'bool', 1, 'out', {'default': False})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns *true* if output of voltage and current is enabled, *false* otherwise.
""",
'de':
"""
Gibt *true* zurück falls die Ausgabe von Spannung und Strom aktiviert ist,
*false* sonst.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Voltage',
'elements': [('Voltage', 'uint16', 1, 'in', {'scale': (1, 1000), 'unit': 'Volt', 'range': (0, 10000)})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Sets the output voltage.

The output voltage and output current are linked. Changing the output voltage
also changes the output current.
""",
'de':
"""
Setzt die Ausgangsspannung.

Die Ausgangsspannung und der Ausgangsstrom sind gekoppelt. Eine Änderung der
Ausgangsspannung führt auch zu einer Änderung des Ausgangsstroms.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Voltage',
'elements': [('Voltage', 'uint16', 1, 'out', {'scale': (1, 1000), 'unit': 'Volt', 'range': (0, 10000)})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the voltage as set by :func:`Set Voltage`.
""",
'de':
"""
Gibt die Spannung zurück, wie von :func:`Set Voltage` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Current',
'elements': [('Current', 'uint16', 1, 'in', {'scale': (1, 10**6), 'unit': 'Ampere', 'range': (0, 24000)})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Sets the output current.

The output current and output voltage are linked. Changing the output current
also changes the output voltage.
""",
'de':
"""
Setzt den Ausgangsstrom.

Der Ausgangsstrom und die Ausgangsspannung sind gekoppelt. Eine Änderung des
Ausgangsstroms führt auch zu einer Änderung der Ausgangsspannung.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Current',
'elements': [('Current', 'uint16', 1, 'out', {'scale': (1, 10**6), 'unit': 'Ampere', 'range': (0, 24000)})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the current as set by :func:`Set Current`.
""",
'de':
"""
Gibt die Spannung zurück, wie von :func:`Set Current` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Configuration',
'elements': [('Voltage Range', 'uint8', 1, 'in', {'constant_group': 'Voltage Range', 'default': 1}),
             ('Current Range', 'uint8', 1, 'in', {'constant_group': 'Current Range', 'default': 0})],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Configures the voltage and current range.

Possible voltage ranges are:

* 0V to 5V
* 0V to 10V

Possible current ranges are:

* 4mA to 20mA
* 0mA to 20mA
* 0mA to 24mA

The resolution will always be 12 bit. This means, that the
precision is higher with a smaller range.
""",
'de':
"""
Konfiguriert die Spannungs- und Stromwertebereiche.

Einstellbare Spannungswertebereiche sind:

* 0V bis 5V
* 0V bis 10V

Einstellbare Stromwertebereiche sind:

* 4mA bis 20mA
* 0mA bis 20mA
* 0mA bis 24mA

Die Auflösung ist immer 12 Bit. Dass heißt, die Genauigkeit erhöht
sich bei kleineren Wertebereichen.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Configuration',
'elements': [('Voltage Range', 'uint8', 1, 'out', {'constant_group': 'Voltage Range', 'default': 1}),
             ('Current Range', 'uint8', 1, 'out', {'constant_group': 'Current Range', 'default': 0})],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the configuration as set by :func:`Set Configuration`.
""",
'de':
"""
Gibt die Konfiguration zurück, wie von :func:`Set Configuration` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Out LED Config',
'elements': [('Config', 'uint8', 1, 'in', {'constant_group': 'Out LED Config', 'default': 3})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
You can turn the Out LED off, on or show a
heartbeat. You can also set the LED to "Out Status". In this mode the
LED can either be turned on with a pre-defined threshold or the intensity
of the LED can change with the output value (voltage or current).

You can configure the channel status behavior with :func:`Set Out LED Status Config`.
""",
'de':
"""
Die Out LED kann an- oder
ausgeschaltet werden. Zusätzlich kann ein Heartbeat oder der "Out-Status"
angezeigt werden. Falls Out-Status gewählt wird kann die LED entweder ab einem
vordefinierten Schwellwert eingeschaltet werden oder ihre Helligkeit anhand des
Ausgabewertes (Spannung oder Strom) skaliert werden.

Das Verhalten des Out-Status kann mittels :func:`Set Out LED Status Config`
eingestellt werden.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Out LED Config',
'elements': [('Config', 'uint8', 1, 'out', {'constant_group': 'Out LED Config', 'default': 3})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the Out LED configuration as set by :func:`Set Out LED Config`
""",
'de':
"""
Gibt die Out-LED-Konfiguration zurück, wie von :func:`Set Out LED Config` gesetzt.
"""
}]
})

out_led_status_description = {
'en': """For each channel you can choose between threshold and intensity mode.

In threshold mode you can define a positive or a negative threshold.
For a positive threshold set the "min" parameter to the threshold value in mV or
µA above which the LED should turn on and set the "max" parameter to 0. Example:
If you set a positive threshold of 5V, the LED will turn on as soon as the
output value exceeds 5V and turn off again if it goes below 5V.
For a negative threshold set the "max" parameter to the threshold value in mV or
µA below which the LED should turn on and set the "min" parameter to 0. Example:
If you set a negative threshold of 5V, the LED will turn on as soon as the
output value goes below 5V and the LED will turn off when the output value
exceeds 5V.

In intensity mode you can define a range mV or µA that is used to scale the brightness
of the LED. Example with min=2V, max=8V: The LED is off at 2V and below, on at
8V and above and the brightness is linearly scaled between the values 2V and 8V.
If the min value is greater than the max value, the LED brightness is scaled the
other way around.""",
'de': """Für jeden Kanal kann zwischen Schwellwert- und Intensitätsmodus gewählt werden.

Im Schwellwertmodus kann ein positiver oder negativer Schwellwert definiert werden.
Für einen positiven Schwellwert muss der "min" Parameter auf den gewünschten
Schwellwert in mV oder µA gesetzt werden, über dem die LED eingeschaltet werden
soll. Der "max" Parameter muss auf 0 gesetzt werden. Beispiel: Bei einem
positiven Schwellwert von 5V wird die LED eingeschaltet sobald der Ausgabewert
über 5V steigt und wieder ausgeschaltet sobald der Ausgabewert unter 5V fällt.
Für einen negativen Schwellwert muss der "max" Parameter auf den gewünschten
Schwellwert in mV oder µA gesetzt werden, unter dem die LED eingeschaltet werden
soll. Der "max" Parameter muss auf 0 gesetzt werden. Beispiel: Bei einem negativen
Schwellwert von 5V wird die LED eingeschaltet sobald der Ausgabewert unter
5V fällt und wieder ausgeschaltet sobald der Ausgabewert über 5V steigt.

Im Intensitätsmodus kann ein Bereich in mV oder µA angegeben werden über den die
Helligkeit der LED skaliert wird. Beispiel mit min=2V und max=8V: Die LED ist
bei 2V und darunter aus, bei 8V und darüber an und zwischen 2V und 8V wird die
Helligkeit linear skaliert. Wenn der min Wert größer als der max Wert ist, dann
wird die Helligkeit andersherum skaliert."""}

com['packets'].append({
'type': 'function',
'name': 'Set Out LED Status Config',
'elements': [('Min', 'uint16', 1, 'in', {'range': (0, 24000), 'default': 0}),
             ('Max', 'uint16', 1, 'in', {'range': (0, 24000), 'default': 10000}),
             ('Config', 'uint8', 1, 'in', {'constant_group': 'Out LED Status Config', 'default': 1})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Sets the Out LED status config. This config is used if the Out LED is
configured as "Out Status", see :func:`Set Out LED Config`.

{}
""".format(out_led_status_description['en']),
'de':
"""
Setzt die Out-LED-Status-Konfiguration. Diese Einstellung wird verwendet wenn
die Out-LED auf Out-Status eingestellt ist, siehe :func:`Set Out LED Config`.

{}
""".format(out_led_status_description['de'])
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Out LED Status Config',
'elements': [('Min', 'uint16', 1, 'out', {'range': (0, 24000), 'default': 0}),
             ('Max', 'uint16', 1, 'out', {'range': (0, 24000), 'default': 10000}),
             ('Config', 'uint8', 1, 'out', {'constant_group': 'Out LED Status Config', 'default': 1})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the Out LED status configuration as set by :func:`Set Out LED Status Config`.
""",
'de':
"""
Gibt die Out-LED-Status-Konfiguration zurück, wie von :func:`Set Out LED Status Config` gesetzt.
"""
}]
})

com['examples'].append({
'name': 'Simple Voltage',
'functions': [('setter', 'Set Voltage', [('uint16', 3300)], 'Set output voltage to 3.3V', None),
              ('setter', 'Set Enabled', [('bool', True)], None, None),
              ('wait',)],
'cleanups': [('setter', 'Set Enabled', [('bool', False)], None, None)]
})

com['examples'].append({
'name': 'Simple Current',
'functions': [('setter', 'Set Current', [('uint16', 4500)], 'Set output current to 4.5mA', None),
              ('setter', 'Set Enabled', [('bool', True)], None, None),
              ('wait',)],
'cleanups': [('setter', 'Set Enabled', [('bool', False)], None, None)]
})

com['openhab'] = {
    'imports': oh_generic_channel_imports() + ['org.eclipse.smarthome.core.library.types.OnOffType'],
    'param_groups': oh_generic_channel_param_groups() + [{
        'name': 'outledstatus',
        'label': {'en': 'Output LED Status Configuration', 'de': 'Output-LED-Status-Konfiguration'},
        'description': {'en': 'Configuration of the status mode of the output LED',
                        'de': 'Konfiguration des Status-Modus der Output-LED'},
    }],
    'params': [
        {
            'virtual': True,
            'name': 'Control Voltage',
            'type': 'integer',
            'options': [
                ('Current', 0),
                ('Voltage', 1),
            ],
            'limit_to_options': 'true',
            'default': 1,
            'label': {'en': 'Output Configuration', 'de': 'Ausgabekonfiguration'},
            'description': {'en': 'Sets the output configuration. As the output voltage and current level depend on each other, only one can be controlled at the same time.',
                            'de': 'Setzt die Ausgabekonfiguration. Da die ausgegebene Spannung und Stromstärke von einander abhängen, kann nur einer der Werte gleichzeitig gesteuert werden.'}
        }, {
            'packet': 'Set Configuration',
            'element': 'Voltage Range',

            'name': 'Voltage Range',
            'type': 'integer',

            'label': {'en': 'Voltage Range', 'de': 'Spannungsbereich'},
            'description': {'en': 'Configures the voltage range. The resolution will always be 12 bit. This means, that the precision is higher with a smaller range.',
                            'de': 'Konfiguriert den Spannungswertebereich. Die Auflösung ist immer 12 Bit. Dass heißt, die Genauigkeit erhöht sich bei kleineren Wertebereichen.'}
        }, {
            'packet': 'Set Configuration',
            'element': 'Current Range',

            'name': 'Current Range',
            'type': 'integer',

            'label': {'en': 'Current Range', 'de': 'Stromstärkenbereich'},
            'description': {'en': 'Configures the current range. The resolution will always be 12 bit. This means, that the precision is higher with a smaller range.',
                            'de': 'Konfiguriert den Stromstärken-Wertebereich. Die Auflösung ist immer 12 Bit. Dass heißt, die Genauigkeit erhöht sich bei kleineren Wertebereichen.'}
        }, {
            'packet': 'Set Out LED Config',
            'element': 'Config',

            'name': 'Out LED Config',
            'type': 'integer',

            'label': {'en': 'Output LED', 'de': 'Output-LED'},
            'description': {'en': 'You can turn the Out LED off, on or show a heartbeat. You can also set the LED to Out Status. In this mode the LED can either be turned on with a pre-defined threshold or the intensity of the LED can change with the output value (voltage or current).',
                            'de': 'Die Out LED kann an- oder ausgeschaltet werden. Zusätzlich kann ein Heartbeat oder der "Out-Status" angezeigt werden. Falls Out-Status gewählt wird kann die LED entweder ab einem vordefinierten Schwellwert eingeschaltet werden oder ihre Helligkeit anhand des Ausgabewertes (Spannung oder Strom) skaliert werden.'},
        }, {
            'packet': 'Set Out LED Status Config',
            'element': 'Config',

            'name': 'Out LED Status Mode',
            'type': 'integer',
            'groupName': 'outledstatus',
            'label': {'en': 'Output LED Status Mode', 'de': 'Output-LED-Status Modus'},
            'description': {'en': out_led_status_description['en'].replace('"', '\\\"'),
                            'de': out_led_status_description['de'].replace('"', '\\\"')}
        }, {
            'packet': 'Set Out LED Status Config',
            'element': 'Min',

            'name': 'Out LED Status Minimum',
            'type': 'decimal',
            'groupName': 'outledstatus',
            'min': 0,
            'max': 10,
            'label': {'en': 'Output LED Status Minumum', 'de': 'Output-LED-Status Minumum'},
            'description': {'en': 'See Output LED Status Mode for further explaination.',
                            'de': 'Siehe Output LED Status Mode für Details.'}
        }, {
            'packet': 'Set Out LED Status Config',
            'element': 'Max',

            'name': 'Out LED Status Maximum',
            'type': 'decimal',
            'groupName': 'outledstatus',
            'min': 0,
            'max': 10,
            'default': 10,

            'label': {'en': 'Output LED Status Maximum', 'de': 'Output-LED-Status Maximum'},
            'description': {'en': 'See Output LED Status Mode for further explaination.',
                            'de': 'Siehe Output LED Status Mode für Details.'}
        }
    ],
    'init_code': """this.setConfiguration(cfg.voltageRange, cfg.currentRange);
this.setOutLEDConfig(cfg.outLEDConfig);
this.setOutLEDStatusConfig((int)(cfg.outLEDStatusMinimum.doubleValue() * (cfg.controlVoltage == 1 ? 1000.0 : 1000000.0)),
                           (int)(cfg.outLEDStatusMaximum.doubleValue() * (cfg.controlVoltage == 1 ? 1000.0 : 1000000.0)),
                           cfg.outLEDStatusMode);""",
    'channels': [{
            'id': 'Enabled',
            'type': 'Enabled',

            'setters': [{
                'packet': 'Set {title_words}',
                'packet_params': ['cmd == OnOffType.ON'],
                'command_type': "OnOffType"
            }],

            'getters': [{
                'packet': 'Get {title_words}',
                'element': '{title_words}',
                'transform': 'value ? OnOffType.ON : OnOffType.OFF'}]
        },
        {
            'id': 'Current',
            'type': 'Current',

            'predicate': 'cfg.controlVoltage == 0',

            'setters': [{
                'packet': 'Set {title_words}',
                'element': '{title_words}',
                'packet_params': ['(int)(cmd.doubleValue(){divisor})'],
                'command_type': "Number"
            }],

            'getters': [{
                'packet': 'Get {title_words}',
                'element': '{title_words}',
                'transform': 'new {number_type}(value{divisor}{unit})'}],
        },
        {
            'id': 'Voltage',
            'type': 'Voltage',

            'predicate': 'cfg.controlVoltage == 1',

            'setters': [{
                'packet': 'Set {title_words}',
                'element': '{title_words}',
                'packet_params': ['(int)(cmd.doubleValue(){divisor})'],
                'command_type': "Number",
            }],

            'getters': [{
                'packet': 'Get {title_words}',
                'element': '{title_words}',
                'transform': 'new {number_type}(value {divisor}{unit})'}],
        }
    ],
    'channel_types': [
        oh_generic_channel_type('Enabled', 'Switch', {'en': 'Output', 'de': 'Ausgabe'},
                    update_style=None,
                    description={'en': 'Enables/disables the output of voltage and current.',
                                 'de': 'Aktiviert/Deaktiviert die Ausgabe von Spannung und Strom.'}),
        oh_generic_channel_type('Voltage', 'Number', {'en': 'Output Voltage', 'de': 'Ausgabespannung'},
                    update_style=None,
                    description={'en': 'The output voltage. The output voltage and output current are linked. Changing the output voltage also changes the output current.',
                                 'de': 'Die Ausgabespannung. Die Ausgangsspannung und der Ausgangsstrom sind gekoppelt. Eine Änderung der Ausgangsspannung führt auch zu einer Änderung des Ausgangsstroms.'}),
        oh_generic_channel_type('Current', 'Number', {'en': 'Output Current', 'de': 'Ausgabestrom'},
                    update_style=None,
                    description={'en': 'The output current. The output current and output voltage are linked. Changing the output current also changes the output voltage.',
                                 'de': 'Der Ausgabestrom. Der Ausgangsstrom und die Ausgangsspannung sind gekoppelt. Eine Änderung des Ausgangsstroms führt auch zu einer Änderung der Ausgangsspannung.'})
    ],
    'actions': [{'fn': 'Set Enabled', 'refreshs': ['Enabled']}, 'Get Enabled', 'Get Voltage', 'Get Current', 'Get Configuration', 'Get Out LED Config', 'Get Out LED Status Config']
}

