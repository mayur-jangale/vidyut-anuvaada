# Sutra प.7.1.74: तृतीयादिषु भाषितपुंस्कं पुंवद्गालवस्य
# (Taddhita (secondary derivations)) — tftIyAdizu BAzitapuMskaM puMvadgAlavasya

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.74"
SUTRA_TEXT = "तृतीयादिषु भाषितपुंस्कं पुंवद्गालवस्य"
SUTRA_DESC = "(Taddhita (secondary derivations)) — tftIyAdizu BAzitapuMskaM puMvadgAlavasya"


class Sutra7174:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.74: अग्निः'),
		('रामः', '', 'प.7.1.74: रामः'),
		('सीता', '', 'प.7.1.74: सीता'),
	]

