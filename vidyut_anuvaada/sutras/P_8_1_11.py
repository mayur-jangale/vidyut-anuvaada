# Sutra प.8.1.11: कर्मधारयवत् उत्तरेषु
# ṅamo lopaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.11"
SUTRA_TEXT = "कर्मधारयवत् उत्तरेषु"
SUTRA_DESC = "ṅamo lopaḥ — repeated"


class Sutra8111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.11: अग्निः'),
		('रामः', '', 'प.8.1.11: रामः'),
		('सीता', '', 'प.8.1.11: सीता'),
	]

