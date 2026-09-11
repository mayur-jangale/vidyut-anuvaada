# Sutra प.5.2.114: ज्योत्स्नातमिस्राशृङ्गिणोर्जस्विन्नूर्जस्वलगोमिन्मलिनमलीमसाः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — jyotsnAtamisrASfNgiRorjasvinnUrjasvalagominmalinamalImasAH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.114"
SUTRA_TEXT = "ज्योत्स्नातमिस्राशृङ्गिणोर्जस्विन्नूर्जस्वलगोमिन्मलिनमलीमसाः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — jyotsnAtamisrASfNgiRorjasvinnUrjasvalagominmalinamalImasAH"


class Sutra52114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.114: अग्निः'),
		('रामः', '', 'प.5.2.114: रामः'),
		('सीता', '', 'प.5.2.114: सीता'),
	]

