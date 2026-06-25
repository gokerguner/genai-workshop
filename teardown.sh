#!/usr/bin/env bash
set -euo pipefail
SERVICE=${1:-genai-mvp}
REGION=${2:-us-central1}
gcloud run services delete "$SERVICE" --region "$REGION" --quiet
echo "Servis silindi. Maliyet riski yok."
