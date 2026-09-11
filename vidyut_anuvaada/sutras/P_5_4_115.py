# Sutra प.5.4.115: द्वित्रिभ्यां ष मूर्ध्नः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvitriByAM za mUrDnaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.115"
SUTRA_TEXT = "द्वित्रिभ्यां ष मूर्ध्नः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvitriByAM za mUrDnaH"


class Sutra54115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.115: अग्निः'),
		('रामः', '', 'प.5.4.115: रामः'),
		('सीता', '', 'प.5.4.115: सीता'),
	]

