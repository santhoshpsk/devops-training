The cloudformation template is to host website in EC2 instances.
I have four websites. Those are following.

1. DigitalEx
2. Foste
3. Convid
4. Diffuso

I downloaded these websites html code from https://www.free-css.com/free-css-templates
Anyone wants to replicate this cloudformation can go and download these websites (and many more) from the same link.
After downloading each websites as zip file I rezipped them by removing the starting directory because I want it to place the index.html page directly in /var/www/html/ directory when I unzip it in the EC2 instance. Otherwise the index.html page will be available at /var/www/html/digitalex/ (for an example) directory.

The idea is to deploy any one of these websites in a EC2 instance and make it run using httpd.
During CloudFormation creation, one will have option to select which website to deploy in the corresponding EC2 instance.
The rezipped websites are uploaded to a S3 bucket in the same AWS account.

EC2 instance details:
* Operating System: Amazon Linux 2
* Instance Type: 
  * development instance can use t2.micro
  * production instance can use t2.micro, t2.nano, and t2.small

Optimizations done:
* This cloudformation template will work in any normal regions in AWS. The AMI to use in EC2 instance in different regions are taken from public SSM parameter.
* 