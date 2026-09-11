# Sutra प.6.3.51: वा शोकष्यञ्रोगेषु
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.51"
SUTRA_TEXT = "वा शोकष्यञ्रोगेषु"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6351:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.51: अग्निः'),
		('रामः', '', 'प.6.3.51: रामः'),
		('सीता', '', 'प.6.3.51: सीता'),
	]

