# Sutra प.5.4.129: प्रसम्भ्यां जानुनोर्ज्ञुः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — prasamByAM jAnunorjYuH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.129"
SUTRA_TEXT = "प्रसम्भ्यां जानुनोर्ज्ञुः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — prasamByAM jAnunorjYuH"


class Sutra54129:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.129: अग्निः'),
		('रामः', '', 'प.5.4.129: रामः'),
		('सीता', '', 'प.5.4.129: सीता'),
	]

