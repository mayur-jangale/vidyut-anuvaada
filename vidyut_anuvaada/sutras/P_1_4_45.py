# Sutra प.1.4.45: आधारोऽधिकरणम्
# (Samjna (technical definitions)) — ADAro'DikaraRam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.45"
SUTRA_TEXT = "आधारोऽधिकरणम्"
SUTRA_DESC = "(Samjna (technical definitions)) — ADAro'DikaraRam"


class Sutra1445:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_45
		return apply_1_4_45(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-adhar-adhikaraNam:अग्निः'),
		('रामः', '', 'not-adhar-adhikaraNam:रामः'),
		('सीता', '', 'not-adhar-adhikaraNam:सीता'),
	]

