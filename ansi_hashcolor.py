#!/usr/bin/env python3
"""
Get a pair of 256-color ANSI escape sequences, chosen for dark backgrounds.
The choice is made with a non-cryptographic hash function to get the indexes
Copyright © 2022 Eli Array Minkoff
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


def fnv1a_32(str_to_hash):
    """My implementation of FNV-1a, as described at
    http://www.isthe.com/chongo/tech/comp/fnv/index.html#FNV-1a
    Made with reference to the javascript implementation at
    https://github.com/sindresorhus/fnv1a/blob/main/index.js w
    """
    hash = 2166136261
    prime = 16777619
    for c in bytearray(str_to_hash, 'utf-8'):
        hash = (hash ^ c) * prime
    return hash
