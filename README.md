
# PC-XCON 
 O PC-XCON é um sistema especialista que utiliza Redes Bayesianas para recomendar a melhor configuração de hardware para um computador baseando-se no perfil de uso do usuário. 



## Demonstração

O PC-XCON está disponível como API, projeto Netica e Google Colab.

## Projeto Netica
O PC-XCON pode ser utilizado no Netica, o arquivo .dne encontra-se na pasta [/projeto-netica](./projeto-netica/)

## Google Colab

Também é possivel utilizar o PC-XCON com o Google Colab.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FranciscoPaixao/PCXCON/blob/main/PC_XCON.ipynb)

## Documentação da API
##### A Documentação com o Swagger encontra-se na api: [https://api.pcxcon.lab.dev.br](https://api.pcxcon.lab.dev.br)
#### Classifica o uso principal do PC com base nas peças e periféricos informados

```http
  GET /api/classificar
```

| Parâmetro           | Tipo     | Descrição                                 |
| :------------------ | :------- | :---------------------------------------- |
| `cpu`               | `string` | Aceita: Ryzen3, Ryzen5, Ryzen7, RyzenThreadripper |
| `gpu`               | `string` | Aceita: GPUIntegrada, RTX3050, RTX3060, RTX3070, RTX3080, RTX3090 |
| `ram`               | `string` | Aceita: RAM8GB, RAM16GB, RAM32GB, RAM64GB, RAM128GB |
| `armazenamento`     | `string` | Aceita: SSD512GB, SSD1TB, HDD1TB, HDD4TB |
| `teclado`           | `string` | Aceita: Mecanico, Membrana |
| `mouse`             | `string` | Aceita: MousePadaria, Top5DeluxM800PRO, Top4MotospeedDarmosharkM3, Top3AjazzAj139, Top2KysonaM600, Top1DragonFlyVgnF1 |
| `monitor`           | `string` | Aceita: QHD240HzIPS, FHD60hzTN, UHD60hzIPSFoscaC1000P1, UHD60hzIPSBrilhosaC1000P1 |
| `perifericoadicional` | `string` | Aceita: MesaDigitalizadora, SemPeriferico |



#### Recomenda as peças e periféricos para o PC  

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `usoprincipal`      | `string` | **Obrigatório**.  |

*Mais detalhes na documentação Swagger.
## Referências

 - [Redes Bayesianas com o Netica na Prática](https://www.youtube.com/watch?v=NY332nE67_E)
 - [Aula 11 - Exemplo - Previsão de Chuva -  Código em Python no Colab ](https://colab.research.google.com/drive/1e2TH552HGu1F2xl0p2y11-lBqKbWtRVa?usp=sharing) 
 - [Aula 11 - Exemplo - Previsão de Doença Cardíaca -  Código em Python no Colab](https://colab.research.google.com/drive/14dvdnCBgHQTbtknqur5tTisTeQDmES7p?usp=sharing)
# Fonte de dados sobre Mouses e Monitores
 - [Top 5 Melhores Mouses Custo Benefício que eu já usei](https://www.youtube.com/watch?v=DyvHkkT0aFs&t=701s)
 - [ESCOLHENDO O MONITOR IDEAL PARA DESIGN GRÁFICO 2023: DICAS E RECOMENDAÇÕES](https://www.youtube.com/watch?v=X_I07Lv4a7c)

