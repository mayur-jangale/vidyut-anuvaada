# Sutra प.7.2.15: यस्य विभाषा
# (Taddhita (secondary derivations)) — yasya viBAzA

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.15"
SUTRA_TEXT = "यस्य विभाषा"
SUTRA_DESC = "(Taddhita (secondary derivations)) — yasya viBAzA"


class Sutra7215:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.15: अग्निः'),
		('रामः', '', 'प.7.2.15: रामः'),
		('सीता', '', 'प.7.2.15: सीता'),
	]

