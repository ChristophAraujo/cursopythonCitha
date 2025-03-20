import pandas as pd
import matplotlib.pyplot as plt
from plyer import notification
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import sqlite3
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Função 1: Ler e analisar CSV
def ler_analisar_csv(filepath):
    df = pd.read_csv(filepath)
    df['Total'] = df['Quantidade'] * df['Preço']
    total_por_produto = df.groupby('Produto')['Total'].sum()
    produto_mais_vendido = total_por_produto.idxmax()
    total_geral = total_por_produto.sum()
    return df, total_por_produto, produto_mais_vendido, total_geral

# Função 2: Enviar notificação
def enviar_notificacao(produto_mais_vendido, total_geral):
    notification.notify(
        title="Resumo de Vendas",
        message=f"Produto mais vendido: {produto_mais_vendido}\nTotal geral: R${total_geral:.2f}",
        timeout=10
    )

# Função 3: Gerar relatório em Excel
def gerar_relatorio_excel(df, total_por_produto, output_path):
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Vendas', index=False)
        total_por_produto.to_excel(writer, sheet_name='Resumo')

# Função 4: Enviar e-mail com relatório
def enviar_email(relatorio_path, destinatario, remetente, senha):
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = "Relatório de Vendas"
    
    with open(relatorio_path, 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(relatorio_path)}')
        msg.attach(part)
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(remetente, senha)
        server.send_message(msg)

# Função 5: Gerar gráfico
def gerar_grafico(total_por_produto, output_path):
    total_por_produto.plot(kind='bar', title='Vendas por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Total Vendido')
    plt.savefig(output_path)

# Função 6: Agendar execução automática
def agendar_execucao(func, horario):
    import schedule
    import time
    schedule.every().day.at(horario).do(func)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Função 7: Análise de indicadores de desempenho
def calcular_kpis(df):
    ticket_medio = df['Total'].mean()
    produtos_lucro_baixo = df[df['Preço'] < 10]['Produto'].unique()
    top3_produtos = df.groupby('Produto')['Total'].sum().nlargest(3)
    return ticket_medio, produtos_lucro_baixo, top3_produtos

# Função 8: Atualizar banco de dados SQLite
def atualizar_banco_dados(df, db_path):
    conn = sqlite3.connect(db_path)
    df.to_sql('vendas', conn, if_exists='append', index=False)
    conn.close()

# Função 9: Monitorar pasta para novos arquivos
class MonitorarPasta(FileSystemEventHandler):
    def __init__(self, func):
        self.func = func

    def on_created(self, event):
        if event.src_path.endswith('.csv'):
            self.func(event.src_path)

def monitorar_pasta(pasta, func):
    observer = Observer()
    observer.schedule(MonitorarPasta(func), pasta, recursive=False)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()