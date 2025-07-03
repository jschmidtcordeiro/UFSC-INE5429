# Trabalho Individual sobre o PGP

Importante: Respostas às questões abaixo um único arquivo PDF e entregue este arquivo (SEM COMPRIMIR), ou seja, entregue o arquivo PDF.

### Questões

### 1) Criar certificado PGP.

Obs.: SALVAR A CHAVE PRIVADA E NÃO ESQUECER SENHA.

- Faça um backup da sua chave privada;
- Publicar a chave pública em um repositório PGP. Exemplos:
    - MIT PGP Public Key Server
    - Keyserver Ubuntu: https://keyserver.ubuntu.com/

Referências: gpg --help e https://help.ubuntu.com/community/GnuPrivacyGuardHowto

**Resultado Esperado:** Certificado do Aluno publicado no repositório PGP.

### 2) Pratique a revogação de certificados

Crie um novo certificado PGP para este trabalho individual

Obs.: Não use o seu certificado do passo anterior pois este novo será revogado.

- Coloque esse certificado no servidor PGP. Depois verifique seu status.
- Então, crie um certificado de revogação e revogue o certificado novo.

É importante lembrar que a base de dados local ( anéis de chaves privadas e públicas ) precisam ser atualizadas com o conteúdo dos servidores PGP. Utilize a opção "refresh" periodicamente para fazer isso.

## Resultado Esperado:
- Faça um relatório do que você fez, incluindo o KeyID do certificado revogado.

### 3) Pratique a revogação de assinaturas.

Assine um certificado qualquer PGP ( de outra pessoa ). E envie esse certificado para o servidor PGP. Depois verifique o status do certificado. E então, revogue a assinatura que você fez. Confira o resultado no servidor PGP.

## Resultado Esperado:
- Faça um relatório do que você fez, incluindo o KeyID do certificado cuja assinatura você revogou.

### 

### Responda as seguintes perguntas:

**4) O que é o anel de chaves privadas?** Como este está estruturado? Na sua aplicação PGP onde este anel de chaves é armazenado? Quem pode ser acesso a esse porta chaves?

**5) Qual a diferença entre assinar uma chave local e assinar no servidor?**

**6) O que é e como é organizado o banco de dados de confiabilidade?**

**7) O que são e para que servem as sub-chaves?**

**8) Coloque sua foto (ou uma figura qualquer) que represente você em seu certificado PGP.**

**9) O que é preciso para criar e manter um servidor de chaves PGP sincronizado com os demais servidores existentes?**

**10) Dê um exemplo de como tornar sigiloso um arquivo usando o PGP.**

Trabalhe em dupla: envie esse arquivo sigiloso para um colega e peça para que o colega faça o mesmo para você com outro arquivo. Você deve decifrar e recuperar o conteúdo original.

**11) Mostre um exemplo de como assinar um arquivo** (assinatura anexada e outro com assinatura separada ), usando o PGP. Envie uma mensagem assinada para um colega. Esse colega deve enviar para você outra mensagem assinada. Verifique se a assinatura está correta.

**Atenção**: referencie todo o material utilizado para responder cada pergunta e desenvolver o trabalho. Espera-se ao menos 1 citação por questão.

Trabalhos sem referências/citação não serão corrigidos.