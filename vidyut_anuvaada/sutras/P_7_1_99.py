# Sutra प.7.1.99: अम् सम्बुद्धौ
# (Taddhita (secondary derivations)) — am sambudDO

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.99"
SUTRA_TEXT = "अम् सम्बुद्धौ"
SUTRA_DESC = "(Taddhita (secondary derivations)) — am sambudDO"


class Sutra7199:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.99: अग्निः'),
		('रामः', '', 'प.7.1.99: रामः'),
		('सीता', '', 'प.7.1.99: सीता'),
	]

