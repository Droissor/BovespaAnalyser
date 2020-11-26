# BovespaAnalyser

_BovespaAnalyser_ é um script que consulta informações públicas disponibilizadas pela _Fundamentus_ sobre os papéis disponíveis na bolsa brasileira
e faz um ranking dos papéis baseados na fórmula mágica do _"The Little Book that Beats the Market"_ produzindo um relatório CSV no diretório local.

Para criar o ranking da fórmula mágica com base nas informações dos papéis são formulados dois rankings intermediários, um baseado no **ROIC** e outro no **EV/EBIT**.
O posicionamento do papel nos dois rankings intermediários são considerados para a pontuação final.

Para melhorar a qualidade do relatório, alguns uns filtros são aplicados:
- Liquidez maior que R$ 100.000 nos últimos dois meses
- EV/EBIT > 0
- ROIC > 10%

Esses filtros são arbitrários e podem ser alterados.

**Projeto tem caráter de aprendizado e faz uma análise quantitativa com extrema dependência da fonte dos dados.**
