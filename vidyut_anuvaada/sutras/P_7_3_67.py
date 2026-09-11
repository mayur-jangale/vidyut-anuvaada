# Sutra प.7.3.67: वचोऽशब्दसंज्ञायाम्
# (Taddhita (secondary derivations)) — vaco'SabdasaMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.67"
SUTRA_TEXT = "वचोऽशब्दसंज्ञायाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — vaco'SabdasaMjYAyAm"


class Sutra7367:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.67: अग्निः'),
		('रामः', '', 'प.7.3.67: रामः'),
		('सीता', '', 'प.7.3.67: सीता'),
	]

