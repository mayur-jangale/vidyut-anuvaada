# Sutra प.7.3.106: सम्बुद्धौ च
# (Taddhita (secondary derivations)) — sambudDO ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.106"
SUTRA_TEXT = "सम्बुद्धौ च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — sambudDO ca"


class Sutra73106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.106: अग्निः'),
		('रामः', '', 'प.7.3.106: रामः'),
		('सीता', '', 'प.7.3.106: सीता'),
	]

