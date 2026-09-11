# Sutra प.7.2.25: अभेश्चाविदूर्ये
# (Taddhita (secondary derivations)) — aBeScAvidUrye

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.25"
SUTRA_TEXT = "अभेश्चाविदूर्ये"
SUTRA_DESC = "(Taddhita (secondary derivations)) — aBeScAvidUrye"


class Sutra7225:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.25: अग्निः'),
		('रामः', '', 'प.7.2.25: रामः'),
		('सीता', '', 'प.7.2.25: सीता'),
	]

