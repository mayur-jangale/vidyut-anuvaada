# Sutra प.2.2.35: सप्तमीविशेषणे बहुव्रीहौ
# (Samasa (compound formation)) — saptamIviSezaRe bahuvrIhO

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.35"
SUTRA_TEXT = "सप्तमीविशेषणे बहुव्रीहौ"
SUTRA_DESC = "(Samasa (compound formation)) — saptamIviSezaRe bahuvrIhO"


class Sutra2235:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

