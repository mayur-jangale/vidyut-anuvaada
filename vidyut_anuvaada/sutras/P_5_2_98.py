# Sutra प.5.2.98: वत्सांसाभ्यां कामबले
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vatsAMsAByAM kAmabale

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.98"
SUTRA_TEXT = "वत्सांसाभ्यां कामबले"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vatsAMsAByAM kAmabale"


class Sutra5298:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.98: अग्निः'),
		('रामः', '', 'प.5.2.98: रामः'),
		('सीता', '', 'प.5.2.98: सीता'),
	]

