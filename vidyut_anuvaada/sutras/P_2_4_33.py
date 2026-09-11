# Sutra प.2.4.33: एतदस्त्रतसोस्त्रतसौ चानुदात्तौ
# (Samasa (compound formation)) — etadastratasostratasO cAnudAttO

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.33"
SUTRA_TEXT = "एतदस्त्रतसोस्त्रतसौ चानुदात्तौ"
SUTRA_DESC = "(Samasa (compound formation)) — etadastratasostratasO cAnudAttO"


class Sutra2433:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

