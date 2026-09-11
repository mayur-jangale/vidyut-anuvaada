# Sutra प.5.3.39: पूर्वाधरावराणामसि पुरधवश्चैषाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pUrvADarAvarARAmasi puraDavaScEzAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.39"
SUTRA_TEXT = "पूर्वाधरावराणामसि पुरधवश्चैषाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pUrvADarAvarARAmasi puraDavaScEzAm"


class Sutra5339:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.39: अग्निः'),
		('रामः', '', 'प.5.3.39: रामः'),
		('सीता', '', 'प.5.3.39: सीता'),
	]

