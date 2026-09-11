# Sutra प.2.2.3: द्वितीयतृतीयचतुर्थतुर्याण्यन्यतरस्याम्
# (Samasa (compound formation)) — dvitIyatftIyacaturTaturyARyanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.3"
SUTRA_TEXT = "द्वितीयतृतीयचतुर्थतुर्याण्यन्यतरस्याम्"
SUTRA_DESC = "(Samasa (compound formation)) — dvitIyatftIyacaturTaturyARyanyatarasyAm"


class Sutra223:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

