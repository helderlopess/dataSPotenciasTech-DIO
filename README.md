# DIO | Resumo dos comandos markdown e git gitHub

Arquivo MD para exemplificar as propriedades da marcação

## 🖥 estrategias win + . para emojis

- traço para bullets
- [assim vira link](linkaqui.com)
  
## Tabelas

| tabelas | Descrição |
|------------|---------|
|Titulo da tabela|Aqui vai a tabela feita|

python: [documentação](python)

``` python

print('Aqui vai o codigo em linha digitavel')
```

## Comandos

- [Git e Github](link.com)

## criando novos arquivos locais

criando arquivo local com bash

```bash
echo "#comit-1-branch-main.txt"
```

## removendo basta git

Basta deletar a pasta .git ou usar no bash o codigo

```bash
rm -rf .git
```

estando dentro do diretorio que voce quer remover a pasta git

## restaurar arquivos de trabalho comitados

no bash

```bash
git restore

```

ele ira restaurar ate o commite selecionado todas as alterações feitas até aquele tempo

## alterando mensagem do ultimo commit

no bash

```bash
git commit --amend -m"aqui sera a nova mensagem"
```

ele altera a mensagem do ultimo commit

se ao inves de digitar -m voce der enter ele abrira o editor para que o arquivo possa ser alterado

-pra sair voce vai dar ESC:
-W para escrever
-Q para sair

## desfazendo commit

--soft -volta o commit nos arquivos ja presentes no local
--mix -volta o comit mas adiciona os arquivos como untracked
--hard -volta comit ignorando arquivos anteriores retomando ao comit desconsiderando tudo que tinha antes

```bash
git reset --soft hashDoCommit
```

importante fazer estes commits em ambiente local antes de enviar para produção

É possivel ainda passar o git reset nomeDoArquivo é o mesmo será removido do comit selecionado

pode-se tambem usar o comando

```bash
git restore --staged caminho/nomeDoArquivo
```

## Manipulando banches

utlize o comando ```bash checkout -b nomedabranch``` para mudar da branch main para a nova

```bash
echo "#comit-1-branch-main" > comit-1-branch-main
```

utilizando o ```bash git branch -v``` podemos ver os commits no main e nas branchs criadas

## Mesclando na main

para mesclar as alterações feitas na branch com a main utilizaremos

```bash git merge nomeDaBranch```
feito isto ele ira fundir a branch seleciona com  a main incorporando as alterações realizadas

para deletar um branch criada usaremos o camando ```bash git branch -d nomeDaBranch```

## conflitos de Merge

quando os comits em uma branch são iguais no mesmo arquivo e linha de codigo, ao fundilas o git pedira que voce confirme as alterações que devem ser mantidas.
sera criado dentro do arquivo as 2 alterações e voce deve manter as que quer que permaneçam. apos salvar basta realizar add e commitar novamente

## comando uteis com branchs

git fetch - baixa as alterações mas não mescla ate que voce faço o merge
git merge -mescla as alterações entre branch e main
git diff - mostra as diferenças entre as branchs e o main

-copiar clonar apenas a branch no remoto

git clone endereço --branch nome --single-branch

-arquivando alterações
git stash nomeDaBranch

ai sera necessario fazer uma nova branch caso queima rever os arquivos modificados
git checkout -b nomeDaBranch
