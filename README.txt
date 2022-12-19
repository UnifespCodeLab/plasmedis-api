## Para executar com Docker

- Construa a imagem com `docker build -t plasmedis-api .` no diretório com o arquivo `Dockerfile`

- Rode `docker run -d -t plasmedis-api` para executar em modo desacoplado (-d)

- Use `docker network inspect bridge` para identificar o IṔ do container e utilize-o para fazer as requisições sobre a porta 8000

## Para executar com docker-compose
- Build: ```docker-compose build```

- Executar: ```docker-compose up flask-api```

- Verificar: ```http://172.18.0.2:8000/```


## Para montar a imagem e subir no GCP

- docker build -t eu.gcr.io/emtu-371421/plasmedis-api:0.1 .

- docker push eu.gcr.io/emtu-371421/plasmedis-api:0.1