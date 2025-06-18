Problema 10

Documentos e Relatórios Empresariais
implemente um sistema de gerenciamento de documentos empresariais com diferentes formatos de relatório.
- Interface DocumentContract com método getContent(): string.
- Classe Abstrata Document (privado), com titulo e data.
- Classe Report (inclui seção de análise) e Invoice (inclui valor total), herdando de Document.
- Classe genérica DocumentManager<T extends DocumentContract> para adicionar documentos, buscar por tipo e exibir conteúdos.
- No uso, cadastre documentos, filtre por tipo e exiba os conteúdos.

Samuel da Penha Nascimento
Gabriel Lima Silva Oliveira

Entre na raiz do projeto "prova-poo2" e rode npm run dev