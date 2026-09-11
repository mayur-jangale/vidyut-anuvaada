# Sutra प.6.2.187: स्फिगपूतवीणाऽञ्जोऽध्वकुक्षिसीरनामनाम च
# (Sandhi (euphonic combination)) — sPigapUtavIRA'Yjo'DvakukzisIranAmanAma ca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.187"
SUTRA_TEXT = "स्फिगपूतवीणाऽञ्जोऽध्वकुक्षिसीरनामनाम च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — sPigapUtavIRA'Yjo'DvakukzisIranAmanAma ca"


class Sutra62187:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.187: अग्निः'),
		('रामः', '', 'प.6.2.187: रामः'),
		('सीता', '', 'प.6.2.187: सीता'),
	]

