# Raccoon-PS

Olá,

Aqui estarão explicadas cada pergunta e como pensei em realizar cada questão, logo:


1) Qual a média de gastos de pessoas com ingresso Pista?

  Nessa questão, minha idéia foi: juntarei a planilha 1 com a 2, e usarei condicionais, para verificar aqueles que efetivamente foram ao show e estavam na pista, e assim terei também como base gastos na mesma planilha, assim podendo aplicar .mean(), encontrando a média.


<div align="center">
<img src="https://user-images.githubusercontent.com/87606621/172808919-2c788e20-2596-4c37-9b99-0860b789c23e.PNG" width="600px" /><br>
<img src="https://user-images.githubusercontent.com/87606621/172808608-0c740c8d-8d81-4d73-84b5-40b6960268c5.PNG" width="300px" />
</div>

2)Quais pessoas não compareceram aos shows?

  Não houveram pessoas que não compareceram, uma vez que embora não tivessem feito compra efetiva de ingressos com a AT, há gastos, mesmo que mínimos, exaltados pela tabela psel-de-compras.
  
3) Quais pessoas compraram ingressos com concorrentes?
    
    <div align="center">
<img src="https://user-images.githubusercontent.com/87606621/172722207-553754d5-26a3-4371-a482-7b5dd962501b.PNG" width="600px" />
</div>
    
 4) Qual o dia com maior gasto?

    Pelo resultado apontado pelo programa, o dia com maior movimentação financeira foi o dia 1, visto pelo código e pelo gráfico
    
     <div align="center">
<img src="https://user-images.githubusercontent.com/87606621/172722500-8444e0d1-30af-4e2a-b914-a8319016afc2.PNG" width="600px" /><br>
<img src="https://user-images.githubusercontent.com/87606621/172722490-5579b256-6418-473f-870e-fdeb27713353.PNG" width="600px" />
</div>


    

 5) Faça uma lista com os clientes que desistiram de comprar o ingresso com a AT, a soma do valor que foi gasto durante os shows e quais shows eles desistiram de
comprar. Usar para resposta o esquema abaixo:

  foram separados os clientes com status diferentes de concluido, para assim serem inseridos em listas, utilizando de list comprehension, após isso, foi-se utilizado a biblioteca json para criar o arquivo
