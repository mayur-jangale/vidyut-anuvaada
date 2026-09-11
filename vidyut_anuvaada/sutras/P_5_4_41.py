# Sutra प.5.4.41: वृकज्येष्ठाभ्यां तिल्तातिलौ च च्छन्दसि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vfkajyezWAByAM tiltAtilO ca cCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.41"
SUTRA_TEXT = "वृकज्येष्ठाभ्यां तिल्तातिलौ च च्छन्दसि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vfkajyezWAByAM tiltAtilO ca cCandasi"


class Sutra5441:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.41: अग्निः'),
		('रामः', '', 'प.5.4.41: रामः'),
		('सीता', '', 'प.5.4.41: सीता'),
	]

