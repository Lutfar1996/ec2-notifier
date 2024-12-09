pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-1"
        INSTANCE_ID = "i-0dec7ae1549dba4a1"
        DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1315554436285726740/B0Wb36cKUF8o236R6xljUF_3cSG7VTcKbYAOWocEkQcHgB8zFx6Zvxbq_1zY4P8HZTwI"
        GITHUB_REPO = "https://github.com/Lutfar1996/ec2-iac.git"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${GITHUB_REPO}"
            }
        }
        stage('Stop EC2 Instance (Thursday)') {
            when {
                expression { new Date().format('E', TimeZone.getTimeZone('UTC')) == 'Thu' }
            }
            steps {
                sh 'python3 manage_ec2.py stop'
            }
        }
        stage('Start EC2 Instance (Saturday)') {
            when {
                expression { new Date().format('E', TimeZone.getTimeZone('UTC')) == 'Sat' }
            }
            steps {
                sh 'python3 ec2_notifier.py start'
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed."
        }
    }
}
