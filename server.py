import rpyc

class MathService(rpyc.Service):
    def on_connect(self, conn):
        print("Conexão estabelecida.")
    
    def on_disconnect(self, conn):
        print("Conexão encerrada.")
    
    def exposed_sum_and_divide(self, a, b, c):
        # Realiza a soma de a e b
        result = (a + b) / c  # Divide o resultado pelo valor c
        return result

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(MathService, port=18861)
    print("Servidor iniciado. Aguardando conexões...")
    server.start()
