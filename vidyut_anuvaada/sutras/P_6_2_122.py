# Sutra प.6.2.122: कंसमन्थशूर्पपाय्यकाण्डं द्विगौ
# (Sandhi (euphonic combination)) — kaMsamanTaSUrpapAyyakARqaM dvigO

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.122"
SUTRA_TEXT = "कंसमन्थशूर्पपाय्यकाण्डं द्विगौ"
SUTRA_DESC = "(Sandhi (euphonic combination)) — kaMsamanTaSUrpapAyyakARqaM dvigO"


class Sutra62122:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.122: अग्निः'),
		('रामः', '', 'प.6.2.122: रामः'),
		('सीता', '', 'प.6.2.122: सीता'),
	]

