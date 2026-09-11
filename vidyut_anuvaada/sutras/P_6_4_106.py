# Sutra प.6.4.106: उतश्च प्रत्ययादसंयोगपूर्वात्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.106"
SUTRA_TEXT = "उतश्च प्रत्ययादसंयोगपूर्वात्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.106: अग्निः'),
		('रामः', '', 'प.6.4.106: रामः'),
		('सीता', '', 'प.6.4.106: सीता'),
	]

