# Sutra प.6.3.78: सहस्य सः संज्ञायाम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.78"
SUTRA_TEXT = "सहस्य सः संज्ञायाम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6378:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.78: अग्निः'),
		('रामः', '', 'प.6.3.78: रामः'),
		('सीता', '', 'प.6.3.78: सीता'),
	]

