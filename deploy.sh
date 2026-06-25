#!/usr/bin/env bash
set -euo pipefail
SERVICE=${1:-genai-mvp}
REGION=${2:-us-central1}
gcloud run deploy "$SERVICE" \
  --source . \
  --region "$REGION" \
  --allow-unauthenticated \
  --set-env-vars "GEMINI_API_KEY=${GEMINI_API_KEY},GEMINI_MODEL=${GEMINI_MODEL:-gemini-3-flash-preview}"
