# Security and privacy / Segurança e privacidade

## English

Only demo vault names, example.invalid URLs, and generic paths belong in tracked
examples. Keep customized templates in ignored local-only/. Never commit original
extension settings exports; they may contain API keys. A private repository is
access control, not a safe place to store secrets. If a key was committed, revoke
it before coordinating history cleanup; deleting the latest file alone is insufficient.

The baseline scanner checks common credential formats, credential assignments,
personal home paths, and prohibited export filenames. It cannot guarantee absence
of all personal information. Inspect diffs and release contents before sharing.

AI requests go to the provider configured locally in Web Clipper. Review which
page content and metadata may be sent. These templates do not crawl the vault,
execute source scripts, fetch arbitrary linked pages, or install synchronization.

Report a suspected issue privately to the maintainer through GitHub's private
security reporting if enabled; otherwise use an already established private
channel. Do not include live secrets in public issues. No automatic public
deployment is included. Hosting a private repo's site may still expose its pages.

## Português

Use somente dados de demonstração nos arquivos versionados. Guarde configurações
personalizadas em local-only/. Nunca envie exportações reais: podem conter chaves.
Se uma credencial entrar no histórico, revogue-a antes de tratar a remoção.
O scanner é uma ajuda, não uma garantia de privacidade. Revise diffs e ZIPs.
O Interpreter envia dados ao provedor configurado localmente. A hospedagem de um
site pode expor conteúdo mesmo quando o repositório é privado; revisão é obrigatória.
