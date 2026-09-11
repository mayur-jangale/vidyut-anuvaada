# Sutra प.7.1.76: छन्दस्यपि दृश्यते
# (Taddhita (secondary derivations)) — Candasyapi dfSyate

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.76"
SUTRA_TEXT = "छन्दस्यपि दृश्यते"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Candasyapi dfSyate"


class Sutra7176:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.76: अग्निः'),
		('रामः', '', 'प.7.1.76: रामः'),
		('सीता', '', 'प.7.1.76: सीता'),
	]

