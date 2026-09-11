# Sutra प.5.4.57: अव्यक्तानुकरणाद्द्व्यजवरार्धादनितौ डाच्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — avyaktAnukaraRAddvyajavarArDAdanitO qAc

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.57"
SUTRA_TEXT = "अव्यक्तानुकरणाद्द्व्यजवरार्धादनितौ डाच्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — avyaktAnukaraRAddvyajavarArDAdanitO qAc"


class Sutra5457:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.57: अग्निः'),
		('रामः', '', 'प.5.4.57: रामः'),
		('सीता', '', 'प.5.4.57: सीता'),
	]

