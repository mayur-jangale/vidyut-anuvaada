# Sutra प.8.3.105: स्तुतस्तोमयोश्छन्दसि
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.105"
SUTRA_TEXT = "स्तुतस्तोमयोश्छन्दसि"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra83105:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.105: अग्निः'),
		('रामः', '', 'प.8.3.105: रामः'),
		('सीता', '', 'प.8.3.105: सीता'),
	]

