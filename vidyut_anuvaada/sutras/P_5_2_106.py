# Sutra प.5.2.106: दन्त उन्नत उरच्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — danta unnata urac

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.106"
SUTRA_TEXT = "दन्त उन्नत उरच्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — danta unnata urac"


class Sutra52106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.106: अग्निः'),
		('रामः', '', 'प.5.2.106: रामः'),
		('सीता', '', 'प.5.2.106: सीता'),
	]

