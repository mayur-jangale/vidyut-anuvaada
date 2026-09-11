# Sutra प.7.2.17: विभाषा भावादिकर्मणोः
# (Taddhita (secondary derivations)) — viBAzA BAvAdikarmaRoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.17"
SUTRA_TEXT = "विभाषा भावादिकर्मणोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — viBAzA BAvAdikarmaRoH"


class Sutra7217:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.17: अग्निः'),
		('रामः', '', 'प.7.2.17: रामः'),
		('सीता', '', 'प.7.2.17: सीता'),
	]

