# s3 Boto Usage

This is a directory dedicated to interacting with s3 buckets on AWS using `boto3`

The instructions below assume that you've imported the `boto3` library as demonstrated below:

```bash
akalaj:~/ $ python3

Python 3.7.7 (v3.7.7:d7c567b08f, Mar 10 2020, 02:56:16)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import boto3
```

## Boto Resource Handler

The "resource handler" is the `boto.resource()` function.

This is the basic building block of interacting with AWS.

**Please note**: "Resource Handler" is not an official AWS term.

When  `boto.resource(str)` is called with a `str` argument, for example `'s3'`, a handler object is returned which will allow you to interact and handle a given AWS resource.

Let's see this in action with Python.

```python3
>>> s3 = boto3.resource('s3')
>>> type(s3)
<class 'boto3.resources.factory.s3.ServiceResource'>
```

Notice the lineage of classes here:

`boto3 > resources > factory > s3 > ServiceResource`

Depending on the resource you specify when creating a resource handler, you may get a different object.