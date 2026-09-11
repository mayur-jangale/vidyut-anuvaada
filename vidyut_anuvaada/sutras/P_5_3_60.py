# Sutra प.5.3.60: प्रशस्यस्य श्रः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — praSasyasya SraH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.60"
SUTRA_TEXT = "प्रशस्यस्य श्रः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — praSasyasya SraH"


class Sutra5360:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.60: अग्निः'),
		('रामः', '', 'प.5.3.60: रामः'),
		('सीता', '', 'प.5.3.60: सीता'),
	]

