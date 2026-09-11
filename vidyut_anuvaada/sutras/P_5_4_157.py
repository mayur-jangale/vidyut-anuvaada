# Sutra प.5.4.157: वन्दिते भ्रातुः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vandite BrAtuH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.157"
SUTRA_TEXT = "वन्दिते भ्रातुः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vandite BrAtuH"


class Sutra54157:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.157: अग्निः'),
		('रामः', '', 'प.5.4.157: रामः'),
		('सीता', '', 'प.5.4.157: सीता'),
	]

