# Sutra प.1.1.58: न पदान्तद्विर्वचनवरेयलोपस्वरसवर्णानुस्वारदीर्घजश्चर्विधिषु
# (Samjna (technical definitions)) — na padAntadvirvacanavareyalopasvarasavarRAnusvAradIrGajaScarviDizu

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.58"
SUTRA_TEXT = "न पदान्तद्विर्वचनवरेयलोपस्वरसवर्णानुस्वारदीर्घजश्चर्विधिषु"
SUTRA_DESC = "(Samjna (technical definitions)) — na padAntadvirvacanavareyalopasvarasavarRAnusvAradIrGajaScarviDizu"


class Sutra1158:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_58
		return apply_1_1_58(word, pos)

	EXAMPLES = [
		('पद', '', 'प.1.1.58:na-padAntadvir-vacana-reya-lopa-svara-savarṇa-anusvāra-dīrgha-jaścarvidhiṣu;input=पद'),
		('अग्नि', '', 'प.1.1.58:na-padAntadvir-vacana-reya-lopa-svara-savarṇa-anusvāra-dīrgha-jaścarvidhiṣu;input=अग्नि'),
	]

