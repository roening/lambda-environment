# lambda-environment
Este projeto foi desenvolvido para demonstrar a utilização de alguns serviços AWS, voltados para a cultura DevOps, que facilitam o teste, build e deploy de aplicações.

Os serviços AWS utilizados foram:
  - AWS CodePipeline
  - AWS CodeBuild
  - AWS CloudFormation
  - AWS S3
  - AWS IAM
  - AWS API Gateway
  - AWS Lambda

## Arquivos

### cloudformation-template.json
Este arquivo é um template do serviço AWS CloudFormation utilizado para criar o ambiente de automação. Para utilizar este template na criação de um *stack* AWS CloudFormation, os seguintes parametros serão solicitados:

#### Project Name
O nome especificado neste parâmetro será utilizado para nomear todos os recursos criados pela *stack* AWS CloudFormation.

#### S3 Bucket Name
Este bucket S3 será utilizado para armazenar o pacote AWS CloudFormation criado pelo AWS CodeBuild.

#### Repository Name
Nome do repositório onde encontra-se a aplicação. Nesse caso, será utilizado o nome deste próprio repositório: *lambda-environment*

#### Branch Name
Nome da branch onde encontra-se a versão estável da aplicação.

#### Owner Name
Nome do usuário GitHUb que tem permissão de *owner* no repositório.

#### OAuth Token
GitHub token para conceder acesso ao AWS CloudPipeline.

Ao criar um *stack* do CloudFormation utilizando este template, os seguintes recursos AWS serão criados e devidamente configurados:
  - AWS CodePipeline 
  - AWS IAM Role para o AWS CodePipeline
  - AWS S3 Bucket para o AWS CodePipeline
  - AWS CodeBuild
  - AWS IAM Role para o AWS CodeBuild Project
  - AWS S3 Bucket para o AWS CodeBuild Project
  - AWS IAM Role para o AWS CloudFormation Stack que será criado pelo AWS CodeBuild
