# Sutra प.8.2.92: अग्नीत्प्रेषणे परस्य च
# (Final transformations (tripāḍī)) — agnItprezaRe parasya ca

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.92"
SUTRA_TEXT = "अग्नीत्प्रेषणे परस्य च"
SUTRA_DESC = "(Final transformations (tripāḍī)) — agnItprezaRe parasya ca"


class Sutra8292:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.92: अग्निः'),
		('रामः', '', 'प.8.2.92: रामः'),
		('सीता', '', 'प.8.2.92: सीता'),
	]

