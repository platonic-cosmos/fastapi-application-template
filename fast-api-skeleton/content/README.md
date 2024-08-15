# ${{ values.app_name }}
${{ values.description }}

## Details
Running in GCP project ${{ values.project_id }} in Cloud Run service with Cloud Spanner as the data store. ${{ values.description | capitalize}}.

## Technology Stack
* Core Technology: Python
* Service API Framework: FastAPI
* Web Server: Uvicorn
* GCP Project: ${{ values.project_id }}
* Container Runtime Platform: Google Cloud Run
* Data Store: Cloud Spanner
* Instrumentation: Google Cloud Logging
