# Sutra प.5.4.9: जात्यन्ताच्छ बन्धुनि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — jAtyantAcCa banDuni

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.9"
SUTRA_TEXT = "जात्यन्ताच्छ बन्धुनि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — jAtyantAcCa banDuni"


class Sutra549:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.9: अग्निः'),
		('रामः', '', 'प.5.4.9: रामः'),
		('सीता', '', 'प.5.4.9: सीता'),
	]

