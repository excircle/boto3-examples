# AWS Boto3 Examples

This is a repository of some example code that I've written to interact with AWS.

## How to install boto3 using Python3 with MacOS

On my machine, I installed Python3 using the Python installer found at the Python website.

https://www.python.org/downloads/mac-osx/

Once you have that installed, MacOS will typically provide you access to this installation via the `python3` symlink. An example is provided below:

```bash
akalaj:~/ $ whereis python3
/usr/bin/python3
```

I've found that the easiest way to install Python packages to a specific installation of Python is to use the `-m` module flag + `pip`

By running `python3 -m pip` on your mac, you will invoke the correct version of Python, and successfully call on the `pip` package without needing to hunt your system for the actual binary location.

Full command below:

```bash
akalaj:~/ $ python3 -m pip install boto3
```

## How to install the AWS CLI on MacOS

The installation of the AWS CLI on MacOS is super easy.

Simply visit the AWS website and visit the `.pkg` URL to immediately begin installing the `aws` binary on your machine

For the latest version of the AWS CLI: https://awscli.amazonaws.com/AWSCLIV2.pkg

Once you've installed the AWS CLI on your machine, make sure you use the tool to configure your AWS access creds.

An example configuration is provided below:

```bash
akalaj:~/ $ aws configure

AWS Access Key ID [None]: <access_key>
AWS Secret Access Key [None]: <secret_key>
Default region name [None]: us-east-2
Default output format [None]: yaml
```

# How To BOTO!!!

Using Boto3 with AWS s3