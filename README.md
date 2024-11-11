# Dr. RosaIA

No projeto RosaIA, nós temos uma abordagem que combina a inteligência artificial com uma plataforma que vai além de apenas fornecer
informações sobre o câncer de mama. Neste contexto, a ferramenta possibilita
que o público feminino não só encontre dados relevantes, mas também sintam
que têm um ambiente interativo, acolhedor e de fácil acessibilidade. Para isso,
foram utilizados algoritmos de inteligência artificial para desenvolver um chatbot
interativo, projetado para responder a perguntas frequentes e oferecer
informações personalizadas. 

## Instruções
1. Obter uma chave de acesso para a API no Google Gemini.
   Para isso, acesse o link: https://ai.google.dev/, informe o seu melhor e-mail e guarde a key gerada.
2. Abrir uma conta no Twilio

   O twilio é a plataforma que integra o whatsapp com a API do Gemini, portanto é fundamental para o começo do projeto.
   Acesse: https://www.twilio.com, se registre e no painel esquerdo, siga Messaging -> Try it out -> Send a Whatsapp message
   Após isso é só continuar os passos apresentados.
4. Clone esse repositório para ter o código em sua máquina, ou baixe o arquivo .zip dele

   3.1 Para fazer qualquer uma dessas opções é só ir no botão verde escrito "code", caso queira clonar utilize o comando "git clone {link .git}" e se for realizar o download .zip, não se esqueça de extrair os arquivos
5. Já no código, mude a linha 12, onde há api_key, e coloque a chave conseguida no passo 1
6. Instale as bibliotecas com o comando pip install
7. Instale também o ngrok para rodar o sistema e gerar um link. Este link será usado nas configurações no twilio, no campo de "Sandbox Settings"
8. Após ter tudo já configurado, use o comando flask --app apigemini.py run e teste mandar uma mensagem para o número do twilio
