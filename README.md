# How to install

In the serverless.yml file, change the `TEAM_CHANNEL_NAME` and the cronjob config accordingly.

Then to deploy, you first need to get your Slack token from https://api.slack.com/apps.
Put it in the `.env` file in the `SLACK_TOKEN` variable.
Then run:

```
$ . ./.env
$ sls deploy --aws-profile {YOUR_PROFILE} --stage prod
```
