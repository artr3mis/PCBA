# PCBA — Preparação para Delegado

Repositório destinado à organização dos materiais, questões, revisões e acompanhamento de estudos para o concurso de Delegado da Polícia Civil da Bahia.

## Organização sugerida
- `edital/` — edital e conteúdo programático.
- `materiais/` — resumos, legislação e jurisprudência.
- `questoes/` — questões com identificação de fonte, banca, cargo e ano.
- `discursivas/` — enunciados, respostas e correções.
- `progresso/` — tópicos estudados, revisados, testados e pendentes.

As pastas serão criadas à medida que os respectivos arquivos forem adicionados.

## Conectar ao Codex
Abra o projeto no Codex e selecione o repositório GitHub `artr3mis/PCBA` como destino. Se o trabalho estiver em uma pasta local, conecte-a ao repositório e envie os arquivos:

```bash
git remote -v
git remote add origin https://github.com/artr3mis/PCBA.git
git fetch origin
git pull origin main --rebase
git push -u origin main
```

**Atenção:** os comandos acima pressupõem que a pasta já é um repositório Git com branch `main`, sem conflitos. Se `origin` já existir, não o adicione novamente; verifique o endereço e ajuste-o quando necessário. Não envie senhas, tokens ou documentos pessoais.

Depois de enviados ao GitHub, os arquivos poderão ser consultados por ferramentas conectadas ao repositório.
