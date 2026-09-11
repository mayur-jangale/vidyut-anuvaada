# Sutra प.3.4.66: पर्याप्तिवचनेष्वलमर्थेषु
# tavya, anīya — future passive participle suffixes

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.66"
SUTRA_TEXT = "पर्याप्तिवचनेष्वलमर्थेषु"
SUTRA_DESC = "tavya, anīya — future passive participle suffixes"


class Sutra3466:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

