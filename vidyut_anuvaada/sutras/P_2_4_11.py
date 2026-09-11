# Sutra प.2.4.11: गवाश्वप्रभृतीनि च
# (Samasa (compound formation)) — gavASvapraBftIni ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.11"
SUTRA_TEXT = "गवाश्वप्रभृतीनि च"
SUTRA_DESC = "(Samasa (compound formation)) — gavASvapraBftIni ca"


class Sutra2411:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

