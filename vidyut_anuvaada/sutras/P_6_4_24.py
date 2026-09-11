# Sutra प.6.4.24: अनिदितां हल उपधायाः क्ङिति
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.24"
SUTRA_TEXT = "अनिदितां हल उपधायाः क्ङिति"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6424:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.24: अग्निः'),
		('रामः', '', 'प.6.4.24: रामः'),
		('सीता', '', 'प.6.4.24: सीता'),
	]

