
# A simple script to deploy a GCP Cloud Function

region=australia-southeast2
project=pythia-f8a4
runtime=python312
source=src/
entry_point=nfoursid
service_account=project-service-account@pythia-f8a4.iam.gserviceaccount.com
build_service_account=projects/${project}/serviceAccounts/${service_account}
stage_bucket=pythia-a5a7
docker_repository=projects/pythia-f8a4/locations/australia-southeast2/repositories/docker
timeout=600s
memory=4Gi

# Give the service account permission (object viewer) to the storage bucket (gcf-v2-sources-370885433818-australia-southeast2)
gsutil iam ch serviceAccount:${service_account}:roles/storage.objectViewer gs://gcf-v2-sources-370885433818-australia-southeast2
# (The bucket was created during the first deployment using the below command - which failed due to permission issues, but the bucket was created)
# Annoying that the bucket is created with the wrong permissions, but it is what it is

gcloud functions deploy nfoursid \
    --gen2 \
    --trigger-http \
    --no-allow-unauthenticated \
    --project=$project \
    --region=$region \
    --runtime=$runtime \
    --source=$source \
    --entry-point=$entry_point \
    --service-account=$service_account \
    --run-service-account=$service_account \
    --build-service-account=$build_service_account \
    --stage-bucket=$stage_bucket \
    --docker-repository=$docker_repository \
    --timeout=$timeout \
    --memory=$memory

# gcloud functions remove-iam-policy-binding YOUR_FUNCTION_NAME \
#   --member="allUsers" \
#   --role="roles/cloudfunctions.invoker"

# gcloud functions add-iam-policy-binding YOUR_FUNCTION_NAME \
#   --member="user:harry.schaefer@general-dev.co" \
#   --role="roles/cloudfunctions.invoker"


