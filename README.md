# Automatically Update Toffee App All Channel Link with Headers

**Watch the video tutorial:**

[![Alt text](https://www.google.com/url?sa=i&url=https%3A%2F%2Fapkpure.com%2Ftoffee-for-android-tv%2Fcom.banglalink.toffeetv&psig=AOvVaw1qeLPxCqK07by84sHB0P1B&ust=1697987539194000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLjcpdO2h4IDFQAAAAAdAAAAABAE)](https://youtu.be/PaGp7Vi5gfM)

This example shows how to run a Python script as cron job with GitHub Actions. It calls an API once a week (could be any schedule you want), logs the response in `status.log`, and automatically pushes the changes to this repo.

- Implement your script in `main.py`
- Inspect and configure cron job in GitHub Action `.github/workflows/actions.yml`
- It can install and use third party packages from `requirements.txt`
- Secret environment variables can be used. Set secrets in Settings/Secrets/Actions -> 'New repository secret'. Use the same secret name inside `actions.yml` and `main.py`
