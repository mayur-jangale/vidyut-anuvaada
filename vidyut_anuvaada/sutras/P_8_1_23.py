# Sutra प.8.1.23: त्वामौ द्वितीयायाः
# ṅamo lopaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.23"
SUTRA_TEXT = "त्वामौ द्वितीयायाः"
SUTRA_DESC = "ṅamo lopaḥ — repeated"


class Sutra8123:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.23: अग्निः'),
		('रामः', '', 'प.8.1.23: रामः'),
		('सीता', '', 'प.8.1.23: सीता'),
	]

