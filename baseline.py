import json
import os
import csv
import re
import argparse
from pathlib import Path
from datetime import datetime

import torch
import jiwer
import matplotlib.pyplot as plt

from nemo.collections.asr.models import EncDecMultiTaskModel
from nemo.utils import logging


# === PALETA PARA LA GRÁFICA ===
PALETTE = {
    "wer": "#FF6B6B",
    "cer": "#4CAF50",
}

# === RUTAS ===
DATASET_DIR = Path("/home/nicommartinez2002/dataset ( este es)")
TRAIN_TSV = DATASET_DIR / "train_spain_balanceado.tsv"
DEV_TSV = DATASET_DIR / "dev_spain_balanceado.tsv"
TEST_TSV = DATASET_DIR / "test_spain_balanceado.tsv"

RESULTS_DIR = Path("/home/nicommartinez2002/thau012/NICOLAS MARTINEZ MARTINEZ PHD/AÑO 1/PRUEBAS FOR ACCENT COMMON VOICE 25/CANARY 1B-V2/BASELINE/resultados")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

MANIFEST_DIR = RESULTS_DIR / "manifests"
MANIFEST_DIR.mkdir(exist_ok=True)

DEFAULT_AUDIO_ROOT = Path("/home/nicommartinez2002/thau012/NICOLAS MARTINEZ MARTINEZ PHD/DATABASE/clips")
DEFAULT_MODEL = "nvidia/canary-1b-v2"


# =========================
# NORMALIZACIÓN
# =========================
def normalize_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\sáéíóúüñ]", " ", text, flags=re.UNICODE)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# =========================
# TSV → MANIFEST (Modificado para extraer la zona/acento)
# =========================
def tsv_to_manifest(tsv_path: Path, manifest_path: Path) -> int:
    count = 0

    with open(tsv_path, "r", encoding="utf-8") as f_in, \
         open(manifest_path, "w", encoding="utf-8") as f_out:

        reader = csv.DictReader(f_in, delimiter="\t")

        for row in reader:
            audio_path = (
                row.get("audio_filepath")
                or row.get("path")
                or row.get("audio")
                or row.get("wav")
            )
            text = row.get("text") or row.get("transcript") or row.get("sentence")
            
            # Buscamos la procedencia en las columnas habituales de acento
            zone = row.get("accent") or row.get("accents") or row.get("zona") or "unknown"

            if audio_path and not Path(audio_path).is_absolute():
                audio_path = str(DEFAULT_AUDIO_ROOT / audio_path)

            if not audio_path or not text:
                continue

            entry = {
                "audio_filepath": str(audio_path),
                "duration": float(row.get("duration", 0.0) or 0.0),
                "text": str(text).strip(),
                "source_lang": "es",
                "target_lang": "es",
                "task": "asr",
                "pnc": "yes",
                "zone": str(zone).strip(), # <-- Guardamos la zona aquí
            }

            f_out.write(json.dumps(entry, ensure_ascii=False) + "\n")
            count += 1

    return count


# =========================
# GRÁFICA
# =========================
def plot_wer_cer(out_path: Path, wer_percent: float, cer_percent: float):
    labels = ["WER", "CER"]
    values = [wer_percent, cer_percent]
    colors = [PALETTE["wer"], PALETTE["cer"]]

    fig, ax = plt.subplots(figsize=(6, 4.5), dpi=130)
    bars = ax.bar(labels, values, color=colors, width=0.55)

    for bar, v in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{v:.2f}%",
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold"
        )

    ax.set_ylabel("Error (%)")
    ax.set_title("WER / CER (Corpus)")
    ax.set_ylim(0, max(values) * 1.2 if max(values) > 0 else 1.0)
    ax.grid(True, axis="y", linestyle=":", alpha=0.5)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    fig.savefig(out_path, bbox_inches="tight")
    plt.close(fig)


# =========================
# MAIN
# =========================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        type=str,
        default=DEFAULT_MODEL,
        help="Ruta a .nemo o nombre del modelo"
    )
    args = parser.parse_args()

    logging.info("=" * 70)
    logging.info("BASELINE Canary-1B-v2 (JIWER STANDARD)")
    logging.info("=" * 70)

    # manifests
    dev_manifest = MANIFEST_DIR / "dev.jsonl"
    test_manifest = MANIFEST_DIR / "test.jsonl"

    logging.info("Convirtiendo DEV...")
    tsv_to_manifest(DEV_TSV, dev_manifest)

    logging.info("Convirtiendo TEST...")
    tsv_to_manifest(TEST_TSV, test_manifest)

    # modelo
    logging.info(f"Cargando modelo: {args.model}")
    if os.path.exists(args.model):
        model = EncDecMultiTaskModel.restore_from(args.model)
    else:
        model = EncDecMultiTaskModel.from_pretrained(args.model)

    model.eval()
    if torch.cuda.is_available():
        model = model.cuda()

    # cargar test
    audio_files = []
    references = []
    zones = [] # <-- Lista para almacenar las zonas de forma emparejada

    with open(test_manifest, "r", encoding="utf-8") as f:
        for line in f:
            entry = json.loads(line)
            audio_files.append(entry["audio_filepath"])
            references.append(entry["text"])
            zones.append(entry.get("zone", "unknown")) # <-- Extraemos la zona del jsonl

    # inferencia
    logging.info(f"Transcribiendo {len(audio_files)} audios...")

    with torch.no_grad():
        hypotheses_raw = model.transcribe(
            audio=audio_files,
            batch_size=16,
            source_lang="es",
            target_lang="es",
            task="asr",
            pnc="yes",
            verbose=True,
        )

    hypotheses = [
        h.text if hasattr(h, "text") else str(h)
        for h in hypotheses_raw
    ]

    # =========================
    # JIWER
    # =========================
    refs = [normalize_text(r) for r in references]
    hyps = [normalize_text(h) for h in hypotheses]

    # Modificado para no perder el rastro de 'zones' al filtrar elementos vacíos
    pairs = [(r, h, z) for r, h, z in zip(refs, hyps, zones) if r.strip()]
    refs, hyps, zones = zip(*pairs)
    refs, hyps, zones = list(refs), list(hyps), list(zones)

    wer_out = jiwer.process_words(refs, hyps)
    cer_out = jiwer.process_characters(refs, hyps)

    wer = wer_out.wer * 100
    cer = cer_out.cer * 100


    # =========================
    # ERROR POR AUDIO (Se añade la clave "zone")
    # =========================
    detailed_errors = []

    for i, (r, h, z) in enumerate(zip(refs, hyps, zones)):
        sample_wer = jiwer.wer(r, h) * 100

        detailed_errors.append({
            "id": i,
            "zone": z, # 🔥 Agregado aquí
            "reference": r,
            "hypothesis": h,
            "wer": round(sample_wer, 4)
        })

    # top 10 peores
    worst_10 = sorted(detailed_errors, key=lambda x: x["wer"], reverse=True)[:10]


    # =========================
    # OUTPUT
    # =========================
    timestamp = datetime.now().strftime("%Y%m%dT%H%M%SZ")

    results_file = RESULTS_DIR / f"baseline_test_{timestamp}.json"
    summary_file = RESULTS_DIR / "summary.json"
    plot_file = RESULTS_DIR / "wer_cer_corpus.png"

    summary = {
        "timestamp": timestamp,
        "model": args.model,
        "dataset": "test_spain_balanceado",
        "n_samples": len(refs),

        "wer_micro": round(wer, 4),
        "cer_micro": round(cer, 4),

        "wer_substitutions": wer_out.substitutions,
        "wer_deletions": wer_out.deletions,
        "wer_insertions": wer_out.insertions,

        "cer_substitutions": cer_out.substitutions,
        "cer_deletions": cer_out.deletions,
        "cer_insertions": cer_out.insertions,

        "details": detailed_errors,
        "worst_10": worst_10,
    }

    with open(results_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    plot_wer_cer(plot_file, wer, cer)

    logging.info("=" * 70)
    logging.info("✓ BASELINE COMPLETADO (JIWER)")
    logging.info(f"WER: {wer:.2f}%")
    logging.info(f"CER: {cer:.2f}%")
    logging.info(f"Resultados: {results_file}")
    logging.info(f"Summary: {summary_file}")
    logging.info(f"Gráfica: {plot_file}")
    logging.info("=" * 70)


if __name__ == "__main__":
    main()