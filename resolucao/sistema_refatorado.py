
# CLASSES ABSTRATAS E INTERFACES
class Pagamento:
  def pagar(self, valor):
      pass
    
class Notificacao:
  def enviar(self):
      pass

# IMPLEMENTAÇÕES CONCRETAS
class ProcessadorDePedidos:
  def processar(self, pedido):
      print(f"Processando o pedido #{pedido['id']} no valor de R$ {pedido['valor']:.2f}...")

class PagamentoCartaoCredito(Pagamento):
    def pagar(self, valor):
        print(f"Pagando R$ {valor:.2f} com cartão de crédito.")

class PagamentoBoleto(Pagamento):
    def pagar(self, valor):
        print(f"Gerando boleto no valor de R$ {valor:.2f}.")
        
class PagamentoPix(Pagamento):
    def pagar(self, valor):
        print(f"Gerando QR Code Pix para pagamento de R$ {valor:.2f}.")

class NotificacaoEmail(Notificacao):
    def enviar(self):
        print("Enviando e-mail de confirmação...")

class NotificacaoSMS(Notificacao):
    def enviar(self):
        print("Enviando SMS de confirmação...")
        
class AlterarStatusPedido:
    def alterar_status(self, pedido):
        pedido['status'] = 'finalizado'
        print(f"Status do pedido #{pedido['id']} alterado para finalizado.")
        
if __name__ == "__main__":
    meu_pedido = {
        'id': 123,
        'valor': 150.75,
        'cliente_email': 'cliente@exemplo.com',
        'status': 'pendente'
    }

    meu_pedido_2 = {
        'id': 456,
        'valor': 200.00,
        'cliente_email': 'cliente2@exemplo.com',
        'status': 'pendente'
    }
    
    processador = ProcessadorDePedidos()
    processador.processar(meu_pedido)

    pagamento_cartao = PagamentoCartaoCredito()
    pagamento_cartao.pagar(meu_pedido['valor'])
    
    notificacao_email = NotificacaoEmail()
    notificacao_email.enviar()
    
    alterador_status = AlterarStatusPedido()
    alterador_status.alterar_status(meu_pedido)
    
    print("-"*20)
    
    # PEDIDO 02
    processador.processar(meu_pedido_2)
    
    pagamento_pix = PagamentoPix()
    pagamento_pix.pagar(meu_pedido_2['valor'])
    
    # Enviando notificações
    notificacao_sms = NotificacaoSMS()
    notificacao_sms.enviar()
    
    alterador_status.alterar_status(meu_pedido_2)
    
    print("-"*20)