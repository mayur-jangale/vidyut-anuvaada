# Sutra प.7.2.65: विभाषा सृजिदृशोः
# (Taddhita (secondary derivations)) — viBAzA sfjidfSoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.65"
SUTRA_TEXT = "विभाषा सृजिदृशोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — viBAzA sfjidfSoH"


class Sutra7265:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.65: अग्निः'),
		('रामः', '', 'प.7.2.65: रामः'),
		('सीता', '', 'प.7.2.65: सीता'),
	]

