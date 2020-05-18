#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Saleae ZIP Generator
Copyright (C) 2020 Erik Fleckstein <erik@tinkerforge.com>

generate_saleae_zip.py: Generator for Saleae ZIP

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

import sys

if sys.hexversion < 0x3040000:
    print('Python >= 3.4 required')
    sys.exit(1)

import os
import shutil

sys.path.append(os.path.split(os.getcwd())[0])
import common
import saleae_common

class SaleaeZipGenerator(saleae_common.SaleaeGeneratorTrait, common.ZipGenerator):
    def __init__(self, *args):
        common.ZipGenerator.__init__(self, *args)

        self.tmp_dir          = self.get_tmp_dir()

    def get_bindings_name(self):
        return 'saleae'

    def prepare(self):
        common.recreate_dir(self.tmp_dir)

    def generate(self, device):
        pass

    def finish(self):
        root_dir = self.get_root_dir()
        bindings_dir = self.get_bindings_dir()

        # Copy bindings and readme
        shutil.copy(os.path.join(bindings_dir, 'HighLevelAnalyzer.py'),           self.tmp_dir)
        shutil.copy(os.path.join(bindings_dir, 'extension.json'),           self.tmp_dir)
        shutil.copy(os.path.join(root_dir, 'changelog.txt'),                  self.tmp_dir)
        shutil.copy(os.path.join(root_dir, 'readme.txt'),                     self.tmp_dir)
        shutil.copy(os.path.join(root_dir, '..', 'configs', 'license.txt'),   self.tmp_dir)

        # Make zip
        self.create_zip_file(self.tmp_dir)

def generate(root_dir):
    common.generate(root_dir, 'en', SaleaeZipGenerator)

if __name__ == '__main__':
    generate(os.getcwd())