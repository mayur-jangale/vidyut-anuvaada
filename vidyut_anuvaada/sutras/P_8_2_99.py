# Sutra प.8.2.99: प्रतिश्रवणे च
# (Final transformations (tripāḍī)) — pratiSravaRe ca

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.99"
SUTRA_TEXT = "प्रतिश्रवणे च"
SUTRA_DESC = "(Final transformations (tripāḍī)) — pratiSravaRe ca"


class Sutra8299:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.99: अग्निः'),
		('रामः', '', 'प.8.2.99: रामः'),
		('सीता', '', 'प.8.2.99: सीता'),
	]

