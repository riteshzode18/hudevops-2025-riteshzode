## Jenkins

Q1 . Sample pipeline to build Docker image and Docker push.
- Create a GitHub repository.
- Build the sample application - Backend-Service.
- Push to private Docker registry.


Q 2. Scheduled pipeline in Jenkins
- Change the previous pipeline to schedule-based pipeline.
- Pipeline should trigger every 5 minutes.


Q 3. Multistage Jenkins pipeline and handling secrets as parameters
- Create a multistage pipeline that includes stages for building, testing, and deploying an 
application.
- Configure the pipeline to handle secrets securely using Jenkins credentials.


Q 4. Create a Multiple Jenkins pipeline for Build and Deploy stage.
- Create a one pipeline for build the docker image and another pipeline for deploy 
the application.
- Once the build pipeline is successfully completed, trigger the deploy pipeline.


Q 5. Utilize Jenkins Configuration as Code (JCasC) to create a template for any of the 
above pipelines.
- Create a JCasC template to define the pipeline configuration.
- Ensure the template includes all necessary configurations and credentials.
- Implement a team's notification for any one of the above builds with necessary 
details.
- Configure Jenkins to send notifications to a Microsoft Teams channel.
- Include build details such as build ID, event, status, and actor in the notification

