# Sutra प.2.4.54: चक्षिङः ख्याञ्
# (Samasa (compound formation)) — cakziNaH KyAY

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.54"
SUTRA_TEXT = "चक्षिङः ख्याञ्"
SUTRA_DESC = "(Samasa (compound formation)) — cakziNaH KyAY"


class Sutra2454:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

