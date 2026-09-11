# Sutra प.7.3.27: नातः परस्य
# (Taddhita (secondary derivations)) — nAtaH parasya

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.27"
SUTRA_TEXT = "नातः परस्य"
SUTRA_DESC = "(Taddhita (secondary derivations)) — nAtaH parasya"


class Sutra7327:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.27: अग्निः'),
		('रामः', '', 'प.7.3.27: रामः'),
		('सीता', '', 'प.7.3.27: सीता'),
	]

