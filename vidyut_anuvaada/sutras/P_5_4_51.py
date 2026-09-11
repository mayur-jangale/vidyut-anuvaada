# Sutra प.5.4.51: अरुर्मनश्चक्षुश्चेतोरहोरजसां लोपश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — arurmanaScakzuScetorahorajasAM lopaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.51"
SUTRA_TEXT = "अरुर्मनश्चक्षुश्चेतोरहोरजसां लोपश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — arurmanaScakzuScetorahorajasAM lopaSca"


class Sutra5451:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.51: अग्निः'),
		('रामः', '', 'प.5.4.51: रामः'),
		('सीता', '', 'प.5.4.51: सीता'),
	]

