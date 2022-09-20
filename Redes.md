# Descrição dos tópicos da Matéria

1. Redes de Comunicação
2. Camadas Superiores
   1. Aplicação
      1. Arquiteturas de Aplicativos
         1. Cliente Servidor
         2. Peer-to-peer (P2P)
      2. Sockets (API)
      3. Endereçamento de Aplicativos: IP + Porta
      4. Exemplo Aplicação: web + HTTP
      5. HTTP
         1. Sobre TCP ou QUIC
         2. Não persistente (closed)
            1. Tempo De resposta: = 2RTT + Tempo transmissão Arquivo
         3. Persistente (keep alived)
         4. HTTPS
      6. RTT (Round-Trip Time)
         1. Tempo de ida e volta de pacote pequeno.
   2. Transporte
      1. Camada: envia segmentos processo-processo usando TCP, UDP ou QUIC
      2. Transporte Parte 1
         1. RTD: Reliable Data Transfer
         2. TCP
         3. rtd 1.0 canal confiavel
         4. rdt 2.0 erro em bits
            1. bit paridade
            2. acks
            3. nacks
         5. rdt 2.1 ACKS e NACKS com paridade
         6. rdt 2.2 somente ACKS
            1. identificadores de estado #seq \in [0,1]
      3. Transporte Parte 2
         1. rdt 3.0 erros E perdas de pacote
            1. time out pra reenvio de pacote perdido
            2. protocolo de bit alternante
            3. Protocolo funcional, mas com baixo desempenho
         2. Medidas de Desempenho de Protocolos de Transporte
            1. Atraso de Transmissão:
               1. d_{trans} = L/R  onde (L=nº bits), (R=bits/s do enlace)
            2. Taxa de utilização do enlace
               1. U_{trans} = (L/R) / ( RTT + (L/R) )
         3. Protocolos com paralelismo (Pipelining)
            1. Se transmitir N pacotes por vez
               1. U_{trans} = N*(L/R) / ( RTT + (L/R) )
            2. Go-back-N
               1. único timer
               2. mais simples
               3. reenvia tudo desde o último perdido
               4. ack cumulativo
            3. Repetição Seletiva (RS)
               1. vários timers (um pra cada pacote)
               2. .#seq = 2N necescessários (maior)
               3. reenvia somente pacotes perdidos
               4. precisa de buffer guaradar pacotes e manter ordem
      4. Transporte Parte 3: TCP
         1. Resumo de Reliable Data Transfer
         2. Código detecção erro
            1. Recuperar pacote corrompido
         3. Acknowledgment (ACK)
            1. Avisar que pacote chegou corretamente
         4. NAKC
            1. Avisar que pacote não chegou/ chegou incorreto
         5. Números Sequências
            1. Lidar com duplicatas de pacotes
         6. Timer
            1. Detectar perdas de pacotes
         7. Janelas e paralelismo (Pipelining)
            1. Enviar múltiplos pacotes antes de ACK → Otimiza taxa de utilização do Enlace
         8. UDP: User Datagram Protocol
            1. Entrega não confiavel de pacotes
            2. Datagram implementado pelo usuário
         9. TCP: Transmission Control Protocol
            1. mistura de go-back-N e SR
            2. entrega confiável de pacotes
            3. controle de congestionamento, fluxo
            4. setup de conexão
            5. TCP e UDP não garantem latência e nem capacidade
            6. Características TCP:
               1. .#seq
               2. ACK cumulativo (GBN)
               3. único temporizador (GBN)
               4. Retransmite apenas segmento perdiro (SR)
         10. RTT e Time-out:
             1. Muito curto → time out prematuro → reenvio de pacotes
             2. Muito longo → perde segmento
             3. Estimativa de RTT → sampleRTT
                1. Filtrado com média móvel: Filtro IIR
             4. Formulas Média móvel com ponderação exponêncial
                1. EstimatedRTT(t) =  (1-_α_)*EstimatedRTT(t-1) + _α_*SampleRTT(t)
                2. _α_ = 1/8 normalmente
                3. DevRTT = (1-_β_)_DevRTT(t-1) + β_|SampleRTT(t) - EstimatedRTT(t)|
                4. _β_ = 1/4 normalmente
                5. TimeoutInterval(t) = EstimatedRTT(t) + 4*DevRTT
   3. Rede

‌
