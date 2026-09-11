# Sutra प.7.1.92: सख्युरसम्बुद्धौ
# (Taddhita (secondary derivations)) — saKyurasambudDO

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.92"
SUTRA_TEXT = "सख्युरसम्बुद्धौ"
SUTRA_DESC = "(Taddhita (secondary derivations)) — saKyurasambudDO"


class Sutra7192:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.92: अग्निः'),
		('रामः', '', 'प.7.1.92: रामः'),
		('सीता', '', 'प.7.1.92: सीता'),
	]

