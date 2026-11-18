# Revisão antes da publicação

[English](../en-US/publishing.md) · [Início](../../README.pt-BR.md)

A primeira versão é privada. O projeto não ativa Pages, não muda a visibilidade
e não publica um site automaticamente. O uso de Pages em repositórios privados
depende do plano; repositório privado não garante site privado.

```powershell
py -3 scripts/build_site.py
py -3 -m http.server 8000 --bind 127.0.0.1 --directory site
Start-Process "http://127.0.0.1:8000/pt-BR/"
```

Após escolher e aprovar o endereço real, gere os metadados absolutos. O endereço
abaixo é apenas demonstrativo e deve ser substituído:

```bash
python3 scripts/build_site.py --base-url https://example.invalid/obsidian-web-clipper/ --indexable
python3 scripts/validate.py
```

O script prepara canonical, hreflang, Open Graph, imagem social, JSON-LD, sitemap
e robots. Ele não faz deploy. Publique somente site/ no destino aprovado.
O padrão anterior à revisão é noindex. Os links de arquivos continuam exigindo
acesso ao GitHub se o repositório permanecer privado.

Open Graph é a prévia social; o mapa animado é outra função. llms.txt e
llms-full.txt ajudam clientes compatíveis, sem prometer indexação ou ranking.
Revise licença, histórico, exemplos e dados antes de publicar. Mudar a
visibilidade ou ativar hospedagem pública exige autorização separada.

O README é Markdown renderizado; metadados Open Graph, Twitter, canonical e
JSON-LD ficam no site gerado. A imagem compacta para prévia está em
[assets/social-preview.jpg](../../assets/social-preview.jpg). Se quiser, envie-a
em GitHub Settings → Social preview. Os nomes dos tópicos do GitHub são públicos
mesmo quando o repositório é privado; aguarde a aprovação antes de adicioná-los.
A documentação do Google informa que llms.txt não altera visibilidade ou ranking
do Google Search e que não há schema especial exigido para a busca com IA.
