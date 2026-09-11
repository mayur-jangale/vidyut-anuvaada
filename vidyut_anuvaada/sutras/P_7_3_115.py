# Sutra प.7.3.115: विभाषा द्वितीयातृतीयाभ्याम्
# (Taddhita (secondary derivations)) — viBAzA dvitIyAtftIyAByAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.115"
SUTRA_TEXT = "विभाषा द्वितीयातृतीयाभ्याम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — viBAzA dvitIyAtftIyAByAm"


class Sutra73115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.115: अग्निः'),
		('रामः', '', 'प.7.3.115: रामः'),
		('सीता', '', 'प.7.3.115: सीता'),
	]

