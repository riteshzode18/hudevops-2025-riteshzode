### Git questions:
1.

i. Explain the use of Git LFS, and how it can be configured for a repository that frequently deals with large binary files.

ii. Initialization and Remote management:
Initialize a Git repository locally in a directory with naming convention SCM_Scripting, and complete following instruction:
o Establish a connection to your remote repo in GitHub. -> HU-DevOps-25-<Deloitte_id>
o Pull the branch assignments/scm
o create a branch name dev from it, and work on this branch.
o set up similar folder structure depicted below.
o And commit files while ensuring all .tmp files inside src folder alone are not tracked by Git.

iii. Branching and Merging
Assuming you are working on some development of two new features. You will create two feature branches from the dev branch. And, you have created a third branch test.
o In both the feature branches you work on same file (main.txt), make a commit respectively in both branches.
o Merge feature2 into feature1.
o Create three commits in test branch. Now, you want only the second commit changes to be added in your feature1.
o Finally merge the feature1 to dev and delete all the branches except assignments/scm and dev.

iv. Finally push all these changes to the repo.
o Create a Pull request to merge dev into assignments/scm, and merge it.
o Also make sure your local repo is up to date with your remote repo.




2.

i. Commit history management and snapshotting.
You have made 4 new commits in dev and realized that some of the changes need to be undone or modified.
o You need to remove the last commit from history without having the changes in that commit lost.
o Now that you have uncommitted changes in your working directory. You also realize that the second last commit contains mistakes that need to be removed by you. You need to undo the changes made in that specific commit without losing your current uncommitted changes or commit history.
o Once the changes are undo continue with your uncommited changes.
o Explain and show how you are managing the above issues.

ii. Let’s assume a scenario, where your code in the assignments/scm branch is in production, and a bug is discovered that needs an immediate fix. So, you create a hotfix branch, make the necessary changes, and push the fix to the assignments/scm branch.
o Make sure the all the changes to main goes through PR.
o Now, you already have changes in dev as part of ongoing development. And you need to ensure that the dev branch maintains a linear commit history with the main branch after the hotfix, by making sure that new commits in the main are added to your dev commit history. How are you going to handle it?
Submission Requirements:
• Provide proper screenshots of your terminal of execution of all the git commands.
• Include a screenshot of your folder structure in the file explorer, contents of the file wherever required.
• Include commit history log wherever required to showcase the completion.
• Include proper comments and explanation to all the images and details documented.



### Shell Scripting questions:

1. System Information and Password Strength Shell Script

i. Write a shell script to perform the following tasks:
o Find OS version, kernel version, uptime, memory, cores, and swap details of a Linux machine.
o Show free & available memory.
o Show cache memory.
o Increase the ulimit for the current user to 1028.
o Change the time zone to Brussels, Belgium.

ii. Create a shell script to assess password strength:
o Minimum characters should be 10.
o Should contain both alphabet and number.
o Should include both small and capital case letters.
o If the password doesn’t comply with any of the above conditions, then the script should report it as a <Weak Password>.


2. JSON Data Processing, File Structure, and Nginx Deployment Shell Script

i. Write a shell script to perform the following tasks:
o Extract all the names from a JSON file and display them.
o Filter the JSON data where the user age is above 30 and create a new JSON file with the filtered data.
o Calculate the average age of all users and display it.
Use the below json file:
```
{
"users": [
{
"name": "John Doe",
"age": 30,
"status": "inactive"
},
{
"name": "Jane Smith",
"age": 22,
"status": "inactive"
},
{
"name": "Alice Johnson",
"age": 27,
"status": "inactive"
},
{
"name": "Bob Brown",
"age": 35,
"status": "inactive"
},
{
"name": "Carol White",
"age": 29,
"status": "inactive"
},
{
"name": "David Black",
"age": 24,
"status": "inactive"
}
]
}
```

ii. Write a shell script to create the specified file structure.

iii. Write a shell script that takes a directory as input(q4) and counts the total number of different types of files and directories present in the input directory. Check if a file is executable, and if it is a .sh file, decide whether it is executable or not.
o expected Output – File 'q4/file.sh' is not executable or found File 'q4/file.sh' has been made executable sh: 1 py: 1 yml: 1 md: 2 ts: 1 tf: 1
js: 1 txt: 2 directories: 5
iv. Write a shell script named deploy_nginx.sh to:
o Check if Nginx is installed on the system.
o If Nginx is not installed, install it using the appropriate package manager.
o Copy a custom HTML file (should print your name) to the Nginx HTML directory.
o Restart the Nginx service to apply the changes.
o Attach a screenshot of the custom webpage in the browser.
```
deploy_nginx.sh

if ! command -v nginx > /dev/null 2>&1;
then
  echo "Nginx is not install"
  sudo apt update -y && sudo apt install nginx -y
  echo "Nginx install done"
else
  echo "Nginx is install"
fi

echo "<h1>Ritesh Zode</h1>" > content.html

sudo cp content.html /var/www/html/index.html

sudo systemctl restart nginx

echo "Deployment Success"
```
![image](https://github.com/user-attachments/assets/1871b197-3472-4e27-884f-ca554a9ab3bb)



3. Text Processing and Backup Shell Script and a PowerShell Backup Script
I. Write a shell script named text_processing.sh to perform specific text processing operations on a file named data.txt:
o The data.txt should contain multiple lines of data with each line containing data about a person in the format -> name, age, designation.
o The script should read the data.txt file and print the following:
 Total number of people in each designation.
 All the existing people names.
 Replace the designation "Manager" with "Team Lead" in the text file.
II. Create a shell script named backup.sh to:
o Create shell script which should copy only the text file from directory1 (text file should be there in nested folders as well) to backup directory.
o The script should create additional 2 files (error.log, backup.log) in current directory where error.log should store log of error if any and backup should store log of text files which was copied in the below format.
 <Timestamp> - Backed up - < path of the target file > Example: 2025-04-09 10:43:02 – Backed up - file1.txt to q4/dir1/dir2/file.txt
o The script should also run the script created in above question (3.I)
o Handle errors, such as no directory or no backup folder.
III. Write a PowerShell script to:
o Copy all files from the source directory to the backup directory.
o Create backup.log file and store all the logs of the copied files with the below format: <Timestamp> – Copied file: <source file name> to <path of the target file>. Example: 2025-04-09 10:43:02 – Copied file: file1.txt to C:\Users\user1\backup\file1.txt
