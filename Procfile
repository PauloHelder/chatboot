# O Railway define a variável PORT automaticamente, 
# mas é bom garantir que seu app a leia.
ENV PORT=8080

# Comando para rodar (exemplo com FastAPI/Uvicorn)
# IMPORTANTE: --host 0.0.0.0 e 
# CMD uvicorn main:app 



web: gunicorn app:app --host 0.0.0.0 --port $PORT
