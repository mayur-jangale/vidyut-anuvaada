# Sutra प.6.4.156: स्थूलदूरयुवह्रस्वक्षिप्रक्षुद्राणां यणादिपरं पूर्वस्य च गुणः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.156"
SUTRA_TEXT = "स्थूलदूरयुवह्रस्वक्षिप्रक्षुद्राणां यणादिपरं पूर्वस्य च गुणः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64156:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.156: अग्निः'),
		('रामः', '', 'प.6.4.156: रामः'),
		('सीता', '', 'प.6.4.156: सीता'),
	]

