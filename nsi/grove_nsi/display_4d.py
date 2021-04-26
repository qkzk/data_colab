_SEG = bytearray(b'\x3F\x06\x5B\x4F\x66\x6D\x7D\x07\x7F\x6F\x00\x40')

class D4AFF7SEG(object):
	def __init__(self, clk, dio, brightness=7):
		self._c = clk
		self._d = dio
		self._b = max(0, min(brightness, 7))
		self._data_cmd()
		self._dsp_ctrl()

	def _start(self):
		self._d.write_digital(0)
		self._c.write_digital(0)

	def _stop(self):
		self._d.write_digital(0)
		self._c.write_digital(1)
		self._d.write_digital(1)

	def _data_cmd(self):
		self._start()
		self._write_byte(0x40)
		self._stop()

	def _dsp_ctrl(self):
		self._start()
		self._write_byte(0x88 | self._b)
		self._stop()

	def _write_byte(self, b):
		for i in range(8):
			self._d.write_digital((b >> i) & 1)
			self._c.write_digital(1)
			self._c.write_digital(0)
		self._c.write_digital(0)
		self._c.write_digital(1)
		self._c.write_digital(0)

	def brightness(self, val=None):
		if val is None:
			return self._b
		self._b = max(0, min(val, 7))
		self._data_cmd()
		self._dsp_ctrl()

	def write(self, segments, pos=0):
		if not 0 <= pos <= 3:
			raise ValueError("Position out of range")
		self._data_cmd()
		self._start()
		self._write_byte(0xC0 | pos)
		for seg in segments:
			self._write_byte(seg)
		self._stop()
		self._dsp_ctrl()

	def encode_string(self, string):
		segments = bytearray(len(string))
		for i in range(len(string)):
			segments[i] = self.encode_char(string[i])
		return segments

	def encode_char(self, char):
		o = ord(char)
		if o == 32:
			return _SEG[10] # space
		if o == 45:
			return _SEG[11] # dash
		if o >= 48 and o <= 57:
			return _SEG[o-48] # 0-9
		raise ValueError("Character out of range: {:d} '{:s}'".format(o, chr(o)))

	def affiche(self, num):
		num = max(-999, min(num, 9999))
		string = '{0: >4d}'.format(num)
		self.write(self.encode_string(string))

	def affiche_2(self, num1, num2, colon=True):
		num1 = max(-9, min(num1, 99))
		num2 = max(-9, min(num2, 99))
		segments = self.encode_string('{0:0>2d}{1:0>2d}'.format(num1, num2))
		if colon:
			segments[1] |= 0x80 # colon on
		self.write(segments)




	
