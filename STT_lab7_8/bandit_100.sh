#

COMMITS=$(git log --no-merges -n 100 --pretty=format:"%H")

mkdir -p bandit_results

for COMMIT in $COMMITS; do
    git checkout $COMMIT
    bandit -r . -f json -o bandit_results/$COMMIT.json
done

#!/bin/bash

# Get the last 100 non-merge commit hashes
# COMMITS=$(git log --no-merges -n 100 --pretty=format:"%H")

# # Create directory for bandit results
# mkdir -p bandit_results

# # Loop through each commit hash
# for COMMIT in $COMMITS; do
#     echo "Checking out commit: $COMMIT"
#     git checkout $COMMIT >/dev/null 2>&1  # Suppress unnecessary git output

#     # Run bandit and store results in JSON format
#     bandit -r . -f json -o bandit_results/$COMMIT.json

#     echo "Scan completed for $COMMIT"
# done

# # Switch back to the main branch after running
# git checkout main
