# Sutra प.6.2.12: द्विगौ प्रमाणे
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.12"
SUTRA_TEXT = "द्विगौ प्रमाणे"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6212:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.12: अग्निः'),
		('रामः', '', 'प.6.2.12: रामः'),
		('सीता', '', 'प.6.2.12: सीता'),
	]

