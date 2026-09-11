# Sutra प.1.1.24: ष्णान्ता षट्
# (Samjna (technical definitions)) — zRAntA zaw

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.24"
SUTRA_TEXT = "ष्णान्ता षट्"
SUTRA_DESC = "(Samjna (technical definitions)) — zRAntA zaw"


class Sutra1124:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_24
		return apply_1_1_24(word, pos)

	EXAMPLES = [
		('षट्', '', 'non-ṣaṭ:षट्'),
		('दश', '', 'non-ṣaṭ:दश'),
	]

