1.	What is the difference between git and GitLab?
Git is a distributed version control system that tracks changes in source code, while GitLab is a web-based platform that provides Git repository hosting, CI/CD pipelines, and collaboration tools.

2.	What is the difference between GitLab, GitHub, and BitBucket?

GitLab, GitHub, and BitBucket are all Git repository hosting services, but GitLab offers integrated CI/CD and DevOps features, GitHub is the most widely used for open-source projects, and BitBucket is often preferred for private repositories, especially by teams using Atlassian products.
3.	Why would I ever want to use git, but not GitLab?
You might use Git without GitLab if you are working locally without needing remote collaboration, hosting repositories on a different platform, or using Git for personal version control.

4.	What are the steps to update the GitLab server with some changes I made on my computer?

git add .
git commit -m "Description of changes"
git push origin branch-name

5.	What is a branch and why would I use one?

A branch in Git is a separate line of development that allows multiple people to work on different features or bug fixes without affecting the main codebase. It helps manage parallel development and merge changes when ready.

6.	How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?\


You can visualize it using the following ASCII representation:

A---B---C  (main branch)
     \
      D  (new branch after second commit)
7.	Give an example of a set of git commands that would result in a merge conflict.
git checkout -b feature-branch
echo "Hello, World!" > file.txt
git add file.txt
git commit -m "Added Hello World"

git checkout main
echo "Goodbye, World!" > file.txt
git add file.txt
git commit -m "Added Goodbye World"

git merge feature-branch

8.	Is Git suitable for latex documents?
Yes, Git is suitable for LaTeX documents because LaTeX files are plain text, making them easy to track, merge, and collaborate on.

9.	Should I from now on version my word and powerpoint slides using git? Why/why not?
Versioning Word and PowerPoint files in Git is not ideal because they are binary files, making it difficult to track changes. However, if version control is necessary, using tools like Git LFS (Large File Storage) can help manage them.


10.	What could happen when I push my latest commit to the remote repository without pulling first?
If others have pushed changes since your last pull, Git will reject your push and require you to pull and merge their changes before pushing again.


11.	What happens when I pull without commiting my local changes first?

Git will attempt to merge the remote changes into your local branch, but if there are conflicting changes, it will pause the pull and require you to resolve the conflicts before proceeding.
12.	What is the difference between branching and forking?
Branching creates a new development line within the same repository, while forking creates a separate copy of the repository, usually to contribute to an open-source project without affecting the original.
