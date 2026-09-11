# Sutra प.6.3.18: शयवासवासिष्वकालात्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.18"
SUTRA_TEXT = "शयवासवासिष्वकालात्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6318:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.18: अग्निः'),
		('रामः', '', 'प.6.3.18: रामः'),
		('सीता', '', 'प.6.3.18: सीता'),
	]

