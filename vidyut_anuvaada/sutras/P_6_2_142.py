# Sutra प.6.2.142: नोत्तरपदेऽनुदात्तादावपृथिवीरुद्रपूषमन्थिषु
# (Sandhi (euphonic combination)) — nottarapade'nudAttAdAvapfTivIrudrapUzamanTizu

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.142"
SUTRA_TEXT = "नोत्तरपदेऽनुदात्तादावपृथिवीरुद्रपूषमन्थिषु"
SUTRA_DESC = "(Sandhi (euphonic combination)) — nottarapade'nudAttAdAvapfTivIrudrapUzamanTizu"


class Sutra62142:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.142: अग्निः'),
		('रामः', '', 'प.6.2.142: रामः'),
		('सीता', '', 'प.6.2.142: सीता'),
	]

