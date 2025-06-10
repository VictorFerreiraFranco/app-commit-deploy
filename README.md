# Commit Deploy

Uma ferramenta pessoal criada para facilitar o processo de geração de builds no meu ambiente de trabalho. Com essa aplicação, é possível selecionar sistemas, inserir o hash do commit desejado e salvar o pacote final em uma pasta específica.

## Funcionalidades

- Interface gráfica simples e intuitiva
- Seleção de diferentes sistemas
- Inserção do hash do commit
- Geração de executável com base nas informações fornecidas
- Salvamento automático na pasta de destino

## Requisitos

- Windows
- Python 3.x

## Instalação

1. **Python 3:** Certifique-se de ter o Python 3 instalado no seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).  
   Durante a instalação no Windows, marque a opção **"Add Python to PATH"**.

2. **Atualizar o pip (opcional, mas recomendado):**
   ```bash
   python.exe -m pip install --upgrade pip --user
   ```

3. **Instalar o PyInstaller:**
   ```bash
   pip install -U pyinstaller
   ```

3. **Gerar o executável:**

   No diretório onde está o arquivo commit_deploy.py, execute:
   ```bash
   python -m PyInstaller --onefile --windowed commit_deploy.py
   ```
   O executável será gerado na pasta dist/.

## Licença
Este projeto foi criado com fins pessoais, mas está disponível para quem quiser usar, modificar ou aprimorar.
Você pode utilizar livremente, inclusive para fins comerciais, por sua conta e risco.

Todos os direitos reservados ao autor, mas sem restrições para uso.

Se fizer algo legal com essa base, sinta-se à vontade para compartilhar!
