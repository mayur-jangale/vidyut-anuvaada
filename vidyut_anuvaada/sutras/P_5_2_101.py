# Sutra प.5.2.101: प्रज्ञाश्रद्धार्चाभ्यो णः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — prajYASradDArcAByo RaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.101"
SUTRA_TEXT = "प्रज्ञाश्रद्धार्चाभ्यो णः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — prajYASradDArcAByo RaH"


class Sutra52101:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.101: अग्निः'),
		('रामः', '', 'प.5.2.101: रामः'),
		('सीता', '', 'प.5.2.101: सीता'),
	]

