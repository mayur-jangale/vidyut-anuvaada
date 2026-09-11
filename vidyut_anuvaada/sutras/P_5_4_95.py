# Sutra प.5.4.95: ग्रामकौटाभ्यां च तक्ष्णः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — grAmakOwAByAM ca takzRaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.95"
SUTRA_TEXT = "ग्रामकौटाभ्यां च तक्ष्णः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — grAmakOwAByAM ca takzRaH"


class Sutra5495:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.95: अग्निः'),
		('रामः', '', 'प.5.4.95: रामः'),
		('सीता', '', 'प.5.4.95: सीता'),
	]

