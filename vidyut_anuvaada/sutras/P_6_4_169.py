# Sutra प.6.4.169: आत्माध्वानौ खे
# (Sandhi (euphonic combination)) — AtmADvAnO Ke

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.169"
SUTRA_TEXT = "आत्माध्वानौ खे"
SUTRA_DESC = "(Sandhi (euphonic combination)) — AtmADvAnO Ke"


class Sutra64169:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.169: अग्निः'),
		('रामः', '', 'प.6.4.169: रामः'),
		('सीता', '', 'प.6.4.169: सीता'),
	]

