pipeline {
  environment {
    registry = "YourDockerHubID/YourRepoName"
    registryCredential = 'dockerhub'
  }  
  agent any
  stages {
    stage('Checkout'){
      steps {
        checkout scm
      }
    }
    stage('Building image') {
      steps{
        script {
          imageName = registry + ":$BUILD_NUMBER"
          context = "'.'"
          dockerImage = docker.build(imageName, context)
        }
      }
    }
    stage ("Publish"){
      steps {
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
            dockerImage.push("latest")
          }
        }
      }
    }
    stage('Cleanup') {
      steps{
        sh "docker rmi $registry:$BUILD_NUMBER"
      }
    }
  }
}
