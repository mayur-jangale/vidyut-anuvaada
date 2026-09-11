# Sutra प.3.4.85: लोटो लङ्वत्
# laṅ — imperfect endings

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.85"
SUTRA_TEXT = "लोटो लङ्वत्"
SUTRA_DESC = "laṅ — imperfect endings"


class Sutra3485:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

