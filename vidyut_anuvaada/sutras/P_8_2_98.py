# Sutra प.8.2.98: पूर्वं तु भाषायाम्
# (Final transformations (tripāḍī)) — pUrvaM tu BAzAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.98"
SUTRA_TEXT = "पूर्वं तु भाषायाम्"
SUTRA_DESC = "(Final transformations (tripāḍī)) — pUrvaM tu BAzAyAm"


class Sutra8298:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.98: अग्निः'),
		('रामः', '', 'प.8.2.98: रामः'),
		('सीता', '', 'प.8.2.98: सीता'),
	]

