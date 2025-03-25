import sys
import os
import subprocess
from git import Repo, GitCommandError

def runBanditOnCommits(repoPath, branchName, numCommits):
    try:
        # Initialize repository object
        repo = Repo(repoPath)

        # Checkout to specified branch
        repo.git.checkout(branchName)

        # Get commits
        commits = list(repo.iter_commits(branchName, max_count=numCommits))

        # Filter out merge commits (keep only commits with 0 or 1 parent)
        nonMergeCommits = [commit for commit in commits if len(commit.parents) <= 1]

        # Adjust if fewer non-merge commits are found
        if len(nonMergeCommits) < numCommits:
            print(f"Found only {len(nonMergeCommits)} non-merge commits.")
        nonMergeCommits = nonMergeCommits[:min(len(nonMergeCommits), numCommits)]

        # Define report directory (relative path based on repo name)
        repoName = os.path.basename(os.path.normpath(repoPath))
        reportDirectory = f"./reports/{repoName}"
        os.makedirs(reportDirectory, exist_ok=True)

        # Process each commit
        for i, commit in enumerate(nonMergeCommits, start=1):
            try:
                # Checkout specific commit
                repo.git.checkout(commit.hexsha)

                # Define report file path
                reportFile = os.path.join(reportDirectory, f"{i}.txt")

                # Open report file and run bandit
                with open(reportFile, 'w') as fileHandle:
                    subprocess.run(['bandit', '-r', repoPath], stdout=fileHandle, stderr=subprocess.STDOUT)

                print(f"Commit: {commit.hexsha} - Report saved to {reportFile}")
            except Exception as e:
                print(f"Error running Bandit on commit {commit.hexsha}: {str(e)}")

        # Switch back to original branch
        repo.git.checkout(branchName)
        print(f"Checked out back to branch: {branchName}")

    except GitCommandError as e:
        print(f"Git error: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    # Validate arguments
    if len(sys.argv) != 4:
        print("Usage: script.py <repo_name> <branch_name> <num_commits>")
        sys.exit(1)

    repoName = sys.argv[1]
    branchName = sys.argv[2]
    try:
        numCommits = int(sys.argv[3])
    except ValueError:
        print("Error: num_commits should be an integer.")
        sys.exit(1)

    # Repo path relative to current directory
    repoPath = f"./{repoName}"

    runBanditOnCommits(repoPath, branchName, numCommits)

if __name__ == "__main__":
    main()
