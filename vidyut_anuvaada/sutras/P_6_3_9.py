# Sutra प.6.3.9: हलदन्तात् सप्तम्याः संज्ञायाम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.9"
SUTRA_TEXT = "हलदन्तात् सप्तम्याः संज्ञायाम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra639:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.9: अग्निः'),
		('रामः', '', 'प.6.3.9: रामः'),
		('सीता', '', 'प.6.3.9: सीता'),
	]

