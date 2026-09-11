# Sutra प.5.1.134: गोत्रचरणाच्श्लाघात्याकारतदवेतेषु
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — gotracaraRAcSlAGAtyAkAratadavetezu

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.134"
SUTRA_TEXT = "गोत्रचरणाच्श्लाघात्याकारतदवेतेषु"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — gotracaraRAcSlAGAtyAkAratadavetezu"


class Sutra51134:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.134: अग्निः'),
		('रामः', '', 'प.5.1.134: रामः'),
		('सीता', '', 'प.5.1.134: सीता'),
	]

