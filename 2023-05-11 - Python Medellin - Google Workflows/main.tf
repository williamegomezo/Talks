provider "google" {
    project = var.project_id
}

resource "google_project_service" "workflows" {
    service            = "workflows.googleapis.com"
    disable_on_destroy = false
}

resource "google_service_account" "workflows_service_account" {
    account_id   = "sa-hello-world-workflow"
    display_name = "Sample Workflows Service Account"
}

resource "google_workflows_workflow" "workflows_example" {
    name            = "sample-workflow"
    region          = "us-central1"
    description     = "A sample workflow"
    service_account = google_service_account.workflows_service_account.id
    source_contents = templatefile("workflow.yaml", {
        project_id  = var.project_id
    })
}


