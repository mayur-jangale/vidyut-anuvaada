# Sutra प.5.1.111: अनुप्रवचनादिभ्यश्छः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — anupravacanAdiByaSCaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.111"
SUTRA_TEXT = "अनुप्रवचनादिभ्यश्छः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — anupravacanAdiByaSCaH"


class Sutra51111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.111: अग्निः'),
		('रामः', '', 'प.5.1.111: रामः'),
		('सीता', '', 'प.5.1.111: सीता'),
	]

