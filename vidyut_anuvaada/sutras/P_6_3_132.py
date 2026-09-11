# Sutra प.6.3.132: ओषधेश्च विभक्तावप्रथमायाम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.132"
SUTRA_TEXT = "ओषधेश्च विभक्तावप्रथमायाम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63132:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.132: अग्निः'),
		('रामः', '', 'प.6.3.132: रामः'),
		('सीता', '', 'प.6.3.132: सीता'),
	]

