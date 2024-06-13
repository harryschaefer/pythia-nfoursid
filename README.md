# Pythia N4SID

The implemention of N4SID, interacted with via a concise API, for utilisation within Pythia's black-boxed IBR identification scheme.

## nfoursid

Functionality forked from [spmvg:nfoursid](https://github.com/spmvg/nfoursid).

## notebook

Primarily for local development, including extensions of the classes implemented in nfoursid, complete with plotting and interactivity functionality.

## local-docker

For local development, implementing functionality to expose the nfoursid API locally via a docker-compose deployment.

To run:
```
docker compose --project-directory local-docker up --build
```

## gcp-deploy.sh

Code to carry the API to a GCP Cloud Function deployment. Must be authentication to run.
```
gcloud auth login
gcloud config set project pythia-f8a4
```
