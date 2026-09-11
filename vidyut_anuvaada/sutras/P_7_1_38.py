# Sutra प.7.1.38: क्त्वाऽपि छन्दसि
# (Taddhita (secondary derivations)) — ktvA'pi Candasi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.38"
SUTRA_TEXT = "क्त्वाऽपि छन्दसि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ktvA'pi Candasi"


class Sutra7138:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.38: अग्निः'),
		('रामः', '', 'प.7.1.38: रामः'),
		('सीता', '', 'प.7.1.38: सीता'),
	]

