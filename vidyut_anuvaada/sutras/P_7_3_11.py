# Sutra प.7.3.11: अवयवादृतोः
# (Taddhita (secondary derivations)) — avayavAdftoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.11"
SUTRA_TEXT = "अवयवादृतोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — avayavAdftoH"


class Sutra7311:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.11: अग्निः'),
		('रामः', '', 'प.7.3.11: रामः'),
		('सीता', '', 'प.7.3.11: सीता'),
	]

