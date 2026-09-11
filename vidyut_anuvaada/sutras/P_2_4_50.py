# Sutra प.2.4.50: विभाषा लुङ्लृङोः
# (Samasa (compound formation)) — viBAzA luNlfNoH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.50"
SUTRA_TEXT = "विभाषा लुङ्लृङोः"
SUTRA_DESC = "(Samasa (compound formation)) — viBAzA luNlfNoH"


class Sutra2450:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

