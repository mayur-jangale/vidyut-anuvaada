# Sutra प.5.4.138: पादस्य लोपोऽहस्त्यादिभ्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pAdasya lopo'hastyAdiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.138"
SUTRA_TEXT = "पादस्य लोपोऽहस्त्यादिभ्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pAdasya lopo'hastyAdiByaH"


class Sutra54138:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.138: अग्निः'),
		('रामः', '', 'प.5.4.138: रामः'),
		('सीता', '', 'प.5.4.138: सीता'),
	]

