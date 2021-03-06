# CALCULADORA DE IMC 

## Webapp que calcula e armazena o IMC em **MongoDB**
###### OS ao qual eu fiz todas etapas: macOS Big Sur e Win10 PRO

**Requisitos**
> IDE de scripts (eu utilizo o vscode)
> docker desktop 
> kubectl (no docker desktop eu habilitei kubernetes nas configurações)

**Para criar o ambiente e disponibilizar o app**
1. instale o docker desktop https://www.docker.com/products/docker-desktop
2. Faça login na sua conta. Caso não tenha, crie-a
3. Após a instalação, habilite em configurações o kubernetes 
4. Em um local de sua escolha, faça o clone do meu git
   - git clone https://github.com/italomarcelogit/kubernetes-Calculadora-IMC.git
   - senão tiver o git, acesse e baixe-o https://git-scm.com/downloads

5. Para subir o ambiente, execute o arquivo start.sh (chmod +x para dar permissao de execucao nele) ou caso windows, start.bat. 
   - logo em seguida, execute o comando kubectl get all, com ele você poderá visualizar as subidas dos 15 pods (replicas) do seu ambiente, pod por pod
   - Este script irá fazer o deployment de 15 replicas e subirá os serviços web e mongodb
6. Aguarde poucos instantes e o serviço já estará no ar na url http://localhost:30000
