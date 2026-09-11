# Sutra प.7.2.68: विभाषा गमहनविदविशाम्
# (Taddhita (secondary derivations)) — viBAzA gamahanavidaviSAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.68"
SUTRA_TEXT = "विभाषा गमहनविदविशाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — viBAzA gamahanavidaviSAm"


class Sutra7268:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.68: अग्निः'),
		('रामः', '', 'प.7.2.68: रामः'),
		('सीता', '', 'प.7.2.68: सीता'),
	]

