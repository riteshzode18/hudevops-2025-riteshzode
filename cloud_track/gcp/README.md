# Cloud Assignment DAY 1

## Question:1

1. Orchestrate a Data Workflow using Cloud Composer and BigQuery
• Objec@ve: Automate and manage complex data workflows.
• Steps:
a. Create a Cloud Composer environment to manage the workflow.
b. Write a Directed Acyclic Graph (DAG) to automate the following steps:
i. Load data from a Cloud Storage bucket into a BigQuery table.
ii. Run a BigQuery query to transform the data which is already present in 
the cloud.
iii. Export the results to another Cloud Storage bucket.
c. Schedule the DAG to run daily and verify the successful execu5on

## Question:2

C2. Integrate Google Cloud Storage (GCS) with Google Cloud CDN to serve static content efficiently.
• Objective: Set up Google Cloud CDN to cache and serve static content from a Google Cloud 
Storage bucket, improving content delivery performance.
• Steps:
1. Create a Google Cloud Storage Bucket:
- Create a GCS bucket to store your static content.
- Upload some sample static files (e.g., images, HTML, CSS) to the bucket.
2. Configure Bucket Permissions:
- Set the appropriate IAM roles to allow public access to the bucket.
3. Set Up a Load Balancer:
- Create a global HTTP(S) load balancer in Google Cloud.
4. Enable Cloud CDN:
- Configure caching policies to optimize content delivery.
5. Test the Setup:
- Access the static content via the CDN URL and verify that it is being served 
correctly


## Question:3
3. Create a Cloud Func@on to list down the current working directory using the os module and print 
the @me using Cloud Scheduler at an interval of 1 minute.
• Objective: Automate the execution of a Cloud Function that lists the current working directory 
and prints the current time at regular intervals.
• Steps:
a. Create the Cloud Function:
i. Write a Python Cloud Function that uses the os module to list the current 
working directory and prints the current time.
ii. Deploy the Cloud Function to GCP.
b. Set Up Cloud Scheduler:
i. Create a Cloud Scheduler job to trigger the Cloud Function every 1 minute.
ii. Ensure the necessary permissions are set up for Cloud Scheduler to invoke the 
Cloud Function.
c. Verify the Setup:
i. Monitor the Cloud Function logs to ensure it is being triggered every minute and 
is printing the desired output

## Question:4

4. Create a custom Instance Template using gcloud with all the details below-: 
a. Name-: YOUR_FIRSTNAME-hudevops 
b. Boot Disk Size-: 5 GB 
c. Image Family-: debian-10 
d. Machine Type-: n1-standard-1 
e. Image Project-: Debian-cloud
f. Take the screenshot of this once created and delete the resource.

## Question:5

5. Implement an Event-Driven Architecture with Cloud Pub/Sub and Cloud Storage
• Objec5ve: Automate file processing based on events.
• Steps:
a. Create a Pub/Sub topic to receive event no5fica5ons from Cloud Storage.
b. Enable event no5fica5ons on a Cloud Storage bucket to trigger the Pub/Sub 
topic when a new file is uploaded.
c. Write a Cloud Func5on that triggers on Pub/Sub messages and processes the 
uploaded file (e.g., image resizing).
d. Upload a file to the bucket and verify that the event-driven workflow is 
executed
