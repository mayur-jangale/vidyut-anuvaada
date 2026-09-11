# Sutra प.5.1.3: कम्बलाच्च संज्ञायाम्
# strīpratyaya — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.3"
SUTRA_TEXT = "कम्बलाच्च संज्ञायाम्"
SUTRA_DESC = "strīpratyaya — continued"


class Sutra513:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.3: अग्निः'),
		('रामः', '', 'प.5.1.3: रामः'),
		('सीता', '', 'प.5.1.3: सीता'),
	]

