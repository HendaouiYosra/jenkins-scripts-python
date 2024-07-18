import jenkins

from jenkins import JenkinsException

def trigger_jenkins_job_build(server_url, access_token, job_name):
  try:
    # Connect to Jenkins server using access token
    server = jenkins.Jenkins(server_url, api_token=access_token)

    # Check if the job exists
    if server.job_exists(job_name):
      # Trigger a build for the job
      server.build_job(job_name)
      print(f"Build triggered for job '{job_name}'.")
    else:
      print(f"Error: Job '{job_name}' does not exist.")

  except JenkinsException as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  # Jenkins server details
  jenkins_server_url = "https://jenkins.artibedded.com/"
  jenkins_access_token = "11b42187f5222050e03da11baea3bf4e44"

  # Job details
  job_name = "build"

  # Trigger Jenkins job build
  trigger_jenkins_job_build(jenkins_server_url, jenkins_access_token, job_name)
