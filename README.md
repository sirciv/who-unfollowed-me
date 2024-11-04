# who-unfollowed-me
An Instagram utility that reports on one-way follows.

Currently, Instagram makes it difficult to find out who has unfollowed you or hasn't followed you back. This python script converts Meta-provided data into a plain text list and then compares your follows and following lists to find discrepancies.

_Instructions as of November 2024..._

1. To request a list of your connections from Meta, go to https://accountscenter.instagram.com/info_and_permissions/
2. Click on "**Download your information**" and then "**download or transfer information**."
3. Click "**Some of your information**." Check the box that says "**Followers and following**," then "**download to device**," and set the date range to max. Under "**format**," choose **JSON**.
4. After a bit of time, you'll be allowed to download your requested information. Take the "**following.json**" and "**followers_1.json**" files and put them in the same folder as **who-unfollowed-me.py**.
5. Run the script. It will export four text files:
  - Your followers
  - Your following
  - People who are only following you
  - People who only you are following

Altogether, it takes less than a minute to convert the data. There are probably ways to make it more efficient or adaptable, but I'm pretty happy with its present level of automation and consider the project complete.
