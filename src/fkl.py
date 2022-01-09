'''
FOCK YOU LIFE(FKL) - asciidea.github.com
- 09/01/2022
- VSCODE
- PYTHON3
'''

import os

class FKL:
	def __init__(self, filename: str):
		self.filename = filename
		self.data = None
		self._tree = {}
		self._latest_section = None
		self._latest_ptr_section = None

		if os.path.exists(self.filename):
			with open(self.filename, 'r') as f:
				self.data = f.readlines()
		
			self.find_sections()
		pass

	def find_sections(self):
		if self.data != None:
			#print(self.data)
			for i in range(len(self.data)):
				line = self.data[i]
				
				if len(line) > 0 and line != '\n' and line[0] != '&':
					if line[0] != '\t':
						self._latest_section = line.replace('\n', '')
						self._tree[self._latest_section] = {}
					else:
						if self._latest_section:
							line_items = line.replace('\t', '').replace('\n', '').split(' ', 1)

							if line_items[0][0] == ';':
								line_items[0] = line_items[0].replace(';', '')
								line_items[1] = int(line_items[1])
							
							if line_items[0][0] == '!':
								line_items[0] = line_items[0].replace('!', '')
								line_items[1] = float(line_items[1].replace(',', '.'))
							
							if line_items[0][0] == '?':
								line_items[0] = line_items[0].replace('?', '')
								if line_items[1] == 'false':
									line_items[1] = False
								else:
									line_items[1] = True
							
							if line_items[0][0] == '*':
								line_items[0] = line_items[0].replace('*', '')
								for j in range(len(self.data)):
									ptr_line = self.data[j]

									if not self._latest_ptr_section:
										if ptr_line[0] == '&':
											#print(ptr_line.replace('&', '').replace('\n', ''), line_items[1])
											if ptr_line.replace('&', '').replace('\n', '') == line_items[1]:
												self._latest_ptr_section = ptr_line.replace('&', '')
												
									else:
										if not type(line_items[1]) is list:
											line_items[1] = []
								
										if ptr_line[0] == '\t':
											line_items[1].append(ptr_line.replace('\t', '').replace('\n', ''))
										else:
											self._latest_ptr_section = None
											

							self._tree[self._latest_section][line_items[0]] = line_items[1]
				else:
					self._latest_section = None
					if line[0] == '\t':
						continue
		pass




#print(FKL('role.fkl')._tree)