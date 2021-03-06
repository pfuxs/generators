# -*- coding: utf-8 -*-

"""
Go Generator
Copyright (C) 2018, 2020 Erik Fleckstein <erik@tinkerforge.com>
Copyright (C) 2019-2020 Matthias Bolte <matthias@tinkerforge.com>

go_common.py: Common library for generation of Go bindings and documentation

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

import re

from generators import common

class GoDevice(common.Device):
    def get_go_name(self):
        if self.is_tng():
            return self.get_category().camel + self.get_name().camel

        return self.get_name().camel + self.get_category().camel

    def get_go_package(self):
        if self.is_tng():
            return self.get_category().under + "_" + self.get_name().under

        return self.get_name().under + "_" + self.get_category().under

    def specialize_go_doc_function_links(self, text):
        def specializer(packet, high_level):
            if packet.get_type() == 'callback':
                name = 'Register{0}Callback'.format(packet.get_name(skip=-2 if high_level else 0).camel)
            else:
                name = packet.get_name(skip=-2 if high_level else 0).camel

            return name

        return self.specialize_doc_rst_links(text, specializer)

class GoPacket(common.Packet):
    def get_go_return_type(self, high_level=False, ignore_constant_group=False):
        returns = list("{} {}".format(r.get_go_name(), r.get_go_type(ignore_constant_group=ignore_constant_group)) for r in self.get_elements(direction='out') if not high_level or r.get_level() != 'low')

        if high_level and self.has_high_level():
            if self.get_high_level('stream_in') != None:
                stream = self.get_high_level('stream_in')
                written_elements = [elem for elem in self.get_elements(direction='out') if elem.get_level() == 'low' and elem.get_role() == 'stream_chunk_written']

                if stream.has_short_write():
                    returns.append("{} {}".format(written_elements[0].get_go_name(), "uint64"))
            elif self.get_high_level('stream_out') != None:
                data = self.get_high_level('stream_out').get_data_element()
                returns.insert(0, "{} []{}".format(data.get_go_name(), data.get_go_type(ignore_cardinality=True, ignore_constant_group=True)))

        if self.get_type() == 'callback':
            return ", ".join(returns)

        return ", ".join(returns + ["err error"])

    def get_high_level_payload_type(self):
        return [elem.get_go_type(ignore_cardinality=True) for elem in self.get_elements(direction='out') if elem.get_level() == 'low' and elem.get_role() == 'stream_chunk_data'][0]

    def get_go_parameters(self, high_level=False, ignore_constant_group=False):
        parameters = []

        for element in self.get_elements(high_level=high_level):
            if element.get_direction() == 'out' and self.get_type() == 'function':
                continue

            go_type = element.get_go_type(ignore_constant_group=ignore_constant_group)
            name = element.get_go_name()
            parameters.append('{name} {type}'.format(name=name, type=go_type))

        return ', '.join(parameters)

    def get_return_type(self):
        returns = self.get_elements(direction='out')

        if len(returns) == 0:
            return "()"

        if len(returns) == 1:
            if self.has_high_level():
                return self.get_go_type_name()
            else:
                return returns[0].get_go_type()

        return self.get_go_type_name()

    def get_stream_info_return_type(self):
        returns = [elem for elem in self.get_elements(direction='out') if elem.get_level() == 'low']

        if len(returns) == 0:
            return "()"
        if len(returns) == 1:
            return returns[0].get_go_type()

        return self.get_go_type_name()

    def get_go_name(self, skip=0):
        return self.get_name(skip=skip).camel

    def get_go_type_name(self, skip=0):
        name = self.get_go_name(skip)

        if self.get_name(skip).under.startswith('get_'):
            name = name[3:]
        elif self.get_name(skip).under.startswith('is_'):
            name = name[2:]

        return name

    def get_go_derivable_traits(self, high_level_only=False):
        filtered_returns = self.get_elements(direction='out') if not high_level_only else [ret for ret in self.get_elements(direction='out') if ret.get_level() != 'low']
        result = ["Clone"]

        # String can be cloned, but not copied, so don't derive copy if the struct will contain strings
        if all("String" not in x.get_go_type() for x in filtered_returns):
            result.append("Copy")

        # Arrays with more than 32 entries don't implement any traits except clone and copy
        if all(x.get_cardinality() <= 32 for x in filtered_returns):
            result += ["Debug", "Default", "PartialEq"]

            # Floats implement PartialEq only, as NaN != NaN
            if all("f" not in x.get_go_type() for x in filtered_returns):
                result += ["Eq", "Hash"]

        return result

    def get_go_formatted_doc(self):
        text = common.select_lang(self.get_doc_text())

        # handle links
        text = text.replace(":ref:", "")
        text = re.sub("`([^<]+) <([^>]+)>`__", r"\g<2>", text)

        # handle tables
        lines = text.split('\n')
        replaced_lines = []
        in_table_head = False
        in_table_body = False
        col_count = 0

        for line in lines:
            line = line.replace('"', '')

            if line.strip() == '.. csv-table::':
                in_table_head = True
            elif line.strip().startswith(':header: ') and in_table_head:
                line = line[len(':header: '):]
                col_count = line.count(",") + 1
                line = line.replace(",", "|")
                replaced_lines.append(line)
            elif line.strip().startswith(':widths:') and in_table_head:
                pass
            elif len(line.strip()) == 0 and in_table_head:
                in_table_head = False
                in_table_body = True

                replaced_lines.append("|".join([" --- "] * col_count))
            elif in_table_head:
                replaced_lines.append(line.replace(",", "|"))
            elif len(line.strip()) == 0 and in_table_body:
                in_table_body = False
                replaced_lines.append('')
            elif in_table_body:
                replaced_lines.append(line.replace(",", "|"))
            else:
                replaced_lines.append(line)

        text = '\n'.join(replaced_lines)
        text = self.get_device().specialize_go_doc_function_links(text)

        text = text.replace('.. note::', 'Note')
        text = text.replace('.. warning::', 'Warning')

        def format_parameter(name):
            return '\\c {0}'.format(name) # FIXME

        text = common.handle_rst_param(text, format_parameter)
        text = common.handle_rst_word(text)
        text = common.handle_rst_substitutions(text, self)
        text += common.format_since_firmware(self.get_device(), self)

        return '// ' + '\n// '.join(text.strip().split('\n'))

class GoElement(common.Element):
    def format_value(self, value):
        if isinstance(value, list):
            result = []

            for subvalue in value:
                result.append(self.format_value(subvalue))

            return '{{{0}}}'.format(', '.join(result))

        type_ = self.get_type()

        if type_ == 'float':
            return common.format_float(value)

        if type_ == 'bool':
            return str(bool(value)).lower()

        if type_ == 'char':
            return "'{0}'".format(value.replace("'", "\\'"))

        if type_ == 'string':
            return '"{0}"'.format(value.replace('"', '\\"'))

        return str(value)

    def get_go_name(self):
        blacklist = ["break", "default", "func", "interface", "select", "case", "defer", "go", "map", "struct", "chan", "else", "goto", "package", "switch", "const", "fallthrough", "if", "range", "type", "continue", "for", "import", "return", "var"]
        name = self.get_name().headless

        if name in blacklist:
            return name + "_"

        return name

    def get_go_type(self, ignore_cardinality=False, ignore_constant_group=False, context='default', cardinality=None):
        assert context in ['default', 'meta'], context
        assert cardinality == None or (isinstance(cardinality, int) and cardinality > 0), cardinality

        if cardinality == None:
            cardinality = self.get_cardinality()

        # FIXME: currently common.py enforces that there is at most one contant group per element and not one per index
        if not ignore_constant_group and self.get_constant_group(index=self.get_indices()[0]) is not None:
            return self.get_constant_group(index=self.get_indices()[0]).get_name().camel

        if self.get_type() == 'char':
            element_type = 'rune'
        elif self.get_type() == 'string':
            return 'string'
        elif self.get_type() == 'bool':
            element_type = 'bool'
        elif self.get_type() == 'float':
            element_type = 'float32'
        else:
            element_type = self.get_type()

        if cardinality > 1 and not ignore_cardinality:
            if context == 'meta' and self.get_role() == 'stream_data':
                element_type = "[]{}".format(element_type)
            else:
                element_type = "[{count}]{type}".format(type=element_type, count=cardinality)
        elif cardinality < 0 and not ignore_cardinality:
            element_type = "[]{}".format(element_type)

        return element_type

class GoConstantGroup(common.ConstantGroup):
    def get_go_type(self):
        return get_go_type(self.get_type(), 1)

go_types = {
    'int8':   'int8',
    'uint8':  'uint8',
    'int16':  'int16',
    'uint16': 'uint16',
    'int32':  'int32',
    'uint32': 'uint32',
    'int64':  'int64',
    'uint64': 'uint64',
    'float':  'float32',
    'bool':   'bool',
    'char':   'rune',
    'string': 'string'
}

go_sizes = {
    'int8':   8,
    'uint8':  8,
    'int16':  16,
    'uint16': 16,
    'int32':  32,
    'uint32': 32,
    'int64':  64,
    'uint64': 64,
    'float32':32,
    'bool':   1,
    'rune':   8,
    'string': 'string'
}

def get_go_type_size(type_):
    return go_sizes[type_]

def get_go_type(type_, cardinality, array=False):
    go_type = go_types[type_]

    if array and cardinality != 1 and type_ != 'string':
        go_type = '[{}]{}'.format(cardinality, go_type)
    elif cardinality != 1 and type_ != 'string':
        go_type = '[]{}'.format(go_type)

    return go_type

class GoGeneratorTrait:
    def get_bindings_name(self):
        return 'go'

    def get_bindings_display_name(self):
        return 'Go'

    def get_doc_null_value_name(self):
        return 'nil'

    def get_doc_formatted_param(self, element):
        return element.get_go_name()

    def get_element_class(self):
        return GoElement

    def generates_high_level_callbacks(self):
        return True
