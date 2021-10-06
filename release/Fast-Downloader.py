#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2021 Winlows86 <winlows86@pc>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import urllib.request
def main(args):
	print("Fast-Downloader")
	name = input("Введите имя файла_ ")
	url = input("Ссылка на файл_ ")
	try:
		urllib.request.urlretrieve(url, name)
	except:
		print("Загрузка не удалась , проверьте название файла и ссылку")
		print("ВНИМАНИЕ: ссылка должна быть не на сайт , а на файл")
	print("Файл был скачан")
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
