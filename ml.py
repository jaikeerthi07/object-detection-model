from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="8DKMTrHJx6rbTkPVFfbi"
)

result = client.run_workflow(
    workspace_name="jaikeerthi",
    workflow_id="custom-workflow",
    images={
        "image": "YOUR_IMAGE.jpg"
    },
    use_cache=True # cache workflow definition for 15 minutes
)
