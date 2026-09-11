# Sutra प.5.1.97: व्युष्टादिभ्योऽण्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vyuzwAdiByo'R

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.97"
SUTRA_TEXT = "व्युष्टादिभ्योऽण्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vyuzwAdiByo'R"


class Sutra5197:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.97: अग्निः'),
		('रामः', '', 'प.5.1.97: रामः'),
		('सीता', '', 'प.5.1.97: सीता'),
	]

