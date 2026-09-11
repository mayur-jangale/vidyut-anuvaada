# Sutra प.4.4.113: स्रोतसो विभाषा ड्यड्ड्यौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — srotaso viBAzA qyaqqyO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.113"
SUTRA_TEXT = "स्रोतसो विभाषा ड्यड्ड्यौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — srotaso viBAzA qyaqqyO"


class Sutra44113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.113: अग्निः'),
		('रामः', '', 'प.4.4.113: रामः'),
		('सीता', '', 'प.4.4.113: सीता'),
	]

