# Multi-Account AWS EC2 Disk Utilization Monitoring

This project provides a solution to monitor disk utilization across multiple AWS accounts using Ansible. The solution leverages AWS IAM roles for cross-account access, collects disk utilization metrics, and stores the data in a centralized location for reporting.

## Table of Contents
1. [Architecture](#architecture)
2. [Prerequisites](#prerequisites)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Components](#components)

## Architecture

![Architecture Diagram](architecture-diagram.png)

## Prerequisites

- AWS CLI installed and configured with access to the required accounts.
- Ansible installed on the control machine.
- Python and necessary libraries installed for generating reports.

## Setup

1. **Create IAM Roles in Each AWS Account:**
   - Create a role named `EC2MonitoringRole` in each AWS account.
   - Attach the following policy to the role:

   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "ec2:DescribeInstances",
                   "cloudwatch:GetMetricData"
               ],
               "Resource": "*"
           }
       ]
   }

## Set the trust relationship to allow the Ansible control machine to assume the role:
   
   ```json
   {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<AnsibleControlMachineAccountID>:root"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
