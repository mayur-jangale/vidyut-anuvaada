# Sutra प.6.4.163: प्रकृत्यैकाच्
# (Sandhi (euphonic combination)) — prakftyEkAc

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.163"
SUTRA_TEXT = "प्रकृत्यैकाच्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — prakftyEkAc"


class Sutra64163:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.163: अग्निः'),
		('रामः', '', 'प.6.4.163: रामः'),
		('सीता', '', 'प.6.4.163: सीता'),
	]

