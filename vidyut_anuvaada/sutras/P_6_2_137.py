# Sutra प.6.2.137: प्रकृत्या भगालम्
# (Sandhi (euphonic combination)) — prakftyA BagAlam

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.137"
SUTRA_TEXT = "प्रकृत्या भगालम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — prakftyA BagAlam"


class Sutra62137:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.137: अग्निः'),
		('रामः', '', 'प.6.2.137: रामः'),
		('सीता', '', 'प.6.2.137: सीता'),
	]

