# cf-templates


### Getting Started


* Rename samconfig_template.toml to samconfig.toml
* Update the s3_bucket parameter from the template.toml file (Substitute the S3 bucket you want to use for saving state data)

```
Example CLI command to run this template:
    sam deploy --parameter-overrides "TargetHostedZoneId=<MyHostedZoneID>"
```

```
  Example of calling this template from Github Actions. The Bitbucket Pipelines pipe is very similar.
  - name: Deploy to AWS CloudFormation
  uses: aws-actions/aws-cloudformation-github-deploy@v1
  with:
    name: MyStackName
    template: cloudfront-with-s3-origin-template.yaml
    parameter-overrides: "MyParam1=myValue,TargetHostedZoneId=${{ secrets.MY_SECRET_VALUE }}"
```Rename samconfig_template.toml to samconfig.toml
