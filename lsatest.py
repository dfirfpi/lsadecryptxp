#!/usr/bin/python

# LsaDecryptXp tests
# Copyright 2015 Francesco "dfirfpi" Picasso. All Rights Reserved.
# Author email: <francesco.picasso@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

import unittest
import lsadecryptxp


class DecryptionTest(unittest.TestCase):
    """Decryption tests for LsaDecryptXp."""

    def setUp(self):

        self.feedback = '\x97\x37\x6f\xfb\xb7\x5e\xee\x86'

        self.desxkey = (
            '\x3d\x6a\x42\x1f\x3b\xfe\xe0\x7b\xa2\xbf\xcb\x46\x91\x32\x63\xf4'
            '\x5c\xd4\xe8\xa4\x4c\x4d\x07\x06\x34\xd8\xb8\x64\x8a\xcd\x0e\xc1'
            '\xbc\xdc\x0c\xcc\x8d\x8a\xc6\x80\xb8\xf0\xc8\x30\x49\xcf\xc2\x8d'
            '\xe4\xa8\x30\xa8\x43\xcb\xce\x4a\xdc\xb0\x48\x64\xc6\xc2\x0f\x49'
            '\xd4\x70\x8c\x4c\xcb\x4b\x0b\xc6\x64\xf4\x58\xd4\xc9\xc8\xcd\x88'
            '\x78\xd4\x5c\x18\xc4\x83\x4d\xc5\xf0\x64\xf4\x3c\x87\x8f\x87\x02'
            '\xb0\xec\xe0\xd0\x44\x84\x0f\x8a\xf8\x0c\xac\x80\xca\xc6\x8a\x47'
            '\xcc\x6c\x14\xdc\xc1\xc5\x43\x05\xec\x58\x74\x38\x4e\xc5\x0f\x8d'
            '\xfc\x1c\xf0\x58\xc4\x49\xc5\x42\x3c\x74\x00\xf4\x86\x4d\x4d\x4e'
        )

        self.encrypted = (
            '\x7c\x84\x16\x07\xca\xa4\x8e\x2a\xec\xf6\xbe\x76\xdb\x91\xfd\xb2'
            '\xa9\x85\x74\x27\x6e\xd7\x2f\x2f\x3c\xf7\x74\x15\x9a\x56\x11\x2f'
            '\x8e\x6c\x14\x86\x40\x68\x60\x5f\x88\x77\xcb\xc9\xd2\x76\x7c\xba'
            '\xa6\x95\xbb\xf3\xa0\x4d\xaa\x37\xbf\x7b\x84\x15\x3c\x9b\x7a\x8d'
        )

        self.decrypted = (
            '\xab\x99\xaf\x0c\x59\x04\xd1\x53\x4a\xdd\xa5\x49\x3f\x38\xd5\x9f'
            '\x3b\xe1\x9a\xdf\x48\x71\xe6\xd8\x0c\xa2\x8d\x02\xfc\xb6\xd6\xff'
            '\x5b\xb6\x13\x95\xc4\x11\x16\x47\xb6\xd7\x7b\x37\x0f\x61\xcd\xb0'
            '\x5d\x31\x05\x0e\x50\xbf\xc5\xdd\x03\x8c\xd0\x38\x69\xb0\x54\x55'
        )

    def test_decryption1(self):

        lsadecrypt = lsadecryptxp.XP_LsaDecryptMemory(
            self.desxkey, self.feedback)
        decrypted = lsadecrypt.decrypt(self.encrypted)
        self.assertEqual(self.decrypted, decrypted)


if __name__ == '__main__':
    unittest.main()
