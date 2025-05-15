## Github Action Assignment
Q 1: Automatic Workflow for Docker Image Build and Push:
Workflow Objective:
Create an automated workflow that builds a Docker image and pushes it to the 
Amazon Elastic Container Registry (ECR).
Docker Tagging:
The Docker image should be tagged using the GitHub commit ID. This ensures that 
each image is uniquely identifiable and traceable back to the specific commit that 
generated it.
Trigger Conditions:
The workflow should only be triggered under specific conditions: 
• When changes are made to designated files or folders within the 
repository.
• When actions related to Docker build and Docker push are 
performed.

code:
```
https://github.com/riteshzode18/image-build-push-ecr
```

## error -- ecr repo was getting deleted automatically

Q 2: Develop a Reusable Workflow for Docker Image Build and Push:
• Create a reusable workflow that handles the building and pushing of Docker 
images to the Amazon Elastic Container Registry (ECR).
• Separate the process into two distinct jobs: one dedicated to building the Docker 
image and another dedicated to pushing the Docker image to the ECR.

code:
```
https://github.com/riteshzode18/reusable-workflow-build-push-ecr
```

Q 3: You need to create a GitHub Action workflow that automates the process of 
building Docker images and pushing them to an Amazon ECR (Elastic Container Registry). 
The workflow should be reusable and tailored for three different environments: Dev, QA, 
and Prod. The workflow should trigger manually based on the user's selection of the 
environment.
Steps to Implement
Automatic Workflow Creation:
Build and Push Docker Image: Create a workflow that builds a Docker image and 
pushes it to the ECR registry.
Docker Tag: Use the GitHub commit ID as the Docker tag to ensure each image is 
uniquely identifiable.
Trigger Conditions:
The workflow should trigger only when changes are made to specific files or 
folders relevant to the Docker build and push process.
Reusable Workflow:
• Develop a reusable workflow that can be used across different 
environments for building and pushing Docker images to the ECR registry.
• Split the workflow into two parts: one for building the Docker image and 
another for pushing it to the ECR.
Environment-Specific Workflows:
• Create workflows for three environments: Dev, QA, and Prod.
• These workflows should trigger manually based on user selection.
• Create three folders in your repository for each environment, named as 
follows: dev-YOUR_NAME, qa-YOUR_NAME, prod-YOUR_NAME (e.g., dev-deepak, qa-deepak, prod-deepak).
Folder Structure and Sample Code:
Add the provided sample code to each environment folder in your repository.
Manual Trigger:
Ensure the pipeline triggers manually when a specific environment is selected. For 
example, if the user selects the dev environment, the workflow should trigger and 
build the dev code.

code:
```
https://github.com/riteshzode18/multi-environments-reusable-workflow
```


Q 4: You need to create two workflows and should contains 3 job for each 
environment (Dev, QA and Prod). One workflow should contain only the build job and it 
should get trigger when you created Pull Request and another workflow should contains 
both build and deploy job and it should get trigger when you merged to main branch.
Environment Setup:
• Development (Dev): This is the initial environment where code is built and 
tested by developers.
• Quality Assurance (QA): This environment is used for more rigorous 
testing, typically by a QA team.
• Production (Prod): This is the live environment where the final, approved 
code is deployed.
Folder Structure:
Create three folders in your repository, each corresponding to an environment. 
The folder names should follow the format ENVIRONMENT-YOUR_NAME. For 
example: 
dev-username
qa- username
prod- username
Place the provided sample code in each of these folders.
Workflow Triggers:
• When create a Pull Request:
o When ever you create a pull request and change the python code, 
the pipeline should get trigger.
o It should contain only Build job.
• When merged to main branch:
o Once the Pull Request pipeline success, and merged to the main 
branch, the pipeline should get trigger with build and deploy job.
o It should contain Build and Deploy job.
Jobs in the Workflow:
• Build Job: This job is responsible for building the Docker image and pushing 
it to Amazon Elastic Container Registry (ECR).
• Deployment Job: This job handles the deployment of the Docker image to 
the selected environment. This job should only run manually to ensure 
proper oversight and control.
Manual Triggers and Approvals:
• Dev Environment: No approval is needed. The workflow can be triggered 
manually by any user to build and deploy the code to the Dev environment.
• QA Environment: Requires developer approval. This ensures that only 
code that has passed initial testing in the Dev environment is promoted to 
QA.
• Prod Environment: Requires manager approval. This adds an additional 
layer of oversight to ensure that only thoroughly tested and approved code 
is deployed to the live environment.

note:
i understand the concept we have to use pull request trigger and merge request trigger to run workflow


Q 5: Notify the team with the pipeline details.
• Create a teams channel and notify each and every build status

note: 
we can use webhook to connect with team and send post request to teams
i know the concept but don't know implementation