The cloudformation template is to host website in EC2 instances.
I have four websites. Those are following.

1. DigitalEx (digitalex.zip)
2. Foste (foste.zip)
3. Convid (convid.zip)
4. Diffuso (diffuso.zip)

I downloaded these websites html code from https://www.free-css.com/free-css-templates
Anyone wants to replicate this cloudformation can go and download these websites (and many more) from the same link.
After downloading each websites as zip file I rezipped them by removing the starting directory because I want it to place the index.html page directly in /var/www/html/ directory when I unzip it in the EC2 instance. Otherwise the index.html page will be available at /var/www/html/digitalex/ (for an example) directory.

The idea is to deploy any one of these websites in a EC2 instance and make it run using httpd.
During CloudFormation creation, one will have option to select which website to deploy in the corresponding EC2 instance.

Steps I have done:
1. Downloaded and reziped the websites above said from the link.
2. Created a S3 bucket to upload the websites' zip files
3. Uploaded rezipped zip files to a S3 bucket in the same AWS account.
4. Created EC2 instances' key pair with the name ec2-keypair (This name is hard coded in the template)
5. Deploy the cloudformation using the template.

Assumptions and Limitations:
* This cloudformation template doesn't specify any security group id to use for EC2 instance. In turn, it will select the default security group of the region while creating EC2 instance. So make sure that the 80 port is allowed in your default security group.
* The websites can be accessed using the EC2 instance's IP address. No DNS is configured in this cfn template and hence No SSL also configured.

EC2 instance details:
* Operating System: Amazon Linux 2
* Instance Type: 
  * development instance can use t2.micro
  * production instance can use t2.micro, t2.nano, and t2.small
 

The AMI to use in EC2 instance in different regions are taken from public SSM parameter.

This cloudformation template will work in any normal regions in AWS. One should make sure few things before deploying this cfn stack:
* Create a EC2 instance key pair with name ec2-keypair in the corresponding region.

Your S3 bucket can be in any region. But one have to provide S3 bucket name and region during the time of cfn stack creation.