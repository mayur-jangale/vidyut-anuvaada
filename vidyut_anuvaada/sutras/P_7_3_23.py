# Sutra प.7.3.23: दीर्घाच्च वरुणस्य
# (Taddhita (secondary derivations)) — dIrGAcca varuRasya

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.23"
SUTRA_TEXT = "दीर्घाच्च वरुणस्य"
SUTRA_DESC = "(Taddhita (secondary derivations)) — dIrGAcca varuRasya"


class Sutra7323:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.23: अग्निः'),
		('रामः', '', 'प.7.3.23: रामः'),
		('सीता', '', 'प.7.3.23: सीता'),
	]

