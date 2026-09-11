# Sutra प.8.1.33: अङ्गाप्रातिलोम्ये
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.33"
SUTRA_TEXT = "अङ्गाप्रातिलोम्ये"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra8133:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.33: अग्निः'),
		('रामः', '', 'प.8.1.33: रामः'),
		('सीता', '', 'प.8.1.33: सीता'),
	]

