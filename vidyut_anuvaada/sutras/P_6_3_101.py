# Sutra प.6.3.101: कोः कत् तत्पुरुषेऽचि
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.101"
SUTRA_TEXT = "कोः कत् तत्पुरुषेऽचि"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63101:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.101: अग्निः'),
		('रामः', '', 'प.6.3.101: रामः'),
		('सीता', '', 'प.6.3.101: सीता'),
	]

