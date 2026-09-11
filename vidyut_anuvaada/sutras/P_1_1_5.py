# Sutra प.1.1.5: क्ङिति च
# Also before suffixes marked with ङ् (kṅit)

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.5"
SUTRA_TEXT = "क्ङिति च"
SUTRA_DESC = "Also before suffixes marked with ङ् (kṅit)"


class Sutra115:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_5
		return apply_1_1_5(word, pos)

	EXAMPLES = [
		('गमृ', '', 'lṛdhātu-keeps-ending:गमृ;kṅit-context'),
		('गम्', '', 'regular-root:गम्;kṅit-context'),
	]

