pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-1"
        INSTANCE_ID = "i-0dec7ae1549dba4a1"  // Replace with your EC2 instance ID
        DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1315554436285726740/B0Wb36cKUF8o236R6xljUF_3cSG7VTcKbYAOWocEkQcHgB8zFx6Zvxbq_1zY4P8HZTwI"  // Replace with your Discord webhook URL
       AWS_CREDENTIALS_ID = 'aws-credentials' // Replace with your AWS credentials ID
    }

    triggers {
        cron('59 7 * * *')  // Trigger at 07:40 UTC (13:40 BGT) for EC2 Start
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    echo "Installing Python dependencies..."
                    sh 'pip install boto3 requests'
                }
            }
        }

        stage('Start EC2 Instance') {
            steps {
                script {
                    echo "Starting EC2 Instance: ${INSTANCE_ID}..."
                    sh 'python3 manage_ec2.py start'  // Replace with your EC2 start command
                    sendDiscordNotification("🚀 EC2 instance ${INSTANCE_ID} has started.")
                }
            }
        }

        stage('Stop EC2 Instance') {
            steps {
                script {
                    echo "Stopping EC2 Instance: ${INSTANCE_ID}..."
                    sh 'python3 manage_ec2.py stop'  // Replace with your EC2 stop command
                    sendDiscordNotification("🛑 EC2 instance ${INSTANCE_ID} has stopped.")
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed."
        }
    }
}

def sendDiscordNotification(message) {
    echo "Sending Discord notification..."
    def response = sh(script: """
        curl -X POST -H "Content-Type: application/json" -d '{"content": "${message}"}' ${DISCORD_WEBHOOK_URL}
    """, returnStatus: true)
    
    if (response != 0) {
        echo "Failed to send Discord notification."
    } else {
        echo "Discord notification sent successfully."
    }
}


// ---------------------



// pipeline {
//     agent any

//     environment {
//         // AWS Credentials ID from Jenkins credentials store
//         AWS_CREDENTIALS_ID = 'aws-credentials' // Replace with your AWS credentials ID
//     }

//     stages {
//         stage('Checkout') {
//             steps {
//                 git branch: 'main', url: 'https://github.com/Lutfar1996/ec2-iac.git'
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 script {
//                     // Install necessary dependencies, create virtual environment
//                     sh '''#!/bin/bash
//                         sudo apt update && sudo apt install -y python3.12-venv
//                         python3 -m venv venv
//                         source venv/bin/activate
//                         pip install -r requirements.txt
//                     '''
//                 }
//             }
//         }

//         stage('Run Python Script') {
//             steps {
//                 script {
//                     // Use withCredentials to inject AWS IAM credentials
//                     withCredentials([[
//                         $class: 'AmazonWebServicesCredentialsBinding', 
//                         credentialsId: AWS_CREDENTIALS_ID // AWS credentials ID
//                     ]]) {
//                         // Run your python script with AWS credentials available
//                         sh '''#!/bin/bash
//                             source venv/bin/activate
//                             python3 script.py
//                         '''
//                     }
//                 }
//             }
//         }
//     }
// }
