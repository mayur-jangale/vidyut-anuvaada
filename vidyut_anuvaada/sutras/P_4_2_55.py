# Sutra प.4.2.55: सोऽस्यादिरिति च्छन्दसः प्रगाथेषु
# (Sup-sthāna (nominal endings) and kṛt-affixes) — so'syAdiriti cCandasaH pragATezu

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.55"
SUTRA_TEXT = "सोऽस्यादिरिति च्छन्दसः प्रगाथेषु"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — so'syAdiriti cCandasaH pragATezu"


class Sutra4255:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.55: अग्निः'),
		('रामः', '', 'प.4.2.55: रामः'),
		('सीता', '', 'प.4.2.55: सीता'),
	]

