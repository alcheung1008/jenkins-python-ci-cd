pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Show Project Files') {
            steps {
                powershell '''
                    Get-ChildItem -Recurse
                '''
            }
        }

        stage('Run Python Program') {
            steps {
                powershell '''
                    python3 sample_code.py
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                powershell '''
                    python3 -m pytest -v tests
                '''
            }
        }

        stage('Check Code Style') {
            steps {
                powershell '''
                    pycodestyle sample_code.py --max-line-length=100
                '''
            }
        }
    }

    post {
        always {
            script {
                env.BUILD_RESULT = currentBuild.currentResult

                withCredentials([
                    string(
                        credentialsId: 'webex-bot-token',
                        variable: 'WEBEX_TOKEN'
                    ),
                    string(
                        credentialsId: 'webex-room-id',
                        variable: 'WEBEX_ROOM_ID'
                    )
                ]) {
                    sh '''
                        python3 - <<'PY'
import json
import os
import urllib.request

status = os.environ.get("BUILD_RESULT", "UNKNOWN")
job_name = os.environ.get("JOB_NAME", "Unknown Job")
build_number = os.environ.get("BUILD_NUMBER", "Unknown")
build_url = os.environ.get("BUILD_URL", "")

message = (
    f"Jenkins build notification\\n\\n"
    f"Job: {job_name}\\n"
    f"Build: #{build_number}\\n"
    f"Status: {status}\\n"
    f"Details: {build_url}"
)

payload = json.dumps({
    "roomId": os.environ["WEBEX_ROOM_ID"],
    "markdown": message
}).encode("utf-8")

request = urllib.request.Request(
    "https://webexapis.com/v1/messages",
    data=payload,
    headers={
        "Authorization": "Bearer " + os.environ["WEBEX_TOKEN"],
        "Content-Type": "application/json"
    },
    method="POST"
)

with urllib.request.urlopen(request) as response:
    print("Webex notification sent. HTTP status:", response.status)
PY
                    '''
                }
            }
        }
    }
}