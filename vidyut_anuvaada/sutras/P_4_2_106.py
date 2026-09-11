# Sutra प.4.2.106: तीररूप्योत्तरपदादञ्ञौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tIrarUpyottarapadAdaYYO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.106"
SUTRA_TEXT = "तीररूप्योत्तरपदादञ्ञौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tIrarUpyottarapadAdaYYO"


class Sutra42106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.106: अग्निः'),
		('रामः', '', 'प.4.2.106: रामः'),
		('सीता', '', 'प.4.2.106: सीता'),
	]

