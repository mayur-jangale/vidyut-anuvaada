# Sutra प.3.2.56: आढ्यसुभगस्थूलपलितनग्नान्धप्रियेषु च्व्यर्थेष्वच्वौ कृञः करणे ख्युन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — AQyasuBagasTUlapalitanagnAnDapriyezu cvyarTezvacvO kfYaH karaRe Kyun

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.56"
SUTRA_TEXT = "आढ्यसुभगस्थूलपलितनग्नान्धप्रियेषु च्व्यर्थेष्वच्वौ कृञः करणे ख्युन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — AQyasuBagasTUlapalitanagnAnDapriyezu cvyarTezvacvO kfYaH karaRe Kyun"


class Sutra3256:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

