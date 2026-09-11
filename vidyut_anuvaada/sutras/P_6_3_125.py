# Sutra प.6.3.125: अष्टनः संज्ञायाम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.125"
SUTRA_TEXT = "अष्टनः संज्ञायाम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63125:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.125: अग्निः'),
		('रामः', '', 'प.6.3.125: रामः'),
		('सीता', '', 'प.6.3.125: सीता'),
	]

