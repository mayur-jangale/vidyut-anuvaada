# Sutra प.5.4.117: अन्तर्बहिर्भ्यां च लोम्नः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — antarbahirByAM ca lomnaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.117"
SUTRA_TEXT = "अन्तर्बहिर्भ्यां च लोम्नः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — antarbahirByAM ca lomnaH"


class Sutra54117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.117: अग्निः'),
		('रामः', '', 'प.5.4.117: रामः'),
		('सीता', '', 'प.5.4.117: सीता'),
	]

