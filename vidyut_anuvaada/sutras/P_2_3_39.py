# Sutra प.2.3.39: स्वामीश्वराधिपतिदायादसाक्षिप्रतिभूप्रसूतैश्च
# (Samasa (compound formation)) — svAmISvarADipatidAyAdasAkzipratiBUprasUtESca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.39"
SUTRA_TEXT = "स्वामीश्वराधिपतिदायादसाक्षिप्रतिभूप्रसूतैश्च"
SUTRA_DESC = "(Samasa (compound formation)) — svAmISvarADipatidAyAdasAkzipratiBUprasUtESca"


class Sutra2339:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

