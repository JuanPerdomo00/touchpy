#!/usr/bin/python3
# -*- coding: utf-8 -*-
#   ** GOD IS FIRTS **
#
#   Copyright (C) <2023>  <Jakepys>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

__author__ = "Jakepys Perdomo"
__version__ = '1.1'

import sys
import re
import os
import argparse
from datetime import datetime
from cansii import CAnsii as c


class LICENSE:
    @staticmethod
    def gplv3(author: str, year: str) -> str:
        return f'''
# Copyright (C) <{year}>  <{author}>  

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

    @staticmethod
    def mit(author: str, year: str) -> str:
        return f'''
# MIT License
# 
# Copyright (c) [{year}] [{author}]
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

    @staticmethod
    def apache2(author: str, year: str) -> str:
        return f'''
# Apache License
# 
# Version 2.0, January 2004
# 
# Copyright (c) [{year}] [{author}]
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
'''

    @staticmethod
    def bsd(author: str, year:  str) -> str:
        return f'''
# BSD License
# 
# Copyright (c) <{year}> <{author}>
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
# GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

    @staticmethod
    def mozilla_public_license(author: str, year: str) -> str:
        return f'''
# Mozilla Public License 2.0 (MPL-2.0)
# <{author}> <{year}>
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.u
'''

    @staticmethod
    def isc(author: str, year: str) -> str:
        return f'''
# ISC License
# 
# Copyright (c) <{author}>, <{year}>
# 
# Permission to use, copy, modify, and/or distribute this software for any purpose with or without
# fee is hereby granted, provided that the above copyright notice and this permission notice
# appear in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS
# SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY
# DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF
# CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE
# OR PERFORMANCE OF THIS SOFTWARE.
'''

    @staticmethod
    def list_licenses() -> str:
        licenses = ['gplv3', 'mit', 'apache2',
                    'bsd', 'mozilla_public_license', 'isc']

        licenses_info = "\n".join([
            f"License: {license}\n{getattr(LICENSE, license)('example-author', 'example-date')}\n{'='*80}" for license in licenses
        ])

        return licenses_info


def version() -> None:
    '''Print Version'''
    print(c.bold(f'''\r1.0 touchpy \n
                    \rCopyright (C) 2023 Free Software.
                    \rLicense GPLv3 GNU GPL version 3 <https://gnu.org/licenses/gpl.html>.
                    \rThis is free software

                     \rIt is a small script that arose after the need to put headers in python files 
                     \rsuch as encoding or binary path. Finally enjoy it.\n
            \rWritten by {__author__}.\n'''))
    sys.exit(0)


def authors(author: str) -> str:
    return author.capitalize()


def linceses(author: str = None, year: str = None, license_name: str = None) -> str:
    if author is None:
        author = 'Anonymous'

    current_date = datetime.now()
    if year is None:
        year = current_date.strftime('%Y-%m-%d')

    license_functions = {
        'gplv3': LICENSE.gplv3,
        'mit': LICENSE.mit,
        'apache2': LICENSE.apache2,
        'bsd': LICENSE.bsd,
        'mozilla_public_license': LICENSE.mozilla_public_license,
        'isc': LICENSE.isc
    }

    # Verifica si se proporciona un nombre de licencia válido y si coincide con las funciones disponibles
    if license_name and license_name in license_functions:
        # Devuelve el texto de la licencia correspondiente
        return license_functions[license_name](author, year)
    else:
        return ''  # Devuelve una cadena vacía si no se proporciona una licencia válida


def list_licenses():
    print(c.italic(LICENSE.list_licenses()))


def create_file(filename: str, author: str = None, license_text: str = None) -> None:
    lines = [
        '#!/usr/bin/python3\n',
        '# -*- coding: utf-8 -*-\n',
        '# === Generate By Touchpy ===\n',
        license_text]

    if re.match(r".+\.py", filename):
        print(c.green(f"[+] Creating file: {filename}\n"))
        with open(filename, "w", encoding="UTF-8") as f:
            f.writelines(lines)
    else:
        print(c.red_bold("[!] The file must have a .py extension."))


def main(argv: list) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='Create a Python file')
    parser.add_argument(
        '-a', '--author',  type=str, help='Specify the author of the file', default='Anonymous')
    parser.add_argument('-l', '--license', type=str,
                        help='Specify the license')
    parser.add_argument('-v', '--version', action='store_true',
                        help='Display version message and exit 0')
    parser.add_argument('-pl', '--printlicenses', action='store_true',
                        help='Display List Licenses and exit 0')

    args = parser.parse_args(argv[1:])

    if args.version:
        version()
    elif args.printlicenses:
        list_licenses()
    else:
        if os.path.exists(args.file):
            print(c.yellow(f'[?] The file {args.file} already exists'))
            sys.exit(1)

        create_file(filename=args.file, author=authors(
            args.author), license_text=linceses(args.author, license_name=args.license))


if __name__ == "__main__":
    main(sys.argv)
