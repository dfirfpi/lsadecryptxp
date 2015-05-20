==============
LSA Decrypt XP
==============

Windows NT 5.1 and 5.2 LsaEncryptMemory decryption algorithm.

On NT5, LsaEncryptMemory calls these lsasrv.dll functions: CBC, DESX, DES.
DES and DESX decryption routine are completed, the CBC method is a bit branched,
so only a partial implementation is here. Anyway it should be able to decrypt the
encrypted data, provided you know the DES key 16-rounds scheduling and the IV,
pointed by the debug symbols lsasrv!g_pDESXKey and lsasrv!g_Feedback.


How to use
----------

The decryption routine are included in a single file called *lsadecryptxp.py*.

Inside *lsatest.py* testing code there is a simple example on how to use it.

Licensing and Copyright
-----------------------

Copyright 2015 Francesco "dfirfpi" Picasso. All Rights Reserved.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
02111-1307, USA.

Bugs and Support
----------------

There is no support provided with this software. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE.

For any bug or enhancement please use this site facilities.
