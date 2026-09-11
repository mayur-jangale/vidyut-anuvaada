# Sutra प.5.1.129: प्राणभृज्जातिवयोवचनोद्गात्रादिभ्योऽञ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — prARaBfjjAtivayovacanodgAtrAdiByo'Y

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.129"
SUTRA_TEXT = "प्राणभृज्जातिवयोवचनोद्गात्रादिभ्योऽञ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — prARaBfjjAtivayovacanodgAtrAdiByo'Y"


class Sutra51129:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.129: अग्निः'),
		('रामः', '', 'प.5.1.129: रामः'),
		('सीता', '', 'प.5.1.129: सीता'),
	]

