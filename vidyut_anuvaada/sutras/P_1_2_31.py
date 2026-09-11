# Sutra प.1.2.31: समाहारः स्वरितः
# (Samjna (technical definitions)) — samAhAraH svaritaH

from P_1_2 import apply_1_2_31

SUTRA_CODE = "प.1.2.31"
SUTRA_TEXT = "समाहारः स्वरितः"
SUTRA_DESC = "(Samjna (technical definitions)) — samAhAraH svaritaH"


class Sutra1231:
	def apply(self, word, pos):
		return apply_1_2_31(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-svarita:अग्निः'),
		('रामः', '', 'non-svarita:रामः'),
		('सीता', '', 'non-svarita:सीता'),
	]

