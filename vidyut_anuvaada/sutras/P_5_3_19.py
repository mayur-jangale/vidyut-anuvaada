# Sutra प.5.3.19: तदो दा च
# ya — made of (kāṃsya-ya → kāṃsyeya)

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.19"
SUTRA_TEXT = "तदो दा च"
SUTRA_DESC = "ya — made of (kāṃsya-ya → kāṃsyeya)"


class Sutra5319:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.19: अग्निः'),
		('रामः', '', 'प.5.3.19: रामः'),
		('सीता', '', 'प.5.3.19: सीता'),
	]

