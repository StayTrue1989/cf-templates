.PHONY: build

delete-content:
	aws s3 rm s3://<s3-bucket-name> --recursive

upload-content:
	aws s3 sync ./site-content s3://<s3-bucket-name>/production

delete-all:
	aws s3 rm s3://<s3-bucket-name> --recursive 
	sam delete --no-prompts

deploy-and-upload:
	sam deploy --no-confirm-changeset
	aws s3 sync ./site-content s3://<s3-bucket-name>/production
