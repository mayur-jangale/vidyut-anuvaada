# Sutra प.8.4.17: नेर्गदनदपतपदघुमास्यतिहन्तियातिवातिद्रातिप्सातिवपतिवहतिशाम्यतिचिनोतिदेग्धिषु च
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.17"
SUTRA_TEXT = "नेर्गदनदपतपदघुमास्यतिहन्तियातिवातिद्रातिप्सातिवपतिवहतिशाम्यतिचिनोतिदेग्धिषु च"
SUTRA_DESC = "final transformations — continued"


class Sutra8417:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.17: अग्निः'),
		('रामः', '', 'प.8.4.17: रामः'),
		('सीता', '', 'प.8.4.17: सीता'),
	]

