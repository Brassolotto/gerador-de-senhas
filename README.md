# Gerador de Senhas em Python

## 📝 Descrição
Um gerador de senhas seguras desenvolvido em Python que permite criar senhas com diferentes níveis de complexidade. O programa oferece opções para senhas básicas, médias e fortes, atendendo a diferentes necessidades de segurança.

## 🚀 Funcionalidades
- Geração de senhas com comprimento personalizado
- Três níveis de complexidade:
  - Básica: apenas letras minúsculas
  - Média: letras minúsculas e números
  - Forte: letras (maiúsculas e minúsculas), números e caracteres especiais
- Interface via linha de comando
- Validação de entradas
- Opção de sair do programa a qualquer momento

## 📋 Pré-requisitos
- Python 3.6 ou superior instalado
- Módulos utilizados:
  - random (biblioteca padrão)

## 🔧 Como executar
1. Clone este repositório:
```bash
git clone https://github.com/Brassolotto/gerador-de-senhas.git
```

2. Navegue até o diretório do projeto:
```bash
cd gerador-de-senhas
```

3. Execute o programa:
```bash
python gerador_de_senhas.py
```

## 📖 Como usar
1. Digite o tamanho desejado para a senha
2. Escolha o nível de complexidade:
   -  Básica
   -  Média
   -  Forte
3. A senha será gerada e exibida na tela
4. Para sair, digite 'sair' quando solicitado o tamanho da senha

## 🎯 Exemplos de uso
```
Gerador de senhas!
Digite 'sair' para encerrar

Digite o tamanho da senha: 8
Escolha o tipo de senha:
[1] Básica
[2] Média
[3] Forte
Sua escolha: 3

Sua senha forte é: Kj9#mP2$
```

## ⚠️ Validações e Tratamento de Erros
- Verificação de entrada numérica válida
- Tamanho mínimo de senha
- Tratamento de opções inválidas
- Tratamento de erros inesperados

## 🔍 Estrutura do Código
```
gerador_senhas.py
├── Listas de caracteres (maiúsculas, minúsculas, números, especiais)
├── Função gerar_senha_basica()
├── Função gerar_senha_media()
├── Função gerar_senha_forte()
└── Função main()
```

## 🤝 Contribuindo
Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## ✨ Melhorias Futuras
- [ ] Interface gráfica
- [ ] Opção para copiar senha para área de transferência
- [ ] Verificação de força da senha gerada
- [ ] Garantia de pelo menos um caractere de cada tipo
- [ ] Opção para evitar caracteres ambíguos
- [ ] Geração de múltiplas senhas simultaneamente

## 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor
Seu Nome
- GitHub: [@seu-usuario](https://github.com/Brassolotto)
- LinkedIn: [@seu-linkedin](https://linkedin.com/in/ricardo-brassolotto)

---
⌨️ com ❤️ por [Seu Nome] 😊