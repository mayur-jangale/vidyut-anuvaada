# Sutra प.7.2.78: ईडजनोर्ध्वे च
# (Taddhita (secondary derivations)) — IqajanorDve ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.78"
SUTRA_TEXT = "ईडजनोर्ध्वे च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — IqajanorDve ca"


class Sutra7278:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.78: अग्निः'),
		('रामः', '', 'प.7.2.78: रामः'),
		('सीता', '', 'प.7.2.78: सीता'),
	]

