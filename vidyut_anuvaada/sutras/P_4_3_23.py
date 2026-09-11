# Sutra प.4.3.23: सायंचिरम्प्राह्णेप्रगेऽव्ययेभ्यष्ट्युट्युलौ तुट् च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — sAyaMciramprAhReprage'vyayeByazwyuwyulO tuw ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.23"
SUTRA_TEXT = "सायंचिरम्प्राह्णेप्रगेऽव्ययेभ्यष्ट्युट्युलौ तुट् च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — sAyaMciramprAhReprage'vyayeByazwyuwyulO tuw ca"


class Sutra4323:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.23: अग्निः'),
		('रामः', '', 'प.4.3.23: रामः'),
		('सीता', '', 'प.4.3.23: सीता'),
	]

