# Sutra प.6.2.65: सप्तमीहारिणौ धर्म्येऽहरणे
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.65"
SUTRA_TEXT = "सप्तमीहारिणौ धर्म्येऽहरणे"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6265:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.65: अग्निः'),
		('रामः', '', 'प.6.2.65: रामः'),
		('सीता', '', 'प.6.2.65: सीता'),
	]

