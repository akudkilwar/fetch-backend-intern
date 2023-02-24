# Background
Our users have points in their accounts. Users only see a single balance in their account. But for reporting purposes, we actually track their
points per payer. In our system, each transaction record contains: payer (string), points (integer), timestamp (date).
For earning points, it is easy to assign a payer. We know which actions earned the points. And thus, which partner should be paying for the
points.
When a user spends points, they don't know or care which payer the points come from. But, our accounting team does care how the points are
spent. There are two rules for determining what points to "spend" first:

● We want the oldest points to be spent first (oldest based on transaction timestamp, not the order they’re received)

● We want no payer's points to go negative.

# Running the Program
To run the program, go the directory containing mycode.py and run:

`python3 mycode.py <amount of points> <csv name>`

or, if that doesn't work:

`python mycode.py <amount of points> <csv name>`

### Note on extra csv files in repo
`testing.csv` and `testing.csv` are 2 files that I've created and added to test edge cases. Look at `summary.txt` for more details.
