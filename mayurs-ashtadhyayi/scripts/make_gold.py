"""Regenerate mayur/gold/ramayana_bala_1.json from the DCS file for Ram, Ba, 1."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from mayur import resources
from mayur.dcs import compact_orthography, iter_sentences, pada_form
from mayur.translit import iast_to_slp1, to_deva

fp = next((resources.data_dir() / "dcs/sanskrit/dcs/data/conllu/files/Rāmāyaṇa").glob("*-0000-*.conllu"))
verses: dict[int, dict] = {}
for s in iter_sentences(fp):
    n = s["sent_counter"]
    slp = iast_to_slp1(s["text"].replace("ṁ", "ṃ"))
    comp = compact_orthography(slp)
    line = {"text_iast": s["text"], "text_slp1": slp, "compact_slp1": comp, "compact_deva": to_deva(comp),
            "words": [{"form": pada_form(t["unsandhied"], t["lemma"]), "lemma": t["lemma"], "upos": t["upos"],
                       "feats": t["feats"], "compound_member": t["is_compound_member"]} for t in s["tokens"]]}
    v = verses.setdefault(n, {"id": f"R.1.1.{n}", "number": n, "lines": []})
    v["lines"].append(line)
out = {"source": "Digital Corpus of Sanskrit (Oliver Hellwig), Rāmāyaṇa, Bā 1", "license": "CC BY 4.0",
       "verses": [verses[k] for k in sorted(k for k in verses if k is not None)]}
dst = Path(__file__).resolve().parent.parent / "mayur/gold/ramayana_bala_1.json"
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(out["verses"]), "verses", dst.stat().st_size, "bytes")
