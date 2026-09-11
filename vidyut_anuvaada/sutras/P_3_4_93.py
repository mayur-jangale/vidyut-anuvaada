# Sutra प.3.4.93: एत ऐ
# liṭ ca — liṭ is also sārvadhātuka

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.93"
SUTRA_TEXT = "एत ऐ"
SUTRA_DESC = "liṭ ca — liṭ is also sārvadhātuka"


class Sutra3493:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

