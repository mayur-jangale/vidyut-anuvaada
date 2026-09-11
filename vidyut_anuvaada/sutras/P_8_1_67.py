# Sutra प.8.1.67: पूजनात् पूजितमनुदात्तं काष्ठादिभ्यः
# ṅamo lopaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.67"
SUTRA_TEXT = "पूजनात् पूजितमनुदात्तं काष्ठादिभ्यः"
SUTRA_DESC = "ṅamo lopaḥ — repeated"


class Sutra8167:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.67: अग्निः'),
		('रामः', '', 'प.8.1.67: रामः'),
		('सीता', '', 'प.8.1.67: सीता'),
	]

