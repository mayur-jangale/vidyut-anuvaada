# Sutra प.8.1.41: शेषे विभाषा
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.41"
SUTRA_TEXT = "शेषे विभाषा"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra8141:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.41: अग्निः'),
		('रामः', '', 'प.8.1.41: रामः'),
		('सीता', '', 'प.8.1.41: सीता'),
	]

