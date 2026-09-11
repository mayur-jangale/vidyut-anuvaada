# Sutra प.8.1.29: न लुट्
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.29"
SUTRA_TEXT = "न लुट्"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra8129:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.29: अग्निः'),
		('रामः', '', 'प.8.1.29: रामः'),
		('सीता', '', 'प.8.1.29: सीता'),
	]

