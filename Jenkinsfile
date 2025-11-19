// Jenkinsfile
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Código-fonte clonado do Git.'
            }
        }
        
        stage('Build Simples (Verificação)') {
            steps {
                sh 'echo "Iniciando Build do Catálogo de Produtos da Vinheria Agnello..."'
            }
        }
        
        stage('Deploy em Pasta de Publicação') {
            steps {
                sh 'mkdir -p /opt/vinheria/catalogo-producao'
                sh 'cp -r catalogo-service/* /opt/vinheria/catalogo-producao/'
                sh 'echo "Deploy do Catálogo realizado em /opt/vinheria/catalogo-producao"'
            }
        }
        
        stage('Verificação de Deploy') {
            steps {
                sh 'echo "Deploy concluído com sucesso!"'
            }
        }
    }
}
