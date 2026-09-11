# Sutra प.1.1.12: अदसो मात्
# The pronoun adas (that) has māt as its base

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.12"
SUTRA_TEXT = "अदसो मात्"
SUTRA_DESC = "The pronoun adas (that) has māt as its base"


class Sutra1112:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_12
		return apply_1_1_12(word, pos)

	EXAMPLES = [
		('अदस्', '', 'मात््'),
		('अदस्मिन्', '', 'मात््मिन्'),
		('देव', '', 'देव'),
	]

