# Sutra प.7.1.83: दृक्स्ववस्स्वतवसां छन्दसि
# (Taddhita (secondary derivations)) — dfksvavassvatavasAM Candasi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.83"
SUTRA_TEXT = "दृक्स्ववस्स्वतवसां छन्दसि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — dfksvavassvatavasAM Candasi"


class Sutra7183:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.83: अग्निः'),
		('रामः', '', 'प.7.1.83: रामः'),
		('सीता', '', 'प.7.1.83: सीता'),
	]

