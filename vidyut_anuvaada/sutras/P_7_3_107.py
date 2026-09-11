# Sutra प.7.3.107: अम्बाऽर्थनद्योर्ह्रस्वः
# (Taddhita (secondary derivations)) — ambA'rTanadyorhrasvaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.107"
SUTRA_TEXT = "अम्बाऽर्थनद्योर्ह्रस्वः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ambA'rTanadyorhrasvaH"


class Sutra73107:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.107: अग्निः'),
		('रामः', '', 'प.7.3.107: रामः'),
		('सीता', '', 'प.7.3.107: सीता'),
	]

