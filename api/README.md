# Experiments
## AWS Chalice
### Issues
- IAM policy specified in .chalice/config is not deployed
- Generated IAM policy relies on boto3 'client' API calls, high-level api like tables is not detected
- Requires CDK to deploy a data store

### To Try
- use Chalice with CDK

### Solution
- just use the CDK instead and hardcode those IAM policies

