# Sutra प.6.3.12: अमूर्धमस्तकात् स्वाङ्गादकामे
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.12"
SUTRA_TEXT = "अमूर्धमस्तकात् स्वाङ्गादकामे"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6312:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.12: अग्निः'),
		('रामः', '', 'प.6.3.12: रामः'),
		('सीता', '', 'प.6.3.12: सीता'),
	]

