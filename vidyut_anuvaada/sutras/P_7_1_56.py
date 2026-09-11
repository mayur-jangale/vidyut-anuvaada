# Sutra प.7.1.56: श्रीग्रामण्योश्छन्दसि
# (Taddhita (secondary derivations)) — SrIgrAmaRyoSCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.56"
SUTRA_TEXT = "श्रीग्रामण्योश्छन्दसि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — SrIgrAmaRyoSCandasi"


class Sutra7156:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.56: अग्निः'),
		('रामः', '', 'प.7.1.56: रामः'),
		('सीता', '', 'प.7.1.56: सीता'),
	]

