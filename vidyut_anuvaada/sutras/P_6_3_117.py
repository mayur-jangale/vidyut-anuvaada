# Sutra प.6.3.117: वनगिर्योः संज्ञायां कोटरकिंशुलकादीनाम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.117"
SUTRA_TEXT = "वनगिर्योः संज्ञायां कोटरकिंशुलकादीनाम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.117: अग्निः'),
		('रामः', '', 'प.6.3.117: रामः'),
		('सीता', '', 'प.6.3.117: सीता'),
	]

