pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-1"
        INSTANCE_ID = "i-0dec7ae1549dba4a1"
        DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1315554436285726740/B0Wb36cKUF8o236R6xljUF_3cSG7VTcKbYAOWocEkQcHgB8zFx6Zvxbq_1zY4P8HZTwI"
        AWS_CREDENTIALS_ID = 'aws-credentials' // AWS credentials ID
        GITHUB_REPO = "https://github.com/Lutfar1996/ec2-notifier.git"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${GITHUB_REPO}"
            }
        }

        stage('Wait for 13:28 (Start EC2 Instance)') {
            steps {
                script {
                    def timeZone = TimeZone.getTimeZone('Asia/Dhaka')
                    def currentTime = new Date()
                    currentTime.setTimeZone(timeZone)

                    def targetTime = currentTime.clone()
                    targetTime.setTimeZone(timeZone)
                    targetTime.setHours(13, 28, 0, 0)

                    def timeDifference = targetTime.time - currentTime.time
                    def sleepTimeInSeconds = timeDifference / 1000

                    if (sleepTimeInSeconds > 0) {
                        echo "Waiting for 13:28 to start EC2 instance..."
                        sleep time: sleepTimeInSeconds, unit: 'SECONDS'
                    } else {
                        echo "It's already past 13:28, proceeding to start EC2 instance."
                    }
                }
            }
        }

        stage('Start EC2 Instance') {
            steps {
                script {
                    withCredentials([[ 
                        $class: 'AmazonWebServicesCredentialsBinding',
                        credentialsId: AWS_CREDENTIALS_ID 
                    ]]) {
                        try {
                            echo "Starting EC2 instance..."
                            sh "python3 script.py start"
                        } catch (Exception e) {
                            echo "Failed to start EC2 instance: ${e.getMessage()}"
                            error "Exiting due to failure"
                        }
                    }
                }
            }
        }

        stage('Wait for 13:30 (Stop EC2 Instance)') {
            steps {
                script {
                    def timeZone = TimeZone.getTimeZone('Asia/Dhaka')
                    def currentTime = new Date()
                    currentTime.setTimeZone(timeZone)

                    def targetTime = currentTime.clone()
                    targetTime.setTimeZone(timeZone)
                    targetTime.setHours(13, 30, 0, 0)

                    def timeDifference = targetTime.time - currentTime.time
                    def sleepTimeInSeconds = timeDifference / 1000

                    if (sleepTimeInSeconds > 0) {
                        echo "Waiting for 13:30 to stop EC2 instance..."
                        sleep time: sleepTimeInSeconds, unit: 'SECONDS'
                    } else {
                        echo "It's already past 13:30, proceeding to stop EC2 instance."
                    }
                }
            }
        }

        stage('Stop EC2 Instance') {
            steps {
                script {
                    withCredentials([[ 
                        $class: 'AmazonWebServicesCredentialsBinding', 
                        credentialsId: AWS_CREDENTIALS_ID 
                    ]]) {
                        try {
                            echo "Stopping EC2 instance..."
                            sh "python3 script.py stop"
                        } catch (Exception e) {
                            echo "Failed to stop EC2 instance: ${e.getMessage()}"
                            error "Exiting due to failure"
                        }
                    }
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
