# Sutra प.8.1.53: विभाषितं सोपसर्गमनुत्तमम्
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.53"
SUTRA_TEXT = "विभाषितं सोपसर्गमनुत्तमम्"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra8153:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.53: अग्निः'),
		('रामः', '', 'प.8.1.53: रामः'),
		('सीता', '', 'प.8.1.53: सीता'),
	]

