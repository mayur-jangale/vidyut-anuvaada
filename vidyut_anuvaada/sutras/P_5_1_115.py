# Sutra प.5.1.115: तेन तुल्यं क्रिया चेद्वतिः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tena tulyaM kriyA cedvatiH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.115"
SUTRA_TEXT = "तेन तुल्यं क्रिया चेद्वतिः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tena tulyaM kriyA cedvatiH"


class Sutra51115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.115: अग्निः'),
		('रामः', '', 'प.5.1.115: रामः'),
		('सीता', '', 'प.5.1.115: सीता'),
	]

