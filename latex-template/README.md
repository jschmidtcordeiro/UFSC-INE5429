# UFSC LaTeX Template

Este é um template LaTeX baseado no modelo UFSC para trabalhos acadêmicos, configurado especialmente para João Pedro Schmidt Cordeiro.

## Requisitos

Para utilizar este template, você precisa ter instalado:

1. Uma distribuição LaTeX como TeX Live, MiKTeX ou MacTeX
2. Um editor LaTeX de sua preferência (e.g., TeXStudio, Overleaf, VS Code + LaTeX Workshop)
3. Bibliotecas básicas do LaTeX, incluindo `biblatex` e pacotes relacionados
4. `make` (opcional, para usar o Makefile)

## Estrutura de Arquivos

- `main.tex`: Arquivo principal que contém a estrutura do documento
- `settings.tex`: Configurações de estilo e formatação
- `setup/`: Contém os arquivos da classe `ufscthesisx`
- `pictures/`: Diretório para armazenar imagens
- `beforetext/`: Elementos pré-textuais (capa, resumo, etc.)
- `aftertext/`: Elementos pós-textuais (referências, apêndices, etc.)
- `Makefile`: Script para automatizar a compilação e limpeza

## Como Usar

### Usando o Makefile (Recomendado)

O template inclui um Makefile para facilitar a compilação do documento:

```bash
# Compilar o documento com bibliografia completa
make

# Compilação rápida (sem bibliografia)
make quick

# Limpar arquivos temporários
make clean

# Limpar tudo (incluindo o PDF)
make cleanall

# Compilar e abrir o PDF
make view
```

### Compilação Manual

Se preferir compilar manualmente, execute a sequência:

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

## Personalização

1. **Edição do Conteúdo**: Edite o arquivo `main.tex` para:
   - Alterar título, subtítulo ou orientador
   - Mudar a data ou local de defesa
   - Configurar palavras-chave
   - Adicionar seu conteúdo na seção de conteúdo do documento

2. **Idioma**: Por padrão, o documento está em português. Para alternar para inglês, descomente a linha `\englishtrue` no início do arquivo.

3. **Bibliografia**: Adicione suas referências bibliográficas no arquivo `aftertext/references.bib` no formato BibTeX.

4. **Aparência**: O template já vem pré-configurado, mas você pode personalizar:
   - Cores e estilos no arquivo `settings.tex`
   - Cabeçalhos e rodapés
   - Pacotes adicionais no preâmbulo

## Solução de Problemas

- Se enfrentar problemas com a compilação, verifique se tem todas as dependências instaladas
- Execute `make clean` seguido de `make` para uma compilação limpa
- Para problemas com referências, certifique-se de que o Biber está instalado e funcionando

## Suporte

Este template é baseado no [ufscthesisx](https://github.com/UFSC/ufscthesisx), com adaptações para facilitar seu uso em trabalhos da UFSC.

---

Para mais informações sobre a formatação de trabalhos acadêmicos na UFSC, consulte o [Guia de Trabalhos Acadêmicos da BU/UFSC](https://portal.bu.ufsc.br/normalizacao/). 