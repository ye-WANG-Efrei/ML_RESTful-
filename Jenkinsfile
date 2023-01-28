pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker_hub')
    }


    stages {
        stage('Checkout') {
            steps{
                sshagent(credentials : ['JenkinsSSH']){
                    bat 'git branch --delete staging'
                    bat 'git branch staging'
                    bat 'git checkout staging'
                    bat 'git push origin staging'
                }
            }
        }
        
        
        stage('Building') {
            steps {
              bat 'pip3 install -r Archive/requirements.txt'
            }
        }
        stage('Testing') {
            steps {
              bat 'python classfy.py'
            }
        }
        stage('Build_docker_image'){
            steps {
              bat 'docker build -t jenkins:latest .'
            }
        }
        stage('Running'){
            steps {
              bat 'docker run -d -p 8003:8080 jenkins:latest'
            }
        }
                         
        stage('Login DockerHub') {
            steps {
                /*bat 'docker login -u wangyeee -p Wodemima0105.'*/
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                }
        }

        stage('Push image to Hub'){
            steps{
                bat 'docker tag jenkins:latest wangyeee/jenkins:latest'
                bat 'docker push wangyeee/jenkins:latest'

            }
        }
                         
        stage ('Cleanup'){
            steps{
                sshagent(credentials : ['JenkinsSSH']){
                    bat """
                    git push origin -d staging
                    echo "deleted staging"
                    """
                }
            }
        }
    
    }


  post{
      always{
         bat 'docker logout'
      }
  }
}
