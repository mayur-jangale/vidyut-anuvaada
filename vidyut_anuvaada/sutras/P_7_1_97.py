# Sutra प.7.1.97: विभाषा तृतीयादिष्वचि
# (Taddhita (secondary derivations)) — viBAzA tftIyAdizvaci

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.97"
SUTRA_TEXT = "विभाषा तृतीयादिष्वचि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — viBAzA tftIyAdizvaci"


class Sutra7197:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.97: अग्निः'),
		('रामः', '', 'प.7.1.97: रामः'),
		('सीता', '', 'प.7.1.97: सीता'),
	]

